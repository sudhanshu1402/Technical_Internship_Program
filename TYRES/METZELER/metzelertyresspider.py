from metzeler.MetzelerItem import MetzelerItem
import time
import scrapy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class MetzelertyresspiderSpider(scrapy.Spider):
    name = 'metzelertyresspider'
    start_urls = ['https://www.metzeler.com/en-in/dealer-locator']

    def parse(self, response, **kwargs):
        items = MetzelerItem()

        driver.get('https://www.metzeler.com/en-in/dealer-locator')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="cp-decline"]').click()
        print('CLOSING POP UPS AND DIALOGUE BOXES')
        time.sleep(3)

        elems = driver.find_elements_by_xpath('//*[@id="goto-details"]')
        print('FINDING ALL GOTO HREF IN DEALER LIST')

        for elem in elems:

            actions = ActionChains(driver)
            actions.move_to_element(elem).perform()
            elem.click()
            print('CLICKING GOTO HREF IN DEALER LIST')
            time.sleep(5)

            ####################
            ####################
            try:
                manufacturer_unique_id = driver.find_element_by_xpath('//*[@id="scheda-rivenditore"]/input[1]').get_attribute('value')
                if manufacturer_unique_id is None:
                    manufacturer_unique_id = ''
                else:
                    manufacturer_unique_id = driver.find_element_by_xpath('//*[@id="scheda-rivenditore"]/input[1]').get_attribute('value')
            except Exception as e:
                manufacturer_unique_id = ''
                print('Exception while getting manufacturer_unique_id --> ', e)
                pass
            print('manufacturer_unique_id -> ', manufacturer_unique_id)
            items['manufacturer_unique_id'] = manufacturer_unique_id
            ####################
            ####################
            try:
                store_name = driver.find_element_by_xpath('//*[@id="scheda-rivenditore"]/input[2]').get_attribute('value')
            except Exception as e:
                store_name = ''
                print('Exception while getting store_name --> ', e)
                pass
            print('store_name ->', store_name)
            items['store_name'] = store_name
            ####################
            ####################
            try:
                full_address = driver.find_element_by_xpath('//*[@id="scheda-rivenditore"]/input[3]').get_attribute('value')
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
                phone_number = driver.find_element_by_xpath('//*[@id="dealer_phone"]').get_attribute('value')
            except Exception as e:
                phone_number = ''
                print('Exception while getting phone_number --> ', e)
                pass
            print('phone_number ->', phone_number)
            items['phone_number'] = phone_number
            ####################
            ####################
            try:
                district = driver.find_element_by_xpath('//*[@id="scheda-rivenditore"]/input[4]').get_attribute('value')
            except Exception as e:
                district = ''
                print('Exception while getting district --> ', e)
                pass
            print('district ->', district)
            items['district'] = district
            ####################
            ####################
            try:
                state = ''
            except Exception as e:
                state = ''
                print('Exception while getting state --> ', e)
                pass
            print('state --> ', state)
            items['state'] = state
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
                brand = 'METZELER'
            except Exception as e:
                brand = ''
                print('Exception while getting brand --> ', e)
                pass
            print('brand --> ', brand)
            items['brand'] = brand
            ####################
            ####################

            driver.find_element_by_xpath('//*[@id="scheda-rivenditore-outer"]/div[1]/a').click()
            print('CLICKING BACK BUTTON')
            time.sleep(5)
            driver.implicitly_wait(5)

            yield items
