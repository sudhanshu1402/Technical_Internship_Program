from firestonetyre.FirestonetyreItem import FirestonetyreItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class FirestonetyrespiderSpider(scrapy.Spider):
    name = 'firestonetyrespider'

    start_urls = ['https://www.firestonetyre.co.in/our-stores.php']

    def parse(self, response, **kwargs):
        keys = list()
        items = FirestonetyreItem()

        driver.get('https://www.firestonetyre.co.in/our-stores.php')
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

                driver.find_element_by_xpath('//*[@id="dealerlocator"]/div[4]').click()
                time.sleep(2)

                ########################################
                dealerloc = driver.find_element_by_xpath('//*[@id="dealerloc"]').get_attribute('outerHTML')
                dealerloc_soup = BeautifulSoup(dealerloc, features='lxml')
                ########################################
                try:
                    tr = dealerloc_soup.find('tr')
                    if tr is not None:
                        if tr != '<tr><td colspan="4">No Dealer Found! </td></tr>':
                            try:
                                store_name_check = dealerloc_soup.find('td').text
                                if 'Found' not in store_name_check:
                                    full_address_check = dealerloc_soup.find('td').next_sibling.next_sibling.text
                                    if full_address_check not in keys:
                                        keys.append(full_address_check)

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
                                            store_name = dealerloc_soup.find('td').text
                                        except Exception as e:
                                            store_name = ''
                                            print('Exception while getting store_name --> ', e)
                                            pass
                                        print('store_name ->', store_name)
                                        items['store_name'] = store_name
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
                                            all_number = dealerloc_soup.find('div', {'class': 'show-info'}).text
                                        except Exception as e:
                                            all_number = ''
                                            print('Exception while getting all_number --> ', e)
                                            pass
                                        print('all_number --> ', all_number)
                                        ################
                                        ################
                                        try:
                                            phone_number = dealerloc_soup.find('div', {'class': 'show-info'}).find('br').next_sibling
                                        except Exception as e:
                                            phone_number = ''
                                            print('Exception while getting phone_number --> ', e)
                                            pass
                                        print('phone_number ->', phone_number)
                                        items['phone_number'] = phone_number
                                        ####################
                                        ####################
                                        try:
                                            tel_number = all_number.replace(phone_number, '')
                                        except Exception as e:
                                            tel_number = ''
                                            print('Exception while getting tel_number --> ', e)
                                            pass
                                        print('tel_number --> ', tel_number)
                                        items['tel_number'] = str(tel_number).replace('Tel. No.:', '').replace('NA', '')
                                        ################
                                        ################
                                        try:
                                            full_address = dealerloc_soup.find('td').next_sibling.next_sibling.text.replace(all_number, '')
                                        except Exception as e:
                                            full_address = ''
                                            print('Exception while getting full_address --> ', e)
                                            pass
                                        print('full_address ->', full_address)
                                        items['full_address'] = full_address
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
                                            district = dealerloc_soup.find('td', {'class': 'dis-info'}).text
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
                                            brand = 'FIRE STONE'
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
                                        print('ALREADY EXISTING SO NOT EXTRACTING --> ', full_address_check)

                            except Exception as e:
                                print('Exception while getting store_name --> ', e)
                                pass

                except Exception as e:
                    print('No Data Found', e)

                ########################################
                dealerlocfs100 = driver.find_element_by_xpath('//*[@id="dealerlocfs100"]').get_attribute('outerHTML')
                dealerlocfs100_soup = BeautifulSoup(dealerlocfs100, features='lxml')
                ########################################
                try:
                    tr = dealerlocfs100_soup.find('tr')
                    if tr is not None:
                        if tr != '<tr><td colspan="4">No Dealer Found! </td></tr>':
                            try:
                                store_name_check = dealerlocfs100_soup.find('td').text
                                if 'Found' not in store_name_check:
                                    full_address_check = dealerlocfs100_soup.find('td').next_sibling.next_sibling.text
                                    if full_address_check not in keys:
                                        keys.append(full_address_check)

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
                                            store_name = dealerlocfs100_soup.find('td').text
                                        except Exception as e:
                                            store_name = ''
                                            print('Exception while getting store_name --> ', e)
                                            pass
                                        print('store_name ->', store_name)
                                        items['store_name'] = store_name
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
                                            all_number = dealerlocfs100_soup.find('div', {'class': 'show-info'}).text
                                        except Exception as e:
                                            all_number = ''
                                            print('Exception while getting all_number --> ', e)
                                            pass
                                        print('all_number --> ', all_number)
                                        ################
                                        ################
                                        try:
                                            phone_number = dealerlocfs100_soup.find('div', {'class': 'show-info'}).find('br').next_sibling
                                        except Exception as e:
                                            phone_number = ''
                                            print('Exception while getting phone_number --> ', e)
                                            pass
                                        print('phone_number ->', phone_number)
                                        items['phone_number'] = phone_number
                                        ####################
                                        ####################
                                        try:
                                            tel_number = all_number.replace(phone_number, '')
                                        except Exception as e:
                                            tel_number = ''
                                            print('Exception while getting tel_number --> ', e)
                                            pass
                                        print('tel_number --> ', tel_number)
                                        items['tel_number'] = str(tel_number).replace('Tel. No.:', '').replace('NA', '')
                                        ################
                                        ################
                                        try:
                                            full_address = dealerlocfs100_soup.find('td').next_sibling.next_sibling.text.replace(all_number, '')
                                        except Exception as e:
                                            full_address = ''
                                            print('Exception while getting full_address --> ', e)
                                            pass
                                        print('full_address ->', full_address)
                                        items['full_address'] = full_address
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
                                            district = dealerlocfs100_soup.find('td', {'class': 'dis-info'}).text
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
                                            brand = 'FIRE STONE'
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
                                        print('ALREADY EXISTING SO NOT EXTRACTING --> ', full_address_check)

                            except Exception as e:
                                print('Exception while getting store_name --> ', e)
                                pass

                except Exception as e:
                    print('No Data Found', e)
                ########################################
                dealerloc_bridge = driver.find_element_by_xpath('//*[@id="dealerloc_bridge"]').get_attribute('outerHTML')
                dealerloc_bridge_soup = BeautifulSoup(dealerloc_bridge, features='lxml')
                ########################################
                try:
                    tr = dealerloc_bridge_soup.find('tr')
                    if tr is not None:
                        if tr != '<tr><td colspan="4">No Dealer Found! </td></tr>':
                            try:
                                store_name_check = dealerloc_bridge_soup.find('td').text
                                if 'Found' not in store_name_check:
                                    full_address_check = dealerloc_bridge_soup.find('td').next_sibling.next_sibling.text
                                    if full_address_check not in keys:
                                        keys.append(full_address_check)

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
                                            store_name = dealerloc_bridge_soup.find('td').text
                                        except Exception as e:
                                            store_name = ''
                                            print('Exception while getting store_name --> ', e)
                                            pass
                                        print('store_name ->', store_name)
                                        items['store_name'] = store_name
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
                                            all_number = dealerloc_bridge_soup.find('div', {'class': 'show-info'}).text
                                        except Exception as e:
                                            all_number = ''
                                            print('Exception while getting all_number --> ', e)
                                            pass
                                        print('all_number --> ', all_number)
                                        ################
                                        ################
                                        try:
                                            phone_number = dealerloc_bridge_soup.find('div', {'class': 'show-info'}).find('br').next_sibling
                                        except Exception as e:
                                            phone_number = ''
                                            print('Exception while getting phone_number --> ', e)
                                            pass
                                        print('phone_number ->', phone_number)
                                        items['phone_number'] = phone_number
                                        ####################
                                        ####################
                                        try:
                                            tel_number = all_number.replace(phone_number, '')
                                        except Exception as e:
                                            tel_number = ''
                                            print('Exception while getting tel_number --> ', e)
                                            pass
                                        print('tel_number --> ', tel_number)
                                        items['tel_number'] = str(tel_number).replace('Tel. No.:', '').replace('NA', '')
                                        ################
                                        ################
                                        try:
                                            full_address = dealerloc_bridge_soup.find('td').next_sibling.next_sibling.text.replace(all_number, '')
                                        except Exception as e:
                                            full_address = ''
                                            print('Exception while getting full_address --> ', e)
                                            pass
                                        print('full_address ->', full_address)
                                        items['full_address'] = full_address
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
                                            district = dealerloc_bridge_soup.find('td', {'class': 'dis-info'}).text
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
                                            brand = 'FIRE STONE'
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
                                        print('ALREADY EXISTING SO NOT EXTRACTING --> ', full_address_check)

                            except Exception as e:
                                print('Exception while getting store_name --> ', e)
                                pass

                except Exception as e:
                    print('No Data Found', e)
