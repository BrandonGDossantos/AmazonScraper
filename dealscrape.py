#!/usr/bin/env python
import sys
f = open("output.txt", 'w')
sys.stdout = f
from bs4 import BeautifulSoup
from selenium import webdriver
page = 'http://www.amazon.com/gp/goldbox/ref=nav_cs_gb'
#for i in range(10):	
driver = webdriver.Firefox(executable_path='/home/ubuntu/AmazonScraper/geckodriver')
driver.get(page)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
divs = soup.find_all('div', attrs={'class': 'a-row dealContainer dealTile'})
for div in divs:
	tmp = div.find('span', attrs={'id': 'dealTitle'})
	print(tmp.get_text(strip=True) + '\n')
#page = soup.find('a', attrs={'href': '#next'})
driver.find_element_by_link_text('#next').click()
print(page)
driver.quit()
#driver.get(next)
f.close()








