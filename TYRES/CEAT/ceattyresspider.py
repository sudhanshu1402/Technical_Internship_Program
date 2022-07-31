from ceattyres.CeattyresItem import CeattyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver', chrome_options=chrome_options)


class CeattyresspiderSpider(scrapy.Spider):
    name = 'ceattyresspider'
    start_urls = ['https://www.ceat.com/tyre-shop.html']

    def parse(self, response, **kwargs):
        items = CeattyresItem()

        postals = ['400059', '400069', '400037',  '110032', '110033',  '144205', '144206', '152116', '152117']

        driver.get('https://www.ceat.com/tyre-shop.html')
        print('LOADING THE MAIN PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')

        driver.find_element_by_xpath('//*[@id="get-callback"]/div/div/div[1]/button').click()
        print('CLOSING POP UPS AND DIALOGUE BOXES')
        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/header/div/div/div[1]/div[2]/ul/li[1]').click()
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        keys = list()
        for post in postals:

            driver.find_element_by_xpath('//*[@id="pinCode"]').clear()
            print('CLEARING THE SEARCH BAR')
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="pinCode"]').send_keys(post)
            print('GIVING INPUT IN THE SEARCH BAR--> ', post)
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="pinCode"]').send_keys(Keys.ENTER)
            print('LOADING THE STORES AROUND --> ', post)
            time.sleep(3)

            listt = driver.find_element_by_xpath('//*[@id="parentNode"]').get_attribute('outerHTML')
            print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')

            soup = BeautifulSoup(listt, 'html.parser')
            print('PARSING IT USING BS4')

            templatenode = soup.find_all("li", {"style": "display: block;"})
            print('FINDING ALL LI IN DEALER LIST')

            for data in templatenode:

                dealer_code = data.find("span", {"class": "icon icon-whatsapp"}).get('data-dealercode')
                print('DEALER CODE --> ', dealer_code)
                if dealer_code not in keys:

                    print('DEALER CODE NOT PRESENT IN THE LIST SO APPENDING --> ', dealer_code)
                    keys.append(dealer_code)
                    print('APPEND DONE NOW EXTRACTING DATA')

                    ####################
                    ####################
                    try:
                        manufacturer_unique_id = data.find("span", {"class": "icon icon-whatsapp"}).get('data-dealercode')
                    except Exception as e:
                        manufacturer_unique_id = ''
                        print('Exception while getting manufacturer_unique_id --> ', e)
                        pass
                    print('manufacturer_unique_id -> ', manufacturer_unique_id)
                    items['manufacturer_unique_id'] = manufacturer_unique_id
                    ####################
                    ####################
                    try:
                        store_name = data.find("div", {"class": "store-name"}).text
                    except Exception as e:
                        store_name = ''
                        print('Exception while getting store_name --> ', e)
                        pass
                    print('store_name ->', store_name)
                    items['store_name'] = store_name
                    ####################
                    ####################
                    try:
                        full_address = data.find("p", {"class": "address"}).text
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
                        phone_number = data.find("span", {"class": "contact-no"}).text
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
                        pincode = post
                    except Exception as e:
                        pincode = ''
                        print('Exception while getting pincode --> ', e)
                        pass
                    print('pincode ->', pincode)
                    items['pincode'] = pincode
                    ####################
                    ####################
                    try:
                        if data.find("span", {"class": "ceat-shoppe-label"}).get('style') == 'display: none;':
                            ceat_shoppe = '0'
                        else:
                            ceat_shoppe = '1'
                    except Exception as e:
                        ceat_shoppe = ''
                        print('Exception while getting ceat_shoppe --> ', e)
                        pass
                    print('ceat_shoppe --> ', ceat_shoppe)
                    items['ceat_shoppe'] = ceat_shoppe
                    ####################
                    ####################
                    try:
                        brand = 'CEAT'
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
                    print('ALREADY EXISTING SO NOT APPENDING --> ', dealer_code)
