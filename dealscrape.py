#!/usr/bin/env python
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary()
driver = webdriver.Firefox(executable_path='/home/ubuntu/AmazonScraper/geckodriver')
driver.get('http://www.amazon.com/gp/goldbox/ref=nav_cs_gb')
html = driver.page_source
soup = BeautifulSoup(html)
spans = soup.find_all('span', attrs={'id': 'dealTitle'})
for span in spans:
	print span.string
	
