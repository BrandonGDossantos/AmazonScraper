#!/usr/bin/env python
import sys
import os
#import urllib2
#import socket
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from xvfbwrapper import Xvfb
#vdisplay = Xvfb(width=1280, height=740, colordepth=16)
#vdisplay.start()
binary = FirefoxBinary('/usr/bin')
display = Display(visible=0, size=(1024, 768))
display.start()
f = open("output.txt", 'w')
sys.stdout = f
url = 'https://www.amazon.com/gp/goldbox/ref=nav_cs_gbps_ftr_s-3_bb19_page_1?gb_f_GB-SUPPLE=page:1'
#url = 'https://www.amazon.com/gp/goldbox/ref=nav_cs_gb'
driver = webdriver.Firefox(executable_path='/home/ubuntu/AmazonScraper/geckodriver')
driver.maximize_window()
driver.get(url)
print('\t' + "Page: 1")
try:
	for i in range(10):
		print(url)
		html = driver.page_source
		soup = BeautifulSoup(html, "lxml")
		divs = soup.find_all('div', attrs={'class': 'a-row dealContainer dealTile'})
		for div in divs:
			tmp = div.find('span', attrs={'id': 'dealTitle'})
			print(tmp.get_text(strip=True).encode('utf-8'))
			#print(tmp)
		url = list(url)
		url[68] = str(i + 2)
		url[90] = str(i + 2)
		url = "".join(url)
		driver.get(url)
		print('\t' + "Page: " + str(i + 2))
except KeyboardInterrupt:
	driver.close()
	display.stop()
	f.close()
finally:
	driver.close()
	display.stop()
	#vdisplay.stop()
	f.close()
