from pirellityres.PirellityresItem import PirellityresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class PirellityresspiderSpider(scrapy.Spider):
    name = 'pirellityresspider'
    start_urls = ['https://www.pirelli.com/tyres/en-in/car/find-your-dealer/dealer-locator?city=Mumbai%2C+Maharashtra%2C+India']

    def parse(self, response, **kwargs):

        postals = ['Mumbai', 'Akola', 'Dhule', 'Delhi', 'Surat', 'Bangalore']

        items = PirellityresItem()

        driver.get('https://www.pirelli.com/tyres/en-in/car/find-your-dealer/dealer-locator?city=Mumbai%2C+Maharashtra%2C+India')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="cp-accept"]').click()
        print('CLOSING ALL POP UPS AND DIALOGUE BOXES')
        time.sleep(3)

        keys = list()

        for post in postals:

            driver.find_element_by_xpath('//*[@id="locatorField"]').clear()
            print('CLEARING THE SEARCH BAR')
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="locatorField"]').send_keys(post)
            print('GIVING INPUT IN THE SEARCH BAR--> ', post)
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="locatorField"]').send_keys(Keys.ARROW_DOWN)
            print('SELECTING THE FIRST RECOMMENDED OPTION --> ', post)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="locatorField"]').send_keys(Keys.ENTER)
            print('LOADING THE STORES AROUND --> ', post)
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="locatorButton"]/i').click()
            print('CLICKING SEARCH BUTTON')
            time.sleep(3)

            print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
            listt = driver.find_element_by_xpath('//*[@id="results-panel-box"]').get_attribute("outerHTML")
            print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

            soup = BeautifulSoup(listt, features='lxml')
            templatenode = soup.find_all("li", {"dealer-thumbnail": "dealer"})
            print('FINDING ALL LI IN DEALER LIST')

            for div in templatenode:

                dealer_code = div['data-dealerid']
                print('DEALER CODE --> ', dealer_code)

                if dealer_code not in keys:

                    print('DEALER CODE NOT EXISTING SO APPENDING --> ', dealer_code)
                    keys.append(dealer_code)
                    print('APPENDING DONE NOW EXTRACTING')

                    ####################
                    ####################
                    try:
                        manufacturer_unique_id = div['data-dealerid']
                    except Exception as e:
                        manufacturer_unique_id = ''
                        print('Exception while getting manufacturer_unique_id --> ', e)
                        pass
                    print('manufacturer_unique_id -> ', manufacturer_unique_id)
                    items['manufacturer_unique_id'] = manufacturer_unique_id
                    ####################
                    ####################
                    try:
                        store_name = div.find("div", {"class": "dlHeadline"}).find('strong').text
                    except Exception as e:
                        store_name = ''
                        print('Exception while getting store_name --> ', e)
                        pass
                    print('store_name ->', store_name)
                    items['store_name'] = store_name
                    ####################
                    ####################
                    try:
                        full_address = div.find("span", {"class": "dlAddress"}).text
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
                        phone_number = ''
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
                    print('district ->', state)
                    items['state'] = state
                    ####################
                    ####################
                    try:
                        district = post
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
                        brand = 'PIRELLI'
                    except Exception as e:
                        brand = ''
                        print('Exception while getting brand --> ', e)
                        pass
                    print('brand --> ', brand)
                    items['brand'] = brand
                    ####################
                    ####################
                    yield items

                else:
                    print('DEALER ALREADY EXISTING SO NOT EXTRACTING --> ', dealer_code)
