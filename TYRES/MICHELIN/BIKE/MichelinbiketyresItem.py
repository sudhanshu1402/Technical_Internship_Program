import scrapy


class MichelinbiketyresItem(scrapy.Item):
    manufacturer_unique_id = scrapy.Field()
    store_name = scrapy.Field()
    full_address = scrapy.Field()
    email_id = scrapy.Field()
    phone_number = scrapy.Field()
    state = scrapy.Field()
    district = scrapy.Field()
    pincode = scrapy.Field()
    michelin_certified_centre = scrapy.Field()
    brand = scrapy.Field()
    google_maps_direction_url = scrapy.Field()
    website = scrapy.Field()
    appointment_booking_url = scrapy.Field()
    brand_website_store_url = scrapy.Field()
