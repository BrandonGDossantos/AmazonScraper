#!/usr/bin/env python
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox(executable_path='/home/ubuntu/AmazonScraper/geckodriver')
driver.get('http://www.amazon.com/gp/goldbox/ref=nav_cs_gb')
html = driver.page_source
soup = BeautifulSoup(html)
#clean_soup = [span.get_text(strip=True) for span in soup.find_all('span', attrs={'id': 'dealTitle'})]
#for item in clean_soup:
#	print(item + '\n')
	#print(clean_soup)
divs = soup.find_all('div', attrs={'class': 'a-row dealContainer dealTile'})
for div in divs:
	if div.find('span', attrs={'data-action': 'gbdeal-addtocart'}):
		tmp = div.find('span', attrs={'id': 'dealTitle'})
		print(tmp)
		#print('Yes')






