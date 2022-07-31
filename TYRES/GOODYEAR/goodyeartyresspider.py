from goodyeartyres.GoodyeartyresItem import GoodyeartyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class GoodyeartyresspiderSpider(scrapy.Spider):
    name = 'goodyeartyresspider'
    start_urls = ['https://www.goodyear.co.in/store']

    def parse(self, response, **kwargs) :

        driver.get('https://www.goodyear.co.in/store')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        while True:

            print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
            listt = driver.find_element_by_xpath('//*[@id="store-list"]').get_attribute('outerHTML')
            print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

            soup = BeautifulSoup(listt, features='lxml')
            templatenode = soup.find_all('div', {'class': 'store-box'})
            print('FINDING ALL DIVS IN DEALER LIST')

            for href in templatenode:

                store_link = href.find("a", {"class": "store-title"}).get('href')
                view_url = 'https://www.goodyear.co.in/' + str(store_link)
                url = view_url
                print(' url --> ', url)
                yield scrapy.Request(url, callback=self.parse_items)

            time.sleep(3)
            next_page = driver.find_element_by_css_selector('a.next.pagination')
            if next_page is not None:
                next_page.click()
                print('ON Next Page')
                time.sleep(3)

    def parse_items(self, response):
        items = GoodyeartyresItem()

        ####################
        ####################
        try:
            manufacturer_unique_id = ''
        except Exception as e:
            manufacturer_unique_id = ''
            print('Exception while getting manufacturer_unique_id --> ', e)
            pass
        print('manufacturer_unique_id -> ', manufacturer_unique_id)
        items['manufacturer_unique_id'] = manufacturer_unique_id
        ####################
        ####################
        try:
            store_name = response.xpath('//*[@id="wapper"]/div/div/div/div/div[1]/div[1]/div/div[1]/p/strong/text()').extract_first()
        except Exception as e:
            store_name = ''
            print('Exception while getting store_name --> ', e)
            pass
        print('store_name ->', store_name)
        items['store_name'] = store_name
        ####################
        ####################
        try:
            full_address = response.xpath('//*[@id="wapper"]/div/div/div/div/div[1]/div[1]/div/div[1]/p/span/text()').extract_first()
        except Exception as e:
            full_address = ''
            print('Exception while getting full_address --> ', e)
            pass
        print('full_address ->', full_address)
        items['full_address'] = full_address
        ####################
        ####################
        try:
            if response.xpath('//*[@id="wapper"]/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/p[2]/a/text()').extract_first() == None:
                email_id = ''
            else:
                email_id = response.xpath('//*[@id="wapper"]/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/p[2]/a/text()').extract_first()
        except Exception as e:
            email_id = ''
            print('Exception while getting email_id --> ', e)
            pass
        print('email_id ->', email_id)
        items['email_id'] = email_id
        ####################
        ####################
        try:
            phone_number = response.xpath('//*[@id="wapper"]/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/p[1]/span/text()').extract_first()
        except Exception as e:
            phone_number = ''
            print('Exception while getting phone_number --> ', e)
            pass
        print('phone_number ->', phone_number)
        items['phone_number'] = phone_number
        ####################
        ####################
        try:
            district = ''
        except Exception as e:
            district = ''
            print('Exception while getting district --> ', e)
            pass
        print('district ->', district)
        items['district'] = district
        ####################
        ####################
        try:
            pincode = ''
        except Exception as e:
            pincode = ''
            print('Exception while getting pincode --> ', e)
            pass
        print('pincode --> ', pincode)
        items['pincode'] = pincode
        ####################
        ####################
        try:
            if response.xpath('//*[@id="wapper"]/div/div/div/div/div[1]/div/div/div[3]/text()').extract_first() == 'Goodyear Retailer':
                goodyear_zone = '1'
            else:
                goodyear_zone = '0'
        except Exception as e:
            goodyear_zone = ''
            print('Exception while getting goodyear_zone --> ', e)
            pass
        print('goodyear_zone --> ', goodyear_zone)
        items['goodyear_zone'] = goodyear_zone
        ####################
        ####################
        try:
            brand = 'Good Year'
        except Exception as e:
            brand = ''
            print('Exception while getting brand --> ', e)
            pass
        print('brand --> ', brand)
        items['brand'] = brand
        ####################
        ####################
        try:
            website = response.request.url
        except Exception as e:
            website = ''
            print('Exception while getting website --> ', e)
            pass
        print('website --> ', website)
        items['website'] = website
        ####################
        ####################
        yield items
