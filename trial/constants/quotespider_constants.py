class QuoteSpiderConstants:
    # Spider Metadata
    SPIDER_NAME = 'quotespider'
    ALLOWED_DOMAINS = ['quotes.toscrape.com']

    # URL Paths
    BASE_URL = 'http://quotes.toscrape.com/scroll'

    # Field Names
    FIELD_AUTHOR = 'author'
    FIELD_TAG = 'tags'
    FIELD_TEXT = 'text'
