class BookSpiderConstants:
    # Spider Metadata
    SPIDER_NAME = 'bookspider'
    ALLOWED_DOMAINS = ['books.toscrape.com']

    # URL Paths
    BASE_URL = 'https://books.toscrape.com/'
    CATALOGUE_PATH = 'catalogue/'
    CATALOGUE_URL = BASE_URL + CATALOGUE_PATH

    # Table Headers
    PRICE_EXCL_TAX_HEADER = 'Price (excl. tax)'
    PRICE_INCL_TAX_HEADER = 'Price (incl. tax)'
    AVAILABILITY_HEADER = 'Availability'

    # Field Names
    FIELD_URL = 'url'
    FIELD_TITLE = 'title'
    FIELD_PRICE = 'price'
    FIELD_PRICE_EXCL = 'price_excl_tax'
    FIELD_PRICE_INCL = 'price_incl_tax'
    FIELD_AVAIL = 'availability'
    FIELD_STARS = 'stars'

    # Selectors
    BOOKS_LIST_SELECTOR = 'article.product_pod'
    BOOK_LINK_SELECTOR = 'h3 a::attr(href)'
    PAGINATION_SELECTOR = 'li.next a::attr(href)'
    PRODUCT_MAIN_SELECTOR = 'div.product_main'
    TITLE_SELECTOR = 'h1::text'
    PRICE_SELECTOR = 'p.price_color::text'
    STARS_CLASS_SELECTOR = 'p.star-rating'

    # XPath Template
    TABLE_VALUE_XPATH = "//tr[th[text()='{}']]/td/text()"

    # General
    CURRENCY_SIGN = '£'
    AVAIL_STATUS_OUT_OF_STO = 'Out of stock'
    ZERO_STR = 'zero'
    ONE_STR = 'one'
    TWO_STR = 'two'
    THREE_STR = 'three'
    FOUR_STR = 'four'
    FIVE_STR = 'five'
