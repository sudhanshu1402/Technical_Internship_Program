import scrapy


class CeattyresItem(scrapy.Item):
    manufacturer_unique_id = scrapy.Field()
    store_name = scrapy.Field()
    full_address = scrapy.Field()
    email_id = scrapy.Field()
    phone_number = scrapy.Field()
    state = scrapy.Field()
    district = scrapy.Field()
    pincode = scrapy.Field()
    ceat_shoppe = scrapy.Field()
    brand = scrapy.Field()
