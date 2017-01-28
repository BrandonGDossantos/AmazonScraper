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
url = 'https://www.amazon.com/gp/goldbox/ref=nav_cs_gb'
driver = webdriver.Firefox(executable_path='/home/ubuntu/AmazonScraper/geckodriver')
driver.maximize_window()
driver.get(url)
for i in range(3):
	html = driver.page_source
	soup = BeautifulSoup(html, "lxml")
	divs = soup.find_all('div', attrs={'class': 'a-row dealContainer dealTile'})
	for div in divs:
		tmp = div.find('span', attrs={'id': 'dealTitle'})
		print(tmp.get_text(strip=True))
		#print(tmp)
	url = driver.find_element_by_partial_link_text('Next')
 
#print link
#except URLError, e:
#	print "Oops, timed out?"
#except socket.timeout:
#	print "Timed out!"

driver.close()
display.stop()
#vdisplay.stop()
f.close()
