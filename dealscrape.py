from lxml import html
import requests
from bs4 import BeautifulSoup

def AmzonParser(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	page = requests.get(url,headers=headers)
	soup = BeautifulSoup(page.content)
	product_name = [a.text.strip() for a in soup.findAll("div",{"id":"100_dealView"})]
	print(product_name)




	#spans = soup.find_all('div', {'id' : '100_dealView_3'})
	#lines = [span.get_text() for span in spans]
	#storedtxt = []
	#for line in lines:
	#	print('line')


if __name__ == "__main__":
    AmzonParser("https://www.amazon.com/gp/goldbox/ref=nav_cs_gb")
