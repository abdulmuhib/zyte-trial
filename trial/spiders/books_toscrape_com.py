import scrapy
# from dotenv import load_dotenv

from ..constants import BookSpiderConstants
from ..items import BookSpiderItem

# load_dotenv()


class BookSpider(scrapy.Spider):
    name = BookSpiderConstants.SPIDER_NAME
    allowed_domains = BookSpiderConstants.ALLOWED_DOMAINS

    @classmethod
    def update_settings(cls, settings):
        super(BookSpider, cls).update_settings(settings)
        settings["RETRY_HTTP_CODES"] = [500, 502, 503, 504, 522, 524, 408, 521, 520]
        settings["RETRY_TIMES"] = 3
        settings['DOWNLOAD_TIMEOUT'] = 60
        settings['ZYTE_API_ENABLED'] = True
        settings['ZYTE_API_MAX_RETRIES'] = 3
        settings['ADDONS'] = {
            "scrapy_zyte_api.Addon": 500,
        }
        items_pipeline = settings['ITEM_PIPELINES']
        items_pipeline['trial.pipelines.BookSpiderPipeline'] = 300

    def start_requests(self):
        yield scrapy.Request(
            BookSpiderConstants.BASE_URL,
            callback=self.parse,
            meta={"zyte_api_automap": {"browserHtml": True}}
        )

    def parse(self, response):
        books = response.css(BookSpiderConstants.BOOKS_LIST_SELECTOR)
        for book in books:
            relative_url = book.css(BookSpiderConstants.BOOK_LINK_SELECTOR).get()

            if BookSpiderConstants.CATALOGUE_PATH in relative_url:
                book_url = BookSpiderConstants.BASE_URL + relative_url
            else:
                book_url = BookSpiderConstants.CATALOGUE_URL + relative_url

            yield scrapy.Request(
                book_url,
                callback=self.parse_book_page,
                meta={"zyte_api_automap": {"browserHtml": True}}
            )

        next_page = response.css(BookSpiderConstants.PAGINATION_SELECTOR).get()
        if next_page:
            if BookSpiderConstants.CATALOGUE_PATH in next_page:
                next_page_url = BookSpiderConstants.BASE_URL + next_page
            else:
                next_page_url = BookSpiderConstants.CATALOGUE_URL + next_page

            yield response.follow(
                next_page_url,
                callback=self.parse,
                meta={"zyte_api_automap": {"browserHtml": True}}
            )

    def parse_book_page(self, response):
        book = response.css(BookSpiderConstants.PRODUCT_MAIN_SELECTOR)[0]
        book_item = BookSpiderItem()

        print(self.extract_table_value(response, BookSpiderConstants.AVAILABILITY_HEADER))

        book_item[BookSpiderConstants.FIELD_URL] = response.url
        book_item[BookSpiderConstants.FIELD_TITLE] = book.css(BookSpiderConstants.TITLE_SELECTOR).get()
        book_item[BookSpiderConstants.FIELD_PRICE] = book.css(BookSpiderConstants.PRICE_SELECTOR).get()
        book_item[BookSpiderConstants.FIELD_PRICE_EXCL] = self.extract_table_value(response,
                                                                                   BookSpiderConstants.PRICE_EXCL_TAX_HEADER)
        book_item[BookSpiderConstants.FIELD_PRICE_INCL] = self.extract_table_value(response,
                                                                                   BookSpiderConstants.PRICE_INCL_TAX_HEADER)
        book_item[BookSpiderConstants.FIELD_AVAIL] = self.extract_table_value(response,
                                                                              BookSpiderConstants.AVAILABILITY_HEADER)
        book_item[BookSpiderConstants.FIELD_STARS] = book.css(BookSpiderConstants.STARS_CLASS_SELECTOR).attrib['class']
        yield book_item

    def extract_table_value(self, response, header_name):
        xpath_expr = BookSpiderConstants.TABLE_VALUE_XPATH.format(header_name)
        return response.xpath(xpath_expr).get()
