import scrapy


class YokohamatyresItem(scrapy.Item):
    manufacturer_unique_id = scrapy.Field()
    store_name = scrapy.Field()
    full_address = scrapy.Field()
    email_id = scrapy.Field()
    phone_number = scrapy.Field()
    state = scrapy.Field()
    district = scrapy.Field()
    pincode = scrapy.Field()
    yokohama_zone = scrapy.Field()
    brand = scrapy.Field()
    google_maps_direction_url = scrapy.Field()
    dealer_name = scrapy.Field()