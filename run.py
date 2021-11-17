import re, json, requests
from config import *
import html
import urllib
import pandas as pd

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

    keyword_shopee = urllib.parse.quote(keyword_search)
    
    HEADER_SHOPEE["Referer"] = HEADER_SHOPEE["Referer"].format(shopee = URL_WEB_SHOPEE, keyword = keyword_shopee)
    URL_SEARCH_SHOPEE = URL_SEARCH_SHOPEE.format(keyword =keyword_shopee)

    res_shopee = requests.get(URL_SEARCH_SHOPEE, headers = HEADER_SHOPEE).json()

    keyword_jd_central = urllib.parse.quote(keyword_search)
    
    HEADER_JD_CENTRAL["Referer"] = HEADER_JD_CENTRAL["Referer"].format(jd_central = URL_WEB_JD_CENTRAL, keyword = keyword_jd_central)
    URL_SEARCH_JD_CENTRAL = URL_SEARCH_JD_CENTRAL.format(keyword =keyword_jd_central)
    

    res_Jd_central = requests.get(URL_SEARCH_JD_CENTRAL,headers=HEADER_JD_CENTRAL).json()

    JD_Queue = Queue()    
    Shopee_Queue = Queue()

    print('\n*****SHOPEE*****\n')
    for item in res_shopee["items"]:
        dict_shopee_product = {}
        image_link = (URL_IMAGE_SHOPEE+str(item['item_basic']['image']))
        dict_shopee_product["Image_link  "] = image_link
        dict_shopee_product["name        "] = item['item_basic']['name']
        if (int(item['item_basic']['price_min']) != int(item['item_basic']['price_max'])):
            dict_shopee_product['price       '] = "price min : "+str(int(item['item_basic']['price_min'])/100000)+"บาท |  price max : "+str(int(item['item_basic']['price_max'])/100000) +"บาท"
        else:
            dict_shopee_product['price       '] = "price : "+str(int(item['item_basic']['price'])/100000)+"บาท"
        taillink = item['item_basic']['name']
        newtaillink = taillink.replace(" ","-")
        Product_link = URL_LINK_ITEM_SHOPEE+newtaillink
        Product_link = Product_link +'-i.'+ str(item['item_basic']['shopid'])+'.'+str(item['item_basic']['itemid'])
        dict_shopee_product["Product Link"] = Product_link
        Shopee_Queue.enQueue(dict_shopee_product)

    for item_dict in Shopee_Queue.items:
        for i in item_dict:
            print(i,':',item_dict[i])
        print('-'*100)   
  


    print('\n*****JD_CENTRAL*****\n')
    for item in res_Jd_central["wareInfo"]:
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