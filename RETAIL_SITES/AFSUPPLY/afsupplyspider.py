from scrapy.spiders import SitemapSpider
from Hub.models.voomi.AfsupplyItem import AfsupplyItem
from bs4 import BeautifulSoup
import requests as rq


class AfsupplyspiderSpider(SitemapSpider):
    name = 'afsupplyspider'
    sitemap_urls = [
        'https://www.afsupply.com/sitemap_1.xml',
        'https://www.afsupply.com/sitemap_2.xml',
        'https://www.afsupply.com/sitemap_3.xml'
    ]

    def parse(self, response, **kwargs):

        items = AfsupplyItem()
        print('-----------------------------------')

        ####################
        ####################

        try:
            title = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[1]/h1/span/text()').extract_first()
            if title is None:
                exit()
        except Exception as e:
            title = ''
            print('Exception while getting product title -->', e)
            pass
        print(' title --> ', title)
        items['title'] = title

        ####################
        ####################

        try:
            sku = response.xpath(
                '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[@class="value"]/text()').extract_first()
            if sku is True:
                sku = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[@class="value"]/text()').extract_first()
            elif sku is None:
                sku = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/text()').extract_first()
        except Exception as e:
            sku = ''
            print('Exception while getting product sku --> ', e)
            pass
        print(' sku --> ', sku)
        items['sku'] = sku

        ####################
        ####################

        try:
            stock = response.xpath(
                '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[@class="availability only"]/strong/text()').extract_first()
            if stock is True:
                stock = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[@class="availability only"]/strong/text()').extract_first()
            if stock is None:
                stock = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/p/span/text()').extract_first()
            if stock is None:
                stock = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2]/div[2][@class="shipinfo-right"]/span[4]/strong/text()').extract_first()
            if stock is None:
                stock = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[2][@class="product-info-price"]/span/strong/text()').extract_first()
        except Exception as e:
            stock = ''
            print('Exception while getting product stock --> ', e)
            pass
        print(' stock --> ', stock)
        items['stock'] = stock

        ####################
        ####################

        try:
            price = response.xpath('//*[@data-price-type="finalPrice"]/span/text()').extract_first()
            if response.xpath('//*[@data-price-type="finalPrice"]/span/text()').extract_first() is None:
                price = ""
        except Exception as e:
            price = ''
            print('Exception while getting product price --> ', e)
            pass
        print(' price --> ', price)
        items['price'] = str(price).replace('$', '').replace(',', '')

        ####################
        ####################

        try:
            if response.xpath('//*[@data-price-type="oldPrice"]/span/text()').extract_first() is None:
                retail_price = ""
            else:
                retail_price = response.xpath('//*[@data-price-type="oldPrice"]/span/text()').extract_first()
        except Exception as e:
            retail_price = ''
            print('Exception while getting product retail_price --> ', e)
            pass
        print(' retail_price --> ', retail_price)
        items['retail_price'] = str(retail_price).replace('$', '').replace(',', '')

        ####################
        ####################

        try:
            description = response.xpath('//*[@id="description"]').extract()
            if description is None:
                description = ''
        except Exception as e:
            description = ''
            print('Exception while getting product description --> ', e)
            pass
        print(' description --> ', description)
        items['description'] = str(description)

        ####################
        ####################

        try:
            url = response.request.url
        except Exception as e:
            url = ''
            print('Exception while getting product url --> ', e)
            pass
        print(' url --> ', url)
        items['url'] = url

        ####################
        ####################

        table_rows = response.xpath('//*[contains(@class,"additional-attributes")]//tr')
        specs = {}
        mpn = ""
        upc = ""
        brand = ""
        for table_row in table_rows:
            specs[table_row.xpath('th[@class="col label"]/text()').extract_first().strip()] \
                = table_row.xpath('td[@class="col data"]/text()').extract_first().strip()

            if table_row.xpath('th[@class="col label"]/text()').extract_first().strip() == 'MPN':
                mpn = table_row.xpath('td[@class="col data"]/text()').extract_first().strip()
                if table_row.xpath('td[@class="col data"]/text()').extract_first().strip() is None:
                    mpn = ""

            if table_row.xpath('th[@class="col label"]/text()').extract_first().strip() == 'UPC / GTIN':
                upc = table_row.xpath('td[@class="col data"]/text()').extract_first().strip()
                if table_row.xpath('td[@class="col data"]/text()').extract_first().strip() is None:
                    upc = ""

            if table_row.xpath('th[@class="col label"]/text()').extract_first().strip() == 'Manufacturer':
                brand = table_row.xpath('td[@class="col data"]/text()').extract_first().strip()
                if table_row.xpath('td[@class="col data"]/text()').extract_first().strip() is None:
                    brand = ""

        items['mpn'] = mpn
        items['upc'] = upc
        items['brand'] = brand
        items['specs'] = specs
        ####################
        ####################

        try:
            docs = response.xpath('//*[@id="demo.tab"]/a/@href').extract_first()
            if docs is None:
                docs = ""
            else:
                doks = "https://www.afsupply.com" + (response.xpath('//*[@id="demo.tab"]/a/@href').extract_first())
                docs = '[{"Product Specifications" : ' + '"' + doks + '"' + '}]'
        except Exception as e:
            docs = ''
            print('Exception while getting product docs --> ', e)
            pass
        print(' docs --> ', docs)
        items['docs'] = docs

        ####################
        ####################

        try:
            r2 = rq.get(url)
            soup = BeautifulSoup(r2.text, "html.parser")
            image_urls = []
            x = soup.select(
                'img[src^="https://www.afsupply.com/media/catalog/product/cache/2f6d849428e32928a663b11523157b79/"]')
            for img in x:
                image_urls.append(img['src'])
            if image_urls is None:
                image_urls = ""
        except Exception as e:
            image_urls = ''
            print('Exception while getting product image_urls --> ', e)
            pass
        print(' image_urls --> ', image_urls)
        items['image_urls'] = image_urls

        ####################
        ####################

        yield items
