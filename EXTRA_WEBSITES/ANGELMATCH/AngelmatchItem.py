import scrapy


class AngelmatchItem(scrapy.Item):
    name = scrapy.Field()
    company_name = scrapy.Field()
    email_id = scrapy.Field()
    locations = scrapy.Field()
    links = scrapy.Field()
    investment_focuses = scrapy.Field()
    companies_invested_in = scrapy.Field()
    companies_invested_in_links = scrapy.Field()
    website = scrapy.Field()
