import time
from scrapy.spiders import SitemapSpider
from selenium import webdriver
from supplyhouse.SupplyhouseItem import SupplyhouseItem

class SupplyhousespiderSpider(SitemapSpider):
    name = 'supplyhousespider'
    sitemap_urls = [
                        'https://www.supplyhouse.com/sitemap_products_1.xml',
                        'https://www.supplyhouse.com/sitemap_products_2.xml'
                    ]

    def parse(self, response, **kwargs):
        items = SupplyhouseItem()

        ####################
        ####################

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1200,1100")
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')

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

        driver.get(url)
        driver.maximize_window()
        time.sleep(15)

        ####################
        ####################

        try:
            title = driver.find_element_by_xpath('//*[@id="product-layout-helper"]/div[3]/strong').text
        except Exception as e:
            title = ''
            print('Exception while getting product title --> ', e)
            pass
        print('title --> ', title)
        items['title'] = title

        ####################
        ####################

        try:
            sku = driver.find_element_by_xpath('//*[@id="product-layout-helper"]/div[5]/div[1]/div[2]/div[1]/strong').text
        except Exception as e:
            sku = ''
            print('Exception while getting product sku --> ', e)
            pass
        print('sku --> ', sku)
        items['sku'] = sku

        ####################
        ####################

        try:
            brand = driver.find_element_by_xpath('//*[@id="product-layout-helper"]/div[5]/div[1]/div[2]/div[2]/strong').text
        except Exception as e:
            brand = ''
            print('Exception while getting product brand --> ', e)
            pass
        print('brand --> ', brand)
        items['brand'] = brand

        ####################
        ####################

        try:
            price = driver.find_element_by_xpath('//*[@class="relative"]').text.replace('$', '')
        except Exception as e:
            price = ''
            print('Exception while getting product price --> ', e)
            pass
        print('price --> ', price)
        items['price'] = price

        ####################
        ####################

        try:
            if driver.find_element_by_xpath('//*[@class="prod-desc-content section-content"]').text == None:
                desc = ""
            else:
                desc = driver.find_element_by_xpath('//*[@class="prod-desc-content section-content"]').text
        except Exception as e:
            desc = ''
            print('Exception while getting product desc --> ', e)
            pass
        print('desc --> ', desc)
        items['desc'] = str(desc).replace('\n', '').replace('Description', '')

        ####################
        ####################

        try:
            images = {}
            product_imgurls = driver.find_elements_by_xpath('/html/body/main/div[2]/div[2]/div[1]/div[3]/div/img')
            for img_urls in range(len(product_imgurls)):
                images.update({"image_url_" + str(img_urls + 1): product_imgurls[img_urls].get_attribute("src")})
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
            document_urls = driver.find_elements_by_xpath('//*[@id="prod-manuals-list"]/div/p/a')
            for doc_urls in range(len(document_urls)):
                docs.update({"doc_url_" + str(doc_urls + 1): document_urls[doc_urls].get_attribute("href")})
        except Exception as e:
            docs = ''
            print('Exception while getting product docs --> ', e)
            pass
        print('docs --> ', docs)
        items['docs'] = docs

        ####################
        ####################

        try:
            specs = {}
            key = driver.find_elements_by_xpath('//*[@id="prod-spec-list"]/div[1]/div/div[@class="feature-type nowrap"]/strong')
            value = driver.find_elements_by_xpath('//*[@id="prod-spec-list"]/div[1]/div/div[@class="feature-value"]')
            for k in range(len(key)):
                d = key[k].text
                f = value[k].text
                specs.update({d: f})
        except Exception as e:
            specs = ''
            print('Exception while getting product specs --> ', e)
            pass
        print('specs --> ', specs)
        items['specs'] = specs

        ####################
        ####################

        yield items
