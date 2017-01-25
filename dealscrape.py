#!/usr/bin/env python
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary()
driver = webdriver.Firefox(executable_path='/home/ubuntu/AmazonScraper/geckodriver')
driver.get('http://www.amazon.com/gp/goldbox/ref=nav_cs_gb')
html = driver.page_source
soup = BeautifulSoup(html)
#data = []
clean_soup = [span.get_text(strip=True) for span in soup.find_all('span', attrs={'id': 'dealTitle'})]
#for span in spans:
#	data.append(span.text)
#result = ''.join([	
#print(span.get_text())
print(clean_soup)
