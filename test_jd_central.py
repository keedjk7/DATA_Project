from os import error
import requests
from typing import Text
from config import *
import urllib

class Queue:  
    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else :
            self.items = list
    def enQueue(self,i):
        self.items.append(i)       
    def deQueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []

if __name__ == "__main__":
    keyword_search = input("search : ")
    print('-' * 100)
    keyword_jd_central = urllib.parse.quote(keyword_search)
    
    HEADER_JD_CENTRAL["Referer"] = HEADER_JD_CENTRAL["Referer"].format(jd_central = URL_WEB_JD_CENTRAL, keyword = keyword_jd_central)
    URL_SEARCH_JD_CENTRAL = URL_SEARCH_JD_CENTRAL.format(keyword =keyword_jd_central)
    

    res = requests.get(URL_SEARCH_JD_CENTRAL,headers=HEADER_JD_CENTRAL).json()
    JD_Queue = Queue()

    for item in res["wareInfo"]:
        dict_jd_product = {}
        dict_jd_product["Image_link  "] = item['imageurl']
        dict_jd_product["name        "] = item['wname']
        try:
            dict_jd_product['price       '] = 'original_price : '+item['originPrice']+'  บาท '+' JD price : '+item["jdPrice"]+'  บาท'
        except KeyError:
            dict_jd_product['price       '] = 'JD price : '+item["jdPrice"]+'  บาท'
        wname_i = item['wname']
        wname_i = wname_i.replace(" ","%20")
        dict_jd_product["Product Link"] = URL_LINK_ITEM_JD_CENTRAL.format(wname = wname_i,wareId = item['wareId'])
        JD_Queue.enQueue(dict_jd_product)
        
    for item_dict in JD_Queue.items:
        for i in item_dict:
            print(i,':',item_dict[i])
        print('-'*100)
  
