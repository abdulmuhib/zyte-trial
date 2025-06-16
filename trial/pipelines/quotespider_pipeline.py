from itemadapter import ItemAdapter

from ..constants.quotespider_constants import QuoteSpiderConstants


class QuoteSpiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # text --> clean text
        text = adapter.get(QuoteSpiderConstants.FIELD_TEXT)
        cleaned = text.translate(str.maketrans({'“': '', '”': '', '"': ''}))
        adapter[QuoteSpiderConstants.FIELD_TEXT] = cleaned
        return item
