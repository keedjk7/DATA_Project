
import requests
from bs4 import BeautifulSoup

baseurl = 'https://shopee.co.th/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

r = requests.get('https://shopee.co.th/%E0%B8%99%E0%B8%B2%E0%B8%AC%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B9%81%E0%B8%A7%E0%B9%88%E0%B8%99%E0%B8%95%E0%B8%B2-cat.11044952')

soup = BeautifulSoup(r.content,"html.parser")
print(soup.body)


#productlist = soup.find_all('div',class_='col-xs-2-4 shopee-search-item-result__item')


#print(productlist)