import scrapy
from district.items import DistrictItem


class DistrictspiderSpider(scrapy.Spider):
    name = 'districtspider'
    start_urls = ['https://instapdf.in/india-all-state-district-name-list/']

    def parse(self, response, **kwargs):
        items = DistrictItem()

        table = response.xpath('//*[@id="post-23838"]/div[4]/table/tbody')
        for dist in table:

            district_list = dist.xpath('//*[@id="post-23838"]/div[4]/table/tbody//tr/td[2]/text()').extract()
            print('district_list --> ', district_list)

            items['district_list'] = district_list
            yield items