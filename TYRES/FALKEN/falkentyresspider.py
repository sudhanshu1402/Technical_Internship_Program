from falkentyres.FalkentyresItem import FalkentyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class FalkentyresspiderSpider(scrapy.Spider):
    name = 'falkentyresspider'
    start_urls = ['http://falkentyre.in/find-a-store']

    def parse(self, response, **kwargs):
        items = FalkentyresItem()

        driver.get('http://falkentyre.in/find-a-store')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        print('CLICKING SELECT STATE')
        driver.find_element_by_xpath('//*[@id="select_State"]').click()
        time.sleep(3)

        print('SELECTING OPTION FROM DROP DOWN')
        driver.find_element_by_xpath('//*[@id="select_State"]/option[2]').click()
        time.sleep(3)

        print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
        stores = driver.find_element_by_xpath('//*[@id="lst_Stores"]').get_attribute('outerHTML')
        print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

        soup = BeautifulSoup(stores, features='lxml')
        boxes = soup.find_all('address')
        print('FINDING ALL DIVS IN DEALER LIST')

        for data in boxes:
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
                store_name = data.find('h3').text
            except Exception as e:
                store_name = ''
                print('Exception while getting store_name --> ', e)
                pass
            print('store_name ->', store_name)
            items['store_name'] = store_name
            ####################
            ####################
            try:
                full_address = data.find('p').text
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
                phone_number = data.p.next_sibling.text
            except Exception as e:
                phone_number = ''
                print('Exception while getting phone_number --> ', e)
                pass
            print('phone_number ->', phone_number)
            items['phone_number'] = phone_number
            ####################
            ####################
            try:
                state = ''
            except Exception as e:
                state = ''
                print('Exception while getting state --> ', e)
                pass
            print('state ->', state)
            items['state'] = state
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
                brand = 'FALKENTYRES'
            except Exception as e:
                brand = ''
                print('Exception while getting brand --> ', e)
                pass
            print('brand --> ', brand)
            items['brand'] = brand
            ####################
            ####################
            yield items

        print('CLICKING SELECT STATE')
        driver.find_element_by_xpath('//*[@id="select_State"]').click()
        time.sleep(3)

        print('SELECTING OPTION FROM DROP DOWN')
        driver.find_element_by_xpath('//*[@id="select_State"]/option[3]').click()
        time.sleep(3)

        print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
        stores = driver.find_element_by_xpath('//*[@id="lst_Stores"]').get_attribute('outerHTML')
        print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

        soup = BeautifulSoup(stores, features='lxml')
        boxes = soup.find_all('address')
        print('FINDING ALL DIVS IN DEALER LIST')

        for data in boxes:
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
                store_name = data.find('h3').text
            except Exception as e:
                store_name = ''
                print('Exception while getting store_name --> ', e)
                pass
            print('store_name ->', store_name)
            items['store_name'] = store_name
            ####################
            ####################
            try:
                full_address = data.find('p').text
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
                phone_number = data.p.next_sibling.text
            except Exception as e:
                phone_number = ''
                print('Exception while getting phone_number --> ', e)
                pass
            print('phone_number ->', phone_number)
            items['phone_number'] = phone_number
            ####################
            ####################
            try:
                state = ''
            except Exception as e:
                state = ''
                print('Exception while getting state --> ', e)
                pass
            print('state ->', state)
            items['state'] = state
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
                brand = 'FALKENTYRES'
            except Exception as e:
                brand = ''
                print('Exception while getting brand --> ', e)
                pass
            print('brand --> ', brand)
            items['brand'] = brand
            ####################
            ####################
            yield items

        print('CLICKING SELECT STATE')
        driver.find_element_by_xpath('//*[@id="select_State"]').click()
        time.sleep(3)

        print('SELECTING OPTION FROM DROP DOWN')
        driver.find_element_by_xpath('//*[@id="select_State"]/option[4]').click()
        time.sleep(3)

        print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
        stores = driver.find_element_by_xpath('//*[@id="lst_Stores"]').get_attribute('outerHTML')
        print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

        soup = BeautifulSoup(stores, features='lxml')
        boxes = soup.find_all('address')
        print('FINDING ALL DIVS IN DEALER LIST')

        for data in boxes:
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
                store_name = data.find('h3').text
            except Exception as e:
                store_name = ''
                print('Exception while getting store_name --> ', e)
                pass
            print('store_name ->', store_name)
            items['store_name'] = store_name
            ####################
            ####################
            try:
                full_address = data.find('p').text
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
                phone_number = data.p.next_sibling.text
            except Exception as e:
                phone_number = ''
                print('Exception while getting phone_number --> ', e)
                pass
            print('phone_number ->', phone_number)
            items['phone_number'] = phone_number
            ####################
            ####################
            try:
                state = ''
            except Exception as e:
                state = ''
                print('Exception while getting state --> ', e)
                pass
            print('state ->', state)
            items['state'] = state
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
                brand = 'FALKENTYRES'
            except Exception as e:
                brand = ''
                print('Exception while getting brand --> ', e)
                pass
            print('brand --> ', brand)
            items['brand'] = brand
            ####################
            ####################
            yield items
