from continentaltyres.ContinentaltyresItem import ContinentaltyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class ContinentaltyresspiderSpider(scrapy.Spider):
    name = 'continentaltyresspider'
    start_urls = ['https://www.continental-tyres.in/car']

    def parse(self, response, **kwargs):

        districts = ['Mumbai']

        for district in districts:

            driver.get('https://www.continental-tyres.in/car')
            print('Getting To Store Locator Page')
            time.sleep(3)

            driver.maximize_window()
            print('Maximizing Window')

            driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/section/div/button[1]').click()
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="dl-header-button"]').click()
            time.sleep(3)

            driver.find_element_by_name('inputLocation').send_keys(district)
            print('Giving Input in Search Bar --> ', district)
            time.sleep(3)

            driver.find_element_by_name('inputLocation').send_keys(Keys.ENTER)
            print('Hitting Enter for the District --> ', district)
            time.sleep(10)

            page_source = driver.page_source
            soup = BeautifulSoup(page_source, features = 'lxml')
            print('soup --> ', soup)