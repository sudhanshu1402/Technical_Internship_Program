import scrapy


class BridgestonetyresItem(scrapy.Item):
    manufacturer_unique_id = scrapy.Field()
    store_name = scrapy.Field()
    full_address = scrapy.Field()
    email_id = scrapy.Field()
    phone_number = scrapy.Field()
    state = scrapy.Field()
    district = scrapy.Field()
    pincode = scrapy.Field()
    brand = scrapy.Field()
    website = scrapy.Field()
    google_maps_direction_url = scrapy.Field()
    appointment_booking_url = scrapy.Field()