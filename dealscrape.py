#!/usr/bin/env python
import sys
#import urllib2
#import socket
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from xvfbwrapper import Xvfb
#vdisplay = Xvfb(width=1280, height=740, colordepth=16)
#vdisplay.start()
display = Display(visible=0, size=(1024, 768))
display.start()
f = open("output.txt", 'w')
sys.stdout = f
#executable_path='/home/ubuntu/AmazonScraper/geckodriver')
#try:
driver = webdriver.Firefox()
driver.implicitly.wait(30)
driver.maximize_window()
driver.get('https://www.amazon.com/gp/goldbox/ref=nav_cs_gb')
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
divs = soup.find_all('div', attrs={'class': 'a-row dealContainer dealTile'})
for div in divs:
	tmp = div.find('span', attrs={'id': 'dealTitle'})
	#print(tmp.get_text(strip=True) + '\n')
	print(tmp)
link = driver.findElement(By.linkText("//a[@href='Next']"))
print link
#except URLError, e:
#	print "Oops, timed out?"
#except socket.timeout:
#	print "Timed out!"

driver.close()
display.stop()
#vdisplay.stop()
f.close()
