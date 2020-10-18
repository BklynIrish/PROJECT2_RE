#Import Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import pymongo
import requests
from splinter import Browser

def renewable_scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.renewableenergyworld.com"
    base_url = "https://www.renewableenergyworld.com"
    browser.visit(url)
    response4 = requests.get(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    link_list = []
    title_list = []

    for x in range (4):
        #url = "https://www.renewableenergyworld.com"
        browser.visit(url)
        link_ = soup.findAll('article')
        link = link_[x].find('link').get('href')
        link_list.append(link)
        link_ = soup.findAll('article')
        title = link_[x].find('h2', class_='post-list-item__title').find('a').text
        link_list.append(link)
        title_list.append(title)

    print(link_list)
    print(title_list)