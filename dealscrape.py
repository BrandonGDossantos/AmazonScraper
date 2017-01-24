#!/usr/bin/env python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('C:\Program Files\Mozilla Firefox')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://www.amazon.com/gp/goldbox/ref=nav_cs_gb')
html = driver.page_source
soup = BeautifulSoup(html)
for link in soup.find_all('a', href=True):
	print(link['href'])
