from michelinbiketyres.MichelinbiketyresItem import MichelinbiketyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')

class MichelinbiketyresspiderSpider(scrapy.Spider):
    name = 'michelinbiketyresspider'
    start_urls = ['https://www.michelin.in/motorbike/dealer-locator/Andheri%20East,%20Mumbai,%20Maharashtra%20400059,%20India?']


    def parse(self, response, **kwargs):
        items = MichelinbiketyresItem()
        keys = list()

        postals = ['Mumbai', 'Akola', 'Dhule', 'Delhi', 'Surat', 'Bangalore']

        driver.get('https://www.michelin.in/auto/dealer-locator/400059+IN')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(5)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(5)

        driver.find_element_by_xpath('/html/body/div[2]/div/a[2]').click()
        print('CLOSING POP UPS AND DIALOGUE BOXES')

        for post in postals:

            driver.find_element_by_xpath('//*[@id="b2c-dl-search__input"]').clear()
            print('CLEARING THE SEARCH BAR')
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="b2c-dl-search__input"]').send_keys(post)
            print('GIVING INPUT IN THE SEARCH BAR--> ', post)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="b2c-dl-search__input"]').send_keys(Keys.ARROW_DOWN)
            print('SELECTING THE FIRST RECOMMENDED OPTION --> ', post)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="b2c-dl-search__input"]').send_keys(Keys.ENTER)
            print('LOADING THE STORES AROUND --> ', post)
            time.sleep(5)

            while True:

                time.sleep(5)
                if 'display: none;' in driver.find_element_by_xpath('//*[@id="b2c-dl-result-load-more"]').get_attribute('style'):
                    print('NOT INTRACTABLE')
                    break
                else:
                    print('SCROLLING TILL THE END OF RESULTS')
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="b2c-dl-result-load-more"]/div[2]/span[2]').click()

            print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
            result_list = driver.find_element_by_xpath('//*[@id="b2c-dl-result-list"]').get_attribute('outerHTML')
            print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

            soup = BeautifulSoup(result_list, features='lxml')
            blocks = soup.find_all('li', {'class': 'b2c-dl-result-card'})
            print('FINDING ALL LI IN DEALER LIST')

            for li in blocks:

                dealer_code = li['data-dealer-id']
                print('DEALER CODE --> ', dealer_code)

                if dealer_code not in keys:

                    print('DEALER CODE NOT PRESENT IN THE LIST SO APPENDING --> ', dealer_code)
                    keys.append(dealer_code)
                    print('APPEND DONE NOW EXTRACTING DATA')

                    ####################
                    ####################
                    try:
                        manufacturer_unique_id = li['data-dealer-id']
                    except Exception as e:
                        manufacturer_unique_id = ''
                        print('Exception while getting manufacturer_unique_id --> ', e)
                        pass
                    print('manufacturer_unique_id -> ', manufacturer_unique_id)
                    items['manufacturer_unique_id'] = manufacturer_unique_id
                    ####################
                    ####################
                    try:
                        store_name = li.find('div', {'class': 'b2c-dl-result-card-title__dealer-name'}).text
                    except Exception as e:
                        store_name = ''
                        print('Exception while getting store_name --> ', e)
                        pass
                    print('store_name ->', store_name)
                    items['store_name'] = store_name
                    ####################
                    ####################
                    try:
                        full_address = li.find('div', {'class': 'b2c-dl-result-card-infos__dealer-address'}).text
                    except Exception as e:
                        full_address = ''
                        print('Exception while getting full_address --> ', e)
                        pass
                    print('full_address ->', full_address)
                    items['full_address'] = str(full_address).replace('\n', '')
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
                        if li.find('div', {'class': 'b2c-dl-result-card-infos__dealer-phone'}) is None:
                            phone_number = ''
                        else:
                            phone_number = li.find('div', {'class': 'b2c-dl-result-card-infos__dealer-phone'}).text
                    except Exception as e:
                        phone_number = ''
                        print('Exception while getting phone_number --> ', e)
                        pass
                    print('phone_number ->', phone_number)
                    items['phone_number'] = str(phone_number).replace('\n', '')
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
                        if "b2c-dl-result-card--recommended" not in li['class']:
                            michelin_certified_centre = '0'
                        else:
                            michelin_certified_centre = '1'
                    except Exception as e:
                        michelin_certified_centre = ''
                        print('Exception while getting michelin_certified_centre --> ', e)
                        pass
                    print('michelin_certified_centre --> ', michelin_certified_centre)
                    items['michelin_certified_centre'] = michelin_certified_centre
                    ####################
                    ####################
                    try:
                        brand = 'MICHELIN'
                    except Exception as e:
                        brand = ''
                        print('Exception while getting brand --> ', e)
                        pass
                    print('brand --> ', brand)
                    items['brand'] = brand
                    ####################
                    ####################
                    try:
                        google_maps_direction_url = li.find('a', {'data-analytics': 'DL_CLICK_DEALER_DIRECTION'}).get('href')
                    except Exception as e:
                        google_maps_direction_url = ''
                        print('Exception while getting google_maps_direction_url  --> ', e)
                        pass
                    print('google_maps_direction_url  --> ', google_maps_direction_url)
                    items['google_maps_direction_url'] = google_maps_direction_url
                    ####################
                    ####################
                    try:
                        if li.find('a', {'data-analytics': 'DL_CLICK_DEALER_WEBSITE'}) is not None:
                            website = li.find('a', {'data-analytics': 'DL_CLICK_DEALER_WEBSITE'}).get('href')
                        else:
                            website = ''
                    except Exception as e:
                        website = ''
                        print('Exception while getting website --> ', e)
                        pass
                    print('website --> ', website)
                    items['website'] = website
                    ####################
                    ####################
                    try:
                        if li.find('a', {'data-analytics': 'DL_CLICK_DEALER_WEBSITE'}) is not None:
                            appointment_booking_url = li.find('a', {'data-analytics': 'DL_CLICK_DEALER_WEBSITE_APPOINTMENT'}).get('href')
                        else:
                            appointment_booking_url = ''
                    except Exception as e:
                        appointment_booking_url = ''
                        print('Exception while getting appointment_booking_url  --> ', e)
                        pass
                    print('appointment_booking_url  --> ', appointment_booking_url)
                    items['appointment_booking_url'] = appointment_booking_url
                    ####################
                    ####################
                    try:
                        brand_website_store_url = 'https://www.michelin.in' + li.find('div', {'class': 'b2c-dl-result-card-infos__dealer-details'}).find('a').get('href')
                    except Exception as e:
                        brand_website_store_url = ''
                        print('Exception while getting brand_website_store_url  --> ', e)
                        pass
                    print('brand_website_store_url  --> ', brand_website_store_url)
                    items['brand_website_store_url'] = brand_website_store_url
                    ####################
                    ####################
                    yield items

                else:
                    print('ALREADY EXISTING SO NOT EXTRACTING --> ', dealer_code)
