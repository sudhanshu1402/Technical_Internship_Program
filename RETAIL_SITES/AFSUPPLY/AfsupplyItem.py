import scrapy


class AfsupplyItem(scrapy.Item):
    title = scrapy.Field()
    sku = scrapy.Field()
    price = scrapy.Field()
    retail_price = scrapy.Field()
    stock = scrapy.Field()
    mpn = scrapy.Field()
    upc = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    specs = scrapy.Field()
    url = scrapy.Field()
    docs = scrapy.Field()
    image_urls = scrapy.Field()
