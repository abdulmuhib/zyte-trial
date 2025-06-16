# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from ..constants.bookspider_constants import BookSpiderConstants


class BookSpiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            value = adapter.get(field_name)
            adapter[field_name] = value.strip()

        ## Price --> convert to float
        price_keys = [BookSpiderConstants.FIELD_PRICE,
                      BookSpiderConstants.FIELD_PRICE_EXCL,
                      BookSpiderConstants.FIELD_PRICE_INCL]
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace(BookSpiderConstants.CURRENCY_SIGN, '')
            adapter[price_key] = float(value)

        ## Availability --> extract number of books in stock
        availability_string = adapter.get(BookSpiderConstants.FIELD_AVAIL)
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter[BookSpiderConstants.FIELD_AVAIL] = BookSpiderConstants.AVAIL_STATUS_OUT_OF_STO
        else:
            adapter[BookSpiderConstants.FIELD_AVAIL] = split_string_array[0].strip()

        ## Stars --> convert text to number
        stars_string = adapter.get(BookSpiderConstants.FIELD_STARS)
        split_stars_array = stars_string.split(' ')
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == BookSpiderConstants.ZERO_STR:
            adapter[BookSpiderConstants.FIELD_STARS] = 0
        elif stars_text_value == BookSpiderConstants.ONE_STR:
            adapter[BookSpiderConstants.FIELD_STARS] = 1
        elif stars_text_value == BookSpiderConstants.TWO_STR:
            adapter[BookSpiderConstants.FIELD_STARS] = 2
        elif stars_text_value == BookSpiderConstants.THREE_STR:
            adapter[BookSpiderConstants.FIELD_STARS] = 3
        elif stars_text_value == BookSpiderConstants.FOUR_STR:
            adapter[BookSpiderConstants.FIELD_STARS] = 4
        elif stars_text_value == BookSpiderConstants.FIVE_STR:
            adapter[BookSpiderConstants.FIELD_STARS] = 5

        return item
