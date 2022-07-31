import scrapy


class MarketairItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    images = scrapy.Field()