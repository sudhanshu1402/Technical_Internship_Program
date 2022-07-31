from yokohamatyres.YokohamatyresItem import YokohamatyresItem
import time
import scrapy
import re
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class YokohamatyresspiderSpider(scrapy.Spider):
    name = 'yokohamatyresspider'
    start_urls = ['https://www.yokohama-india.com/storelocator']

    def parse(self, response, **kwargs):
        items = YokohamatyresItem()
        keys = list()

        driver.get('https://www.yokohama-india.com/storelocator')
        print('Getting To Store Locator Page')
        time.sleep(3)

        driver.maximize_window()
        print('Maximizing Window')
        time.sleep(2)

        select_state = driver.find_element_by_id('state')
        options = select_state.find_elements_by_tag_name('option')
        for option_state in options:
            option_state.click()
            time.sleep(2)

            select_city = driver.find_element_by_id('city')
            options = select_city.find_elements_by_tag_name('option')
            for option_city in options:
                option_city.click()
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="distance"]/option[7]').click()
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="form-searchby"]/div[4]/button').click()

                boxes = driver.find_elements_by_name('results_entry')
                for box in boxes:
                    box.location_once_scrolled_into_view
                    time.sleep(2)
                    box.click()

                    store_results = driver.find_element_by_xpath('//*[@id="map"]/div/div/div[2]/div[3]/div/div[4]').get_attribute('outerHTML')
                    store_results_soup = BeautifulSoup(store_results, features='lxml')

                    try:
                        check = store_results_soup.find('div', {'id': 'bodyContent'}).find('p').text
                    except Exception as e:
                        check = ''
                        print('Exception while getting store_results_soup --> ', e)
                        pass

                    if check not in keys:
                        keys.append(check)
                        print('Append Done Now Extracting')

                        ########################################
                        ########################################
                        print('--------------------------------------------')
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
                            store_name = store_results_soup.find('div', {'class': 'gm-style-iw-d'}).find('h3').text
                        except Exception as e:
                            store_name = ''
                            print('Exception while getting store_name --> ', e)
                            pass
                        print('store_name ->', store_name)
                        items['store_name'] = store_name
                        ####################
                        ####################
                        try:
                            full_address = store_results_soup.find('div', {'id': 'bodyContent'}).find('p').text
                        except Exception as e:
                            full_address = ''
                            print('Exception while getting full_address --> ', e)
                            pass
                        print('full_address -> ', full_address)
                        items['full_address'] = full_address
                        ####################
                        ####################
                        try:
                            if 'Email' in store_results_soup.find('div', {'id': 'bodyContent'}).find('p').find_next('p').find_next('p').find_next('p').find_next('p').text:
                                email_id = store_results_soup.find('div', {'id': 'bodyContent'}).find('p').find_next('p').find_next('p').find_next('p').find_next('p').text
                            elif 'Email' in store_results_soup.find('div', {'id': 'bodyContent'}).find('p').find_next('p').find_next('p').find_next('p').text:
                                email_id = ''
                            else:
                                email_id = ''
                        except Exception as e:
                            email_id = ''
                            print('Exception while getting email_id --> ', e)
                            pass
                        print('email_id -> ', email_id)
                        items['email_id'] = email_id
                        ####################
                        ####################
                        try:
                            if 'Phone' in store_results_soup.find('div', {'id': 'bodyContent'}).find('p').find_next('p').find_next('p').find_next('p').text:
                                phone_number = store_results_soup.find('div', {'id': 'bodyContent'}).find('p').find_next('p').find_next('p').find_next('p').text
                            else:
                                phone_number = ''
                        except Exception as e:
                            phone_number = ''
                            print('Exception while getting phone_number --> ', e)
                            pass
                        print('phone_number -> ', phone_number)
                        items['phone_number'] = phone_number
                        ####################
                        ####################
                        try:
                            state_check = store_results_soup.find('div', {'id': 'bodyContent'}).find('br').next_sibling
                            state = state_check.split(',')[0]
                        except Exception as e:
                            state = ''
                            print('Exception while getting state --> ', e)
                            pass
                        print('state -> ', state)
                        items['state'] = state
                        ####################
                        ####################

                        try:
                            pincode_check = store_results_soup.find('div', {'id': 'bodyContent'}).find('br').next_sibling
                            pincode = re.sub('\D', '', pincode_check)
                        except Exception as e:
                            pincode = ''
                            print('Exception while getting pincode --> ', e)
                            pass
                        print('pincode -> ', pincode)
                        items['pincode'] = pincode
                        ####################
                        ####################
                        try:
                            district_check = store_results_soup.find('div', {'id': 'bodyContent'}).find('br').next_sibling
                            district = re.sub('\d', '', district_check).replace(state, '').replace('-', '').replace(' ', '').replace(',', '')
                        except Exception as e:
                            district = ''
                            print('Exception while getting district --> ', e)
                            pass
                        print('district -> ', district)
                        items['district'] = district
                        ####################
                        ####################
                        try:
                            if store_results_soup.find('span', {'class': 'ycn_bg'}) is not None:
                                yokohama_zone = '1'
                            else:
                                yokohama_zone = '0'
                        except Exception as e:
                            yokohama_zone = '0'
                            print('Exception while getting yokohama_zone --> ', e)
                            pass
                        print('yokohama_zone -> ', yokohama_zone)
                        items['yokohama_zone'] = yokohama_zone
                        ####################
                        ####################
                        try:
                            brand = 'Yokohama'
                        except Exception as e:
                            brand = ''
                            print('Exception while getting brand --> ', e)
                            pass
                        print('brand -> ', brand)
                        items['brand'] = brand
                        ####################
                        ####################
                        try:
                            google_maps_direction_url = store_results_soup.find('div', {'id': 'bodyContent'}).find('p').next_sibling.get('href')
                        except Exception as e:
                            google_maps_direction_url = ''
                            print('Exception while getting google_maps_direction_url --> ', e)
                            pass
                        print('google_maps_direction_url -> ', google_maps_direction_url)
                        items['google_maps_direction_url'] = google_maps_direction_url
                        ####################
                        ####################
                        try:
                            if 'Mr' in store_results_soup.find('div', {'id': 'bodyContent'}).find_next('p').find_next('p').find_next('p'):
                                dealer_name = store_results_soup.find('div', {'id': 'bodyContent'}).find_next('p').find_next('p').find_next('p').text
                            else:
                                dealer_name = ''
                        except Exception as e:
                            dealer_name = ''
                            print('Exception while getting dealer_name --> ', e)
                            pass
                        print('dealer_name -> ', dealer_name)
                        items['dealer_name'] = dealer_name
                        ####################
                        ###################
                        yield items

                    else:
                        print('ALREADY EXISTING SO NOT APPENDING --> ', check)
