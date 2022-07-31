import scrapy


class SupplyhouseItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    sku = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    desc = scrapy.Field()
    specs = scrapy.Field()
    images = scrapy.Field()
    docs = scrapy.Field()
