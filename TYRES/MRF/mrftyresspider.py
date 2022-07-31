from mrftyres.MrftyresItem import MrftyresItem
import time
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class MrftyresspiderSpider(scrapy.Spider):

    name = 'mrftyresspider'

    start_urls = ['https://www.mrftyres.com/']


    def parse(self, response, **kwargs):

        driver.get('https://www.mrftyres.com/')
        print('Getting To Store Locator Page')
        time.sleep(3)

        driver.maximize_window()
        print('Maximizing Window')
        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[5]/div[1]/a').click()
        print('Closing Pop-ups')
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="storeLocatorStage1"]').location_once_scrolled_into_view

        liElement = driver.find_element_by_xpath('//*[@id="andaman-and-nicobar"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", liElement)