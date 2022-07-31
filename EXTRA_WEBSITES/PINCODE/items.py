import scrapy


class PincodeItem(scrapy.Item):
    pin = scrapy.Field()
    postals = scrapy.Field()