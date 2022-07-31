from birlatyres.BirlatyresItem import BirlatyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class BirlatyresspiderSpider(scrapy.Spider):
    name = 'birlatyresspider'
    start_urls = ['https://www.birla-tyre.in/dealer-network/']

    def parse(self, response, **kwargs):

        postals = ['Mumbai', 'Akola', 'Dhule', 'Delhi', 'Surat', 'Bangalore']

        items = BirlatyresItem()

        driver.get('https://www.birla-tyre.in/dealer-network/')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[2]/a').click()
        print('CLICKING ON THE SEARCH WITH STATE OR CITY')
        time.sleep(3)

        for post in postals:

            driver.find_element_by_xpath('//*[@id="search"]').clear()
            print('CLEARING THE SEARCH BAR')
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="search"]').send_keys(post)
            print('GIVING INPUT IN THE SEARCH BAR--> ', post)
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
            print('LOADING THE STORES AROUND --> ', post)
            time.sleep(3)

            print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
            results = driver.find_element_by_xpath('//*[@id="home-result"]').get_attribute("outerHTML")
            print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

            soup = BeautifulSoup(results, features='lxml')
            search_container = soup.find_all('div', {'class': 'col-md-6 result'})
            print('FINDING ALL DIVS IN DEALER LIST')

            for div in search_container:

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
                    store_name = div.find('strong').text
                except Exception as e:
                    store_name = ''
                    print('Exception while getting store_name --> ', e)
                    pass
                print('store_name ->', store_name)
                items['store_name'] = store_name
                ####################
                ####################
                try:
                    address_line_one = div.br.next_sibling
                except Exception as e:
                    address_line_one = ''
                    print('Exception while getting address_line_one --> ', e)
                    pass
                print('address_line_one ->', address_line_one)
                items['address_line_one'] = address_line_one
                ####################
                ####################
                try:
                    address_line_two = div.br.next_sibling.next_sibling.next_sibling
                except Exception as e:
                    address_line_two = ''
                    print('Exception while getting address_line_two --> ', e)
                    pass
                print('full_aaddress_line_twoddress ->', address_line_two)
                items['address_line_two'] = address_line_two
                ####################
                ####################
                try:
                    full_address = address_line_one + address_line_two
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
                    pincode = div.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('\t', '').replace('\n', '')
                    if 'Phone' in pincode:
                        pincode = div.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('\t', '').replace('\n', '')
                except Exception as e:
                    pincode = ''
                    print('Exception while getting pincode --> ', e)
                    pass
                print('pincode --> ', pincode)
                items['pincode'] = pincode
                ####################
                ####################
                try:
                    phone_number = div.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('\t', '').replace('\n', '').replace('Phone :', '')
                    if phone_number == pincode:
                        phone_number = div.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('\t', '').replace('\n', '').replace('Phone :', '')
                except Exception as e:
                    phone_number = ''
                    print('Exception while getting phone_number --> ', e)
                    pass
                print('phone_number ->', phone_number)
                items['phone_number'] = phone_number
                ####################
                ####################
                try:
                    state = div.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('\t', '').replace('\n', '')
                    if pincode in state:
                        state = div.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('\t', '').replace('\n', '')
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
                    brand = 'BIRLA'
                except Exception as e:
                    brand = ''
                    print('Exception while getting brand --> ', e)
                    pass
                print('brand --> ', brand)
                items['brand'] = brand
                ####################
                ####################
                yield items
