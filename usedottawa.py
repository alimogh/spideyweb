import requests
from bs4 import BeautifulSoup

#WebCrawler for one page
#modules BeautifulSoup
#url 
# Do UsedOttawa Website
def trade_spider(max_pages):
    page = 25
    while page <= max_pages:
        url = 'http://www.usedottawa.com/classifieds/all/' + str(page) + '?description=honda'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'itemprop':'name'}):
            href = "http://www.usedottawa.com/" + link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
            page+=25

#Dynamic Web Crawler
def get_single_item_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for item_name in soup.findAll('div',{'class':'article'}):
		print(item_name.string)
	for link in soup.findAll('a'):
		href = "http://www.usedottawa.com/" + link.get('href')
		print(href)



trade_spider(50) #of pages to crawl. 
