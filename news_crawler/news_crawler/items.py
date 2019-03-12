import scrapy


class NewsItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
