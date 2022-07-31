from sustainablesupply.SustainablesupplyItem import SustainablesupplyItem
import re
import time
import scrapy
from selenium import webdriver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class SustainablesupplyspiderSpider(scrapy.Spider):
    name = 'sustainablesupplyspider'
    start_urls = [
        'https://www.sustainablesupply.com/collections/restroom-supplies#/perpage:48/sort:title:asc',
        'https://www.sustainablesupply.com/collections/electric-motors#/perpage:48/sort:title:asc',
        'https://www.sustainablesupply.com/collections/hvac-r-supplies#/perpage:48/sort:title:asc',
        'https://www.sustainablesupply.com/collections/plumbing-supplies#/perpage:48/sort:title:asc',
        'https://www.sustainablesupply.com/collections/safety-supplies#/perpage:48/sort:title:asc'
    ]

    def parse(self, response, **kwargs):
        url = response.request.url
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        yield scrapy.Request(url, callback=self.parse2, errback=self.parse_items, dont_filter=True)

        ####################
        ####################

    def parse2(self, response):
        for href in driver.find_elements_by_xpath('//*[@id="searchspring-content"]/section/div/div[2]/div/div/a'):
            view_url = "https://www.sustainablesupply.com" + str(href.get_attribute('ng-href'))
            print('view_url --> ', view_url)
            url = view_url
            yield scrapy.Request(url, callback=self.parse_items, errback=self.parse_items, dont_filter=True)

    def parse_items(self, response):
        items = SustainablesupplyItem()
        ####################
        ####################

        try:
            url = response.request.url
        except Exception as e:
            url = ''
            print('Exception while getting product url --> ', e)
            pass
        print('url --> ', url)
        items['url'] = url

        ####################
        ####################

        try:
            title = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[2]/div/div[1]/div/h1/text()').extract_first()
        except Exception as e:
            title = ''
            print('Exception while getting product title --> ', e)
            pass
        print('title --> ', title)
        items['title'] = title

        ####################
        ####################

        try:
            sku = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[2]/div/div[1]/div/div/span[1]/span/text()').extract_first()
        except Exception as e:
            sku = ''
            print('Exception while getting product sku --> ', e)
            pass
        print('sku --> ', sku)
        items['sku'] = sku

        ####################
        ####################

        try:
            brand = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[2]/div/div[1]/div/div/a/text()').extract_first()
        except Exception as e:
            brand = ''
            print('Exception while getting product brand --> ', e)
            pass
        print('brand --> ', brand)
        items['brand'] = brand

        ####################
        ####################

        try:
            mpn = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[2]/div/div[1]/div/div/span[2]/text()').extract_first()
        except Exception as e:
            mpn = ''
            print('Exception while getting product mpn --> ', e)
            pass
        print('mpn --> ', mpn)
        items['mpn'] = mpn

        ####################
        ####################

        try:
            weight = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[2]/div/div[1]/div/div/span[3]/text()').extract_first()
        except Exception as e:
            weight = ''
            print('Exception while getting product weight --> ', e)
            pass
        print('weight --> ', weight)
        items['weight'] = re.sub('[^0123456789.]', '', weight)

        ####################
        ####################

        try:
            string2 = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[2]/div/div[1]/div/div/span[3]/text()').extract_first()
            weight_unit = ''.join((x for x in string2 if not x.isdigit()))
        except Exception as e:
            weight_unit = ''
            print('Exception while getting product weight_unit --> ', e)
            pass
        print('weight_unit --> ', weight_unit)
        items['weight_unit'] = str(weight_unit).replace('.', '').replace(' ', '')

        ####################
        ####################

        try:
            price = response.xpath('//*[@class="price price--highlight"]/text()').extract_first().replace('$', '')
        except Exception as e:
            price = ''
            print('Exception while getting product price --> ', e)
            pass
        print('price --> ', price)
        items['price'] = price

        ####################
        ####################

        try:
            desc = response.xpath('//*[@class="product-block-list__item product-block-list__item--description"]/div/div/div/p/text()').extract_first()
            if desc is None:
                desc = response.xpath('//*[@class="product-block-list__item product-block-list__item--description"]/div/div/div/p/strong/text()').extract_first()
        except Exception as e:
            desc = ''
            print('Exception while getting product desc --> ', e)
            pass
        print('desc --> ', desc)
        items['desc'] = desc

        ####################
        ####################

        try:
            table_rows = response.xpath('//*[@style="padding-bottom:25px"]')
            specs = {}
            for table_row in table_rows:
                key = table_row.xpath('//tr/td/b/text()').extract()
                value = table_row.xpath('//tr/td/text()').extract()
                for k in range(len(key)):
                    d = key[k].replace('.', '')
                    f = value[k]
                    specs.update({d: f})
        except Exception as e:
            specs = ''
            print('Exception while getting product specs --> ', e)
            pass
        print('specs --> ', specs)
        items['specs'] = specs

        ####################
        ####################

        try:
            images = {}
            product_imgurls = response.xpath('//meta[@property="og:image:secure_url"]/@content').extract()
            for img_urls in range(len(product_imgurls)):
                images.update({"image_url_" + str(img_urls + 1): product_imgurls[img_urls]})
        except Exception as e:
            images = ''
            print('Exception while getting product images --> ', e)
            pass
        print('images --> ', images)
        items['images'] = images

        ####################
        ####################

        try:
            docs = {}
            document_urls = response.xpath(
                '//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div/div[4]//tr/td/a/@href').extract()
            for doc_urls in range(len(document_urls)):
                docs.update({"doc_url_" + str(doc_urls + 1): document_urls[doc_urls]})
        except Exception as e:
            docs = ''
            print('Exception while getting product docs --> ', e)
            pass
        print('docs --> ', docs)
        items['docs'] = docs

        ####################
        ####################

        yield items


        next_page = driver.find_element_by_class_name('pagination__next')
        if next_page is not None:
            next_page.location_once_scrolled_into_view
            time.sleep(3)
            next_page.click()
            time.sleep(5)
            print('ON NEXT PAGE')