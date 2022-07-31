from bridgestonetyres.BridgestonetyresItem import BridgestonetyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')

class BridgestonetyresspiderSpider(scrapy.Spider):
    name = 'bridgestonetyresspider'
    start_urls = ['https://select.bridgestone.co.in/']

    def parse(self, response, **kwargs):

        driver.get('https://select.bridgestone.co.in/')
        print('Getting To Store Locator Page')
        time.sleep(3)

        driver.maximize_window()
        print('Maximizing Window')
        time.sleep(3)

        districts = ['Mumbai', 'Akola', 'Dhule']

        for district in districts:

            driver.find_element_by_xpath('//*[@id="search"]').clear()
            print('Clearing The Search Bar')
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="search"]').send_keys(district)
            print('Giving Input in Search Bar --> ', district)
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
            print('Hitting Enter for the District --> ', district)
            time.sleep(3)

            if 'display: block;' == driver.find_element_by_xpath('/html/body/section[3]').get_attribute('style'):

                print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
                container = driver.find_element_by_xpath('/html/body/section[3]/div/div/div/ul').get_attribute("outerHTML")
                print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

                soup = BeautifulSoup(container, features='lxml')
                search_container = soup.find_all("ul", {"class": "address-sub"})
                print('Finding all div in Page Source')

                for data in search_container:

                    try:

                        store_link = data.find('a').get('href')
                        print('store_link --> ', store_link)
                        yield scrapy.Request(store_link, callback=self.parse_items)

                    except Exception as e:
                        print('Exception while getting Page Info --> ', e)
                        pass

                time.sleep(5)
                driver.implicitly_wait(5)

                while True:

                    if 'disabled' not in driver.find_element_by_xpath('//*[@id="pagination"]/li[5]').get_attribute('class'):

                        next_page_class = driver.find_element_by_xpath('//*[@id="pagination"]/li[5]').get_attribute('class')
                        print('next page class --> ', next_page_class)

                        driver.find_element_by_xpath('//*[@id="pagination"]/li[5]').click()
                        print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')

                        container = driver.find_element_by_xpath('/html/body/section[3]/div/div/div/ul').get_attribute("outerHTML")
                        print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

                        soup = BeautifulSoup(container, features='lxml')
                        search_container = soup.find_all("ul", {"class": "address-sub"})
                        print('Finding all div in Page Source')

                        for data in search_container:

                            try:

                                store_link = data.find('a').get('href')
                                print('store_link --> ', store_link)
                                yield scrapy.Request(store_link, callback=self.parse_items)

                            except Exception as e:
                                print('Exception while getting Page Info --> ', e)
                                pass

                        time.sleep(5)
                        driver.implicitly_wait(5)

                    elif 'page-item next disabled' in driver.find_element_by_xpath('//*[@id="pagination"]/li[5]').get_attribute('class'):

                        next_page_class_two = driver.find_element_by_xpath('//*[@id="pagination"]/li[5]').get_attribute('class')
                        print('next_page_class_two --> ', next_page_class_two)
                        break

                    time.sleep(5)
                    driver.implicitly_wait(5)

    def parse_items(self, response):

        print('-------------------------------------')

        items = BridgestonetyresItem()

        ####################
        ####################

        try:
            manufacturer_unique_id = ''
        except Exception as e:
            manufacturer_unique_id = ''
            print('Exception while getting manufacturer_unique_id --> ', e)
            pass
#        print('manufacturer_unique_id -> ', manufacturer_unique_id)
        items['manufacturer_unique_id'] = manufacturer_unique_id
        ####################
        ####################

        try:
            store_name = response.xpath('/html/body/section[3]/div/div/div[1]/h3/text()').extract()
        except Exception as e:
            store_name = ''
            print('Exception while getting store_name --> ', e)
            pass
        print('store_name ->', store_name)
        items['store_name'] = store_name
        ####################
        ####################

        try:
            full_address = response.xpath('/html/body/section[3]/div/div/div[1]/ul/li[1]/text()').extract_first()
        except Exception as e:
            full_address = ''
            print('Exception while getting full_address --> ', e)
            pass
#        print('full_address ->', full_address)
        items['full_address'] = str(full_address).replace('\t', '').replace('\n', '')
        ####################
        ####################

        try:
            email_id = ''
        except Exception as e:
            email_id = ''
            print('Exception while getting email_id --> ', e)
            pass
#        print('email_id ->', email_id)
        items['email_id'] = email_id
        ####################
        ####################

        try:
            phone_number = response.xpath('/html/body/section[3]/div/div/div[1]/ul/li[2]/text()').extract_first()
        except Exception as e:
            phone_number = ''
            print('Exception while getting phone_number --> ', e)
            pass
#        print('phone_number ->', phone_number)
        items['phone_number'] = phone_number
        ####################
        ####################

        try:
            state = ''
        except Exception as e:
            state = ''
            print('Exception while getting state --> ', e)
            pass
#        print('state ->', state)
        items['state'] = state
        ####################
        ####################

        try:
            district = ''
        except Exception as e:
            district = ''
            print('Exception while getting district --> ', e)
            pass
#        print('district ->', district)
        items['district'] = district
        ####################
        ####################

        try:
            pincode = ''
        except Exception as e:
            pincode = ''
            print('Exception while getting pincode --> ', e)
            pass
#        print('pincode --> ', pincode)
        items['pincode'] = pincode
        ####################
        ####################

        try:
            brand = 'BRIDGE STONE'
        except Exception as e:
            brand = ''
            print('Exception while getting brand --> ', e)
            pass
#        print('brand --> ', brand)
        items['brand'] = brand
        ####################
        ####################

        try:
            website = response.request.url
        except Exception as e:
            website = ''
            print('Exception while getting website --> ', e)
            pass
#        print('website --> ', website)
        items['website'] = website
        ####################
        ####################

        try:
            google_maps_direction_url = response.xpath('/html/body/section[3]/div/div/div[1]/ul/li[4]/a/@href').extract_first()
        except Exception as e:
            google_maps_direction_url = ''
            print('Exception while getting google_maps_direction_url --> ', e)
            pass
#        print('google_maps_direction_url --> ', google_maps_direction_url)
        items['google_maps_direction_url'] = google_maps_direction_url
        ####################
        ####################

        try:
            appointment_booking_url = response.xpath('/html/body/section[3]/div/div/div[1]/ul/li[5]/a/@href').extract_first()
        except Exception as e:
            appointment_booking_url = ''
            print('Exception while getting appointment_booking_url --> ', e)
            pass
#        print('appointment_booking_url --> ', appointment_booking_url)
        items['appointment_booking_url'] = appointment_booking_url
        ####################
        ####################

        yield items