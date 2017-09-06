#!/usr/bin/env python
import sys
import os
import re
import sqlite3
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from xvfbwrapper import Xvfb


binary = FirefoxBinary('/usr/bin')
display = Display(visible=0, size=(1024, 768))
display.start()
url = 'https://www.amazon.com/gp/goldbox/ref=nav_cs_gbps_ftr_s-3_bb19_page_1?gb_f_GB-SUPPLE=page:1'
driver = webdriver.Firefox()
driver.get(url)

def database():
	db = sqlite3.connect('amazon.db')
	c = db.cursor()
	c.execute("DROP TABLE IF EXISTS products")
	c.execute("CREATE TABLE IF NOT EXISTS products (title TEXT, price INT, review INT, link TEXT, pid INTEGER PRIMARY KEY AUTOINCREMENT)")
	db.commit()

def parse():
	for page in range(10):
		print(url)
		html = driver.page_source
		soup = BeautifulSoup(html, "lxml")
		divs = soup.find_all('div', attrs={'class': 'a-row dealContainer dealTile'})
		for div in divs:
			if div.find_all('span', attrs={'data-action' : 'gbdeal-addtocart'}):
				tmp = div.find('span', attrs={'id': 'dealTitle'})			
				links = div.find('a', attrs={'class': 'a-link-normal'})
				prices = div.find('span', attrs={'class': 'a-size-medium a-color-base inlineBlock unitLineHeight'})
				reviews = div.find('span', attrs={'id': 'totalReviews'})
				title = tmp.get_text(strip=True)	
				link = links['href']
				link = re.sub('/ref.*', '', link)
				if prices == None:
					price = ""	
					continue
				else:
					price = prices.text
				if reviews == None:
					review = ""
					continue
				else:
					review = reviews.text
					
					# print("Title: {}\nPrice: {}\nReview: {}\nLink: {}\nPage: {}".format(title, price, review, link, page)) 
					save(title.encode('utf-8'), price, review.encode('utf-8'), link.encode('utf-8'), page, url.encode('utf-8'))
			else:
				continue
def save(title, price, review, link, page, url):
	db = sqlite3.connect('amazon.db')
	c = db.cursor()
	
	c.execute("INSERT INTO products (title, price, review, link) VALUES(?, ?, ?, ?)", (title, price, review, link))
	db.commit()
	url = list(url)
	url[68] = str(page + 2)
	url[90] = str(page + 2)
	url = "".join(url)
	driver.get(url)

if __name__=="__main__":
	database()
	parse()
