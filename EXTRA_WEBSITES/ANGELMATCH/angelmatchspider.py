import scrapy
import time
from bs4 import BeautifulSoup
from angelmatch.AngelmatchItem import AngelmatchItem
from selenium import webdriver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')


class AngelmatchspiderSpider(scrapy.Spider):
    name = 'angelmatchspider'
    start_urls = ['https://angelmatch.io/?q=&hPP=3&idx=demo_INVESTORS&p=0']
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def parse(self, response, **kwargs):
        items = AngelmatchItem()

        for page in range(6):
            next_page = 'https://angelmatch.io/?q=&hPP=3&idx=demo_INVESTORS&p=' + str(page + 0)
            print('next_page --> ', next_page)
            driver.get(next_page)
            print('LOADING WEBSITE')
            time.sleep(3)

            page_source = driver.page_source
            soup = BeautifulSoup(page_source, features='lxml')
            ais_hits_item = soup.find_all('div', {'class': 'ais-hits--item'})

            for data in ais_hits_item:

                ####################
                ####################

                try:
                    name = data.find('h1', {'class': 'hit-title card-header-title'}).text
                except Exception as e:
                    name = ''
                    print('Exception while getting name --> ', e)
                    pass
                print('name --> ', name)
                items['name'] = name

                ####################
                ####################

                try:
                    company_name = data.find('h1', {'style': 'flex-grow:0;color: purple;font-size: 1.1rem;font-weight:bold; padding: 0;'}).text
                except Exception as e:
                    company_name = ''
                    print('Exception while getting company_name --> ', e)
                    pass
                print('company_name --> ', company_name)
                items['company_name'] = company_name

                ####################
                ####################

                try:
                    email_id = data.find('a', {'class': 'hit-title'}).get('href')
                except Exception as e:
                    email_id = ''
                    print('Exception while getting email_id --> ', e)
                    pass
                #print('email_id --> ', email_id)
                items['email_id'] = email_id

                ####################
                ####################

                try:
                    locations = data.find('span', {'style': 'font-size:0.7rem'}).text
                except Exception as e:
                    locations = ''
                    print('Exception while getting locations --> ', e)
                    pass
                #print('locations --> ', locations)
                items['locations'] = locations

                ####################
                ####################

                try:
                    links = {}
                    linkslist = data.find('div', {'class': 'social-icons'}).find_all('a', {'target': '_blank'})
                    for link in range(len(linkslist)):
                        links.update({"link_url_" + str(link + 1): linkslist[link].get('href')})
                except Exception as e:
                    links = ''
                    print('Exception while getting links --> ', e)
                    pass
                #print('links --> ', links)
                items['links'] = links

                ####################
                ####################

                try:
                    investment_focuses = {}
                    investment_focuses_list = data.find_all('span', {'style': 'font-weight:bold, margin-top:5px; margin-bottom:5px'})
                    for inv_foc in range(len(investment_focuses_list)):
                        investment_focuses.update({"investment_focuses_" + str(inv_foc + 1): investment_focuses_list[inv_foc].text})
                except Exception as e:
                    investment_focuses = ''
                    print('Exception while getting investment_focuses --> ', e)
                    pass
                #print('investment_focuses --> ', investment_focuses)
                items['investment_focuses'] = investment_focuses

                ####################
                ####################

                try:
                    companies_invested_in = {}
                    companies_invested_in_list = data.find_all('span', {'style': 'margin-top:5px; '})
                    for com_int_in in range(len(companies_invested_in_list)):
                        companies_invested_in.update({"companies_invested_in_" + str(com_int_in + 1): companies_invested_in_list[com_int_in].text})
                except Exception as e:
                    companies_invested_in = ''
                    print('Exception while getting investment_focuses --> ', e)
                    pass
                #print('companies_invested_in --> ', companies_invested_in)
                items['companies_invested_in'] = companies_invested_in

                ####################
                ####################

                try:
                    companies_invested_in_links = {}
                    companies_invested_in_links_list = data.find_all('span', {'style': 'margin-top:5px; '})
                    for com_int_in_link in range(len(companies_invested_in_links_list)):
                        companies_invested_in_links.update({"companies_invested_in_links_" + str(com_int_in_link + 1): companies_invested_in_links_list[com_int_in_link].find('a').get('href')})
                except Exception as e:
                    companies_invested_in_links = ''
                    print('Exception while getting investment_focuses --> ', e)
                    pass
                #print('companies_invested_in_links --> ', companies_invested_in_links)
                items['companies_invested_in_links'] = companies_invested_in_links

                ####################
                ####################

                try:
                    website = data.find('a', {'target': '_blank'}).get('href')
                except Exception as e:
                    website = ''
                    print('Exception while getting website --> ', e)
                    pass
                print('website --> ', website)
                items['website'] = website

                ####################
                ####################

                yield items

                url = website
                print('url --> ', url)
                driver.get(url)
                time.sleep(3)

                page_source = driver.page_source
                print('page_source --> ', page_source)