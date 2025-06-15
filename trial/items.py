# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from .constants import BookSpiderConstants


class BookSpiderItem(scrapy.Item):
    fields = {
        BookSpiderConstants.FIELD_URL: scrapy.Field(),
        BookSpiderConstants.FIELD_TITLE: scrapy.Field(),
        BookSpiderConstants.FIELD_PRICE: scrapy.Field(),
        BookSpiderConstants.FIELD_PRICE_EXCL: scrapy.Field(),
        BookSpiderConstants.FIELD_PRICE_INCL: scrapy.Field(),
        BookSpiderConstants.FIELD_AVAIL: scrapy.Field(),
        BookSpiderConstants.FIELD_STARS: scrapy.Field(),
    }
