from maxxistyres.MaxxistyresItem import MaxxistyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class MaxxistyresspiderSpider(scrapy.Spider):
    name = 'maxxistyresspider'
    start_urls = ['https://www.maxxistyres.in/dealer/locator']

    def parse(self, response, **kwargs):
        items = MaxxistyresItem()

        driver.get('https://www.maxxistyres.in/dealer/locator')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(5)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
        dealers_list = driver.find_element_by_xpath('//*[@id="dealers-list"]').get_attribute("outerHTML")
        print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

        soup = BeautifulSoup(dealers_list, features='lxml')
        search_container = soup.find_all('li', {'class': 'item mx-4'})
        print('FINDING ALL LI IN DEALER LIST')

        for div in search_container:
            ####################
            ####################
            try:
                manufacturer_unique_id = div['value']
            except Exception as e:
                manufacturer_unique_id = ''
                print('Exception while getting manufacturer_unique_id --> ', e)
                pass
            print('manufacturer_unique_id -> ', manufacturer_unique_id)
            items['manufacturer_unique_id'] = manufacturer_unique_id
            ####################
            ####################
            try:
                store_name = div.find('h5').text
            except Exception as e:
                store_name = ''
                print('Exception while getting store_name --> ', e)
                pass
            print('store_name ->', store_name)
            items['store_name'] = store_name
            ####################
            ####################
            try:
                full_address = div.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.replace('Address:', '')
            except Exception as e:
                full_address = ''
                print('Exception while getting full_address --> ', e)
                pass
            print('full_address ->', full_address)
            items['full_address'] = full_address
            ####################
            ####################
            try:
                email_id = ''
            except Exception as e:
                email_id = ''
                print('Exception while getting email_id --> ', e)
                pass
            print('email_id ->', email_id)
            items['email_id'] = email_id
            ####################
            ####################
            try:
                phone_number = div.p.next_sibling.next_sibling.next_sibling.text.replace('Mobile:', '')
            except Exception as e:
                phone_number = ''
                print('Exception while getting phone_number --> ', e)
                pass
            print('phone_number ->', phone_number)
            items['phone_number'] = phone_number
            ####################
            ####################
            try:
                district_demo = div.find('strong').text
                a_string = district_demo
                split_string = a_string.split(",", 1)
                district = split_string[0]
            except Exception as e:
                district = ''
                print('Exception while getting district --> ', e)
                pass
            print('district ->', district)
            items['district'] = district
            ####################
            ####################
            try:
                state = div.find('strong').text.replace(district, '').replace(', ', '')
            except Exception as e:
                state = ''
                print('Exception while getting state --> ', e)
                pass
            print('state --> ', state)
            items['state'] = state
            ####################
            ####################
            try:
                pincode = div.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.replace('Pincode -', '')
            except Exception as e:
                pincode = ''
                print('Exception while getting pincode --> ', e)
                pass
            print('pincode --> ', pincode)
            items['pincode'] = pincode
            ####################
            ####################
            try:
                brand = 'MAXXIS'
            except Exception as e:
                brand = ''
                print('Exception while getting brand --> ', e)
                pass
            print('brand --> ', brand)
            items['brand'] = brand
            ####################
            ####################
            try:
                dealer_name = div.p.next_sibling.text.replace('Contact:', '')
            except Exception as e:
                dealer_name = ''
                print('Exception while getting dealer_name --> ', e)
                pass
            print('dealer_name --> ', dealer_name)
            items['dealer_name'] = dealer_name
            ####################
            ####################
            yield items
