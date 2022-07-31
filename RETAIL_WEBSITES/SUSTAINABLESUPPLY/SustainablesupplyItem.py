import scrapy


class SustainablesupplyItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    sku = scrapy.Field()
    brand = scrapy.Field()
    mpn = scrapy.Field()
    weight = scrapy.Field()
    weight_unit = scrapy.Field()
    price = scrapy.Field()
    desc = scrapy.Field()
    specs = scrapy.Field()
    images = scrapy.Field()
    docs = scrapy.Field()
