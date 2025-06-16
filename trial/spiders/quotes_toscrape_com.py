import json
from base64 import b64decode

from scrapy import Request, Spider

from ..constants.quotespider_constants import QuoteSpiderConstants
from ..items.quotespider_item import QuoteSpiderItem


class QuoteSpider(Spider):
    name = QuoteSpiderConstants.SPIDER_NAME
    allowed_domains = QuoteSpiderConstants.ALLOWED_DOMAINS

    @classmethod
    def update_settings(cls, settings):
        super(QuoteSpider, cls).update_settings(settings)
        settings["RETRY_HTTP_CODES"] = [500, 502, 503, 504, 522, 524, 408, 521, 520]
        settings["RETRY_TIMES"] = 3
        settings['DOWNLOAD_TIMEOUT'] = 60
        settings['ZYTE_API_ENABLED'] = True
        settings['ZYTE_API_MAX_RETRIES'] = 3
        settings['ADDONS'] = {
            "scrapy_zyte_api.Addon": 500,
        }
        items_pipeline = settings['ITEM_PIPELINES']
        items_pipeline['trial.pipelines.quotespider_pipeline.QuoteSpiderPipeline'] = 300

    def start_requests(self):
        yield Request(
            QuoteSpiderConstants.BASE_URL,
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                    "actions": [
                        {
                            "action": "scrollBottom",
                        },
                    ],
                    "networkCapture": [
                        {
                            "filterType": "url",
                            "httpResponseBody": True,
                            "value": "/api/",
                            "matchType": "contains",
                        },
                    ],
                },
            },
        )

    def parse(self, response):
        for capture in response.raw_api_response["networkCapture"]:
            text = b64decode(capture["httpResponseBody"]).decode()
            data = json.loads(text)
            quote_item = QuoteSpiderItem()
            for quote in data["quotes"]:
                quote_item[QuoteSpiderConstants.FIELD_AUTHOR] = quote["author"]["name"]
                quote_item[QuoteSpiderConstants.FIELD_TAG] = quote["tags"]
                quote_item[QuoteSpiderConstants.FIELD_TEXT] = quote["text"]
                yield quote_item
