import scrapy
import time
from pincode.items import PincodeItem

postals = list()


class PincodespiderSpider(scrapy.Spider):
    name = 'pincodespider'
    start_urls = ['https://www.indiatvnews.com/india-pin-codes/']


    def parse(self, response, **kwargs):

        box1 = response.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/div[3]/ul//@href').extract()
        for href in box1:
            print('href --> ', href)
            view_url = "https://www.indiatvnews.com" + str(href)
            print('view_url --> ', view_url)
            url = view_url
            yield scrapy.Request(url, callback=self.parse2, priority=1)

    def parse2(self, response):
        box = response.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/div[3]/ul//@href').extract()
        for href in box:
            view_url = "https://www.indiatvnews.com" + str(href)
            url = view_url
            yield scrapy.Request(url, callback=self.parse_items, priority=1)

    def parse_items(self, response):
        table = response.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/div[3]/table')

        for lop in table:
            pins = lop.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/div[3]/table/tbody//tr/td[5]/text()')
            for pin in pins:
                p = pin.extract()

                if p not in postals:
                    print('p --> ', p)
                    postals.append(p)
                else:
                    print('Already Exists So Not Appending --> ', p)

        print('postals --> ', postals)
