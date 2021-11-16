import re, json, requests
from config import *
import html
import urllib
import pandas as pd


if __name__ == "__main__":
    keyword_search = input("search : ")
    print('-' * 100)

    keyword_shopee = urllib.parse.quote(keyword_search)
    
    HEADER_SHOPEE["Referer"] = HEADER_SHOPEE["Referer"].format(shopee = URL_WEB_SHOPEE, keyword = keyword_shopee)
    URL_SEARCH_SHOPEE = URL_SEARCH_SHOPEE.format(keyword =keyword_shopee)

    res = requests.get(URL_SEARCH_SHOPEE, headers = HEADER_SHOPEE).json()

    lstshopee = []
    for item in res["items"]:
        image_link = requests.get(URL_IMAGE_SHOPEE+str(item['item_basic']['image']))
        #img = Image.open(BytesIO(image_link.content))
        #img.show()
        print(item['item_basic']['name'])
        if (int(item['item_basic']['price_min']) != int(item['item_basic']['price_max'])):
            print("price min : ",int(item['item_basic']['price_min'])/100000,"บาท |  price max : ",int(item['item_basic']['price_max'])/100000 ,"บาท")
        else:
            print("price : ",int(item['item_basic']['price'])/100000,"บาท")
        taillink = item['item_basic']['name']
        newtaillink = taillink.replace(" ","-")
        link = URL_LINK_ITEM_SHOPEE+newtaillink
        link = link +'-i.'+ str(item['item_basic']['shopid'])+'.'+str(item['item_basic']['itemid'])
        print(link)
        lstshopee.append(item['item_basic']['name'])
        print("-" * 100)
  
