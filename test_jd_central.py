import requests
from bs4 import BeautifulSoup

Baseurl = 'https://www.thewhiskyexchange.com/'

headers = {
    "User-Agent": "Chrome",
}

r_jd = requests.get('https://www.thewhiskyexchange.com/c/340/white-rum')
soup = BeautifulSoup(r_jd.content,'lxml')
productlist = soup.body.find_all('div',class_='item')
print(productlist)