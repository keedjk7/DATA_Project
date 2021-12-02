import re, json, requests
from config import *
import html
import urllib
import pandas as pd



class node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linklist():
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode
    def __str__(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        
        last=self.head
        while (last.next is not None):
            temp=temp+" "+str(last.next.data)
            
            last=last.next
            
        return temp
    def output(self):
        if self.head is None:
            return ""
        item_dict=self.head.data
        for i in item_dict:
            print(i,':',item_dict[i])
        print('-'*100)
        last=self.head
        while (last.next is not None):
            item_dict=last.data
            for i in item_dict:
                print(i,':',item_dict[i])
            print('-'*100)            
            last=last.next
            
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def dequeue(self):
        temp=self.head.data
        self.head=self.head.next
        return temp
    def size(self):
        size=0
        last=self.head
        while last is not None:
            last=last.next
            size=size+1
        return  size
    def sortMax(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data["Rating      "] < last.next.data["Rating      "]:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next
    def sortMin(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data["Rating      "] > last.next.data["Rating      "]:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next   


if __name__ == "__main__":

    keyword_search = input("search : ")
    print("Rating :rx mean sort Max to Min")
    print("Rating :rn mean sort Min to Max")
    keyword_sort = input("PLEASE ENTER YOUR SORT : ")
    print('-' * 100)

    keyword_shopee = urllib.parse.quote(keyword_search)
    
    HEADER_SHOPEE["Referer"] = HEADER_SHOPEE["Referer"].format(shopee = URL_WEB_SHOPEE, keyword = keyword_shopee)
    URL_SEARCH_SHOPEE = URL_SEARCH_SHOPEE.format(keyword =keyword_shopee)

    res_shopee = requests.get(URL_SEARCH_SHOPEE, headers = HEADER_SHOPEE).json()

    keyword_jd_central = urllib.parse.quote(keyword_search)
    
    HEADER_JD_CENTRAL["Referer"] = HEADER_JD_CENTRAL["Referer"].format(jd_central = URL_WEB_JD_CENTRAL, keyword = keyword_jd_central)
    URL_SEARCH_JD_CENTRAL = URL_SEARCH_JD_CENTRAL.format(keyword =keyword_jd_central)
    

    res_Jd_central = requests.get(URL_SEARCH_JD_CENTRAL,headers=HEADER_JD_CENTRAL).json()


    Shopee_ll = linklist()
    JD_ll = linklist()

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
        a_float = float(item['item_basic']['item_rating']['rating_star'])
        formatted_float = "{:.2f}".format(a_float)
        dict_shopee_product["Rating      "] = formatted_float
        Shopee_ll.append(dict_shopee_product)
    if keyword_sort == "rx":
        Shopee_ll.sortMax()
    elif keyword_sort == "rn":
        Shopee_ll.sortMin()
    Shopee_ll.output() 
  

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
        dict_jd_product["Rating      "] = float(item['starLevel'])
        JD_ll.append(dict_jd_product)

    if keyword_sort == "rx":
        JD_ll.sortMax()
    elif keyword_sort == "rn":
        JD_ll.sortMin()
    JD_ll.output()
        
   