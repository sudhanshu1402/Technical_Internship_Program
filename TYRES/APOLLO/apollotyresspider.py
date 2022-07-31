from apollotyres.ApollotyresItem import ApollotyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class ApollotyresspiderSpider(scrapy.Spider):
    name = 'apollotyresspider'
    start_urls = ['https://www.apollotyres.com/en-in/car-suv-van/dealer-finder/find-a-dealer/']

    def parse(self, response, **kwargs):

        postals = ['Mumbai', 'Akola', 'Dhule', 'Delhi', 'Surat', 'Bangalore']

        items = ApollotyresItem()

        driver.get('https://www.apollotyres.com/en-in/car-suv-van/dealer-finder/find-a-dealer/')
        print('LOADING THE STORE LOCATOR PAGE')
        time.sleep(3)

        driver.maximize_window()
        print('MAXIMIZING WINDOW')
        time.sleep(3)

        keys = list()
        for post in postals:

            driver.find_element_by_xpath("//input[@itemprop='codeCountry']").clear()
            print('CLEARING THE SEARCH BAR')
            time.sleep(3)

            driver.find_element_by_xpath("//input[@itemprop='codeCountry']").send_keys(post)
            print('GIVING INPUT IN THE SEARCH BAR --> ', post)
            time.sleep(3)

            driver.find_element_by_xpath("//input[@itemprop='codeCountry']").send_keys(Keys.ARROW_DOWN)
            print('SELECTING THE FIRST RECOMMENDED OPTION --> ', post)
            time.sleep(3)

            driver.find_element_by_xpath("//input[@itemprop='codeCountry']").send_keys(Keys.ENTER)
            print('LOADING THE STORES AROUND --> ', post)
            time.sleep(3)

            while True:

                print('SCROLLING TILL THE END OF RESULTS')
                time.sleep(3)

                scr1 = driver.find_element_by_xpath("//div[@id='mCSB_1']")
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                time.sleep(3)

                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

                if driver.find_element_by_xpath("//a[@ng-show='isShowMore']").get_attribute('class') == 'ng-hide':
                    print('NOT INTRACTABLE')
                    break
                else:
                    driver.find_element_by_xpath("//a[@ng-show='isShowMore']").click()

            print('GETTING SOURCE CODE OF CLASS CONTAINING DEALERS LIST')
            page_source = driver.find_element_by_xpath("//div[@id='dealer-result']").get_attribute("outerHTML")
            print('SOURCE CODE OF CLASS CONTAINING DEALERS LIST FETCHED')

            soup = BeautifulSoup(page_source, 'lxml')
            search_container = soup.find_all("div", {"itemtype": "https://schema.org/location"})
            print('FINDING ALL DIVS IN DEALER LIST')

            for div in search_container:
                if div['data-id'] != "current-position-id":
                    dealer_code = div['data-id']
                    print('DEALER CODE --> ', dealer_code)

                    if dealer_code not in keys:

                        print('DEALER CODE NOT PRESENT IN THE LIST SO APPENDING --> ', dealer_code)
                        keys.append(dealer_code)
                        print('APPEND DONE NOW EXTRACTING DATA')

                        ####################
                        ####################
                        try:
                            manufacturer_unique_id = div['data-id']
                        except Exception as e:
                            manufacturer_unique_id = ''
                            print('Exception while getting manufacturer_unique_id --> ', e)
                            pass
                        print('manufacturer_unique_id -> ', manufacturer_unique_id)
                        items['manufacturer_unique_id'] = manufacturer_unique_id
                        ####################
                        ####################
                        try:
                            store_name = div.find("p", {"itemprop": "name"}).text
                        except Exception as e:
                            store_name = ''
                            print('Exception while getting store_name --> ', e)
                            pass
                        print('store_name ->', store_name)
                        items['store_name'] = store_name
                        ####################
                        ####################
                        try:
                            full_address = div.find("div", {"itemprop": "addressRegion"}).find("span").text
                        except Exception as e:
                            full_address = ''
                            print('Exception while getting full_address --> ', e)
                            pass
                        print('full_address ->', full_address)
                        items['full_address'] = full_address
                        ####################
                        ####################
                        try:
                            email_id = div.find("div", {"itemprop": "endDate"}).find("span").text
                        except Exception as e:
                            email_id = ''
                            print('Exception while getting email_id --> ', e)
                            pass
                        print('email_id ->', email_id)
                        items['email_id'] = email_id
                        ####################
                        ####################
                        try:
                            phone_number = div.find("span", {"itemprop": "telephone"}).text
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
                            if div.find("div", {"ng-class": "{'has__apolloZone':dealer.IsApolloZone()}"}).get('class') is None:
                                apollo_zone = '0'
                            else:
                                apollo_zone = '1'
                        except Exception as e:
                            apollo_zone = ''
                            print('Exception while getting apollo_zone --> ', e)
                            pass
                        print('apollo_zone --> ', apollo_zone)
                        items['apollo_zone'] = apollo_zone
                        ####################
                        ####################
                        try:
                            brand = 'APOLLO'
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
