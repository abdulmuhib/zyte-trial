import scrapy

from ..constants.quotespider_constants import QuoteSpiderConstants


class QuoteSpiderItem(scrapy.Item):
    fields = {
        QuoteSpiderConstants.FIELD_AUTHOR: scrapy.Field(),
        QuoteSpiderConstants.FIELD_TAG: scrapy.Field(),
        QuoteSpiderConstants.FIELD_TEXT: scrapy.Field(),
    }
