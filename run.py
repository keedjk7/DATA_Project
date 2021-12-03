import re, json, requests
from config import *
import html
import urllib
import pandas as pd

class node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class link_list():
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = newNode

    def __str__(self) :
        if self.head is None:
            return ''
        temp = str(self.head.data)

        last = self.head
        while last.next is not None:
            temp = temp + ' ' + str(last.next.data)
            last = last.next

        return temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        count_size = 0
        count_node = self.head
        while count_node is not None:
            count_size += 1
            count_node = count_node.next

        return count_size
    
    def sortPrice_min_to_max(self):
        #bubble sort
        count_node_for_check = self.head
        while count_node_for_check is not None:
            count_node = count_node_for_check.next
            while count_node is not None:
                if count_node_for_check.data['originPrice '] > count_node.data['originPrice ']:
                    temp = count_node_for_check.data
                    count_node_for_check.data = count_node.data
                    count_node.data = temp

                count_node = count_node.next
                
            count_node_for_check = count_node_for_check.next

    def sortPrice_max_to_min(self):
        #bubble sort
        count_node_for_check = self.head
        while count_node_for_check is not None:
            count_node = count_node_for_check.next
            while count_node is not None:
                if count_node_for_check.data['originPrice '] < count_node.data['originPrice ']:
                    temp = count_node_for_check.data
                    count_node_for_check.data = count_node.data
                    count_node.data = temp

                count_node = count_node.next
                
            count_node_for_check = count_node_for_check.next

    def sortRating_min_to_max(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data["Rating      "] > last.next.data["Rating      "]:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next 

    def sortRating_max_to_min(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data["Rating      "] < last.next.data["Rating      "]:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next

    def output(self):
        if self.head is None:
            return ''
        item_dict = self.head.data

        for i in item_dict:
            print(i,':',item_dict[i])
        print('-'*100)
        count_node = self.head
        while count_node is not None:
            item_dict = count_node.data
            for i in item_dict:
                print(i,':',item_dict[i])
            print('-'*100)
            count_node = count_node.next


def shopee(res_shopee,keyword_sort):
    Shopee_ll = link_list()

    print('\n*****SHOPEE*****\n')
    for item in res_shopee["items"]:
        dict_shopee_product = {}
        image_link = (URL_IMAGE_SHOPEE+str(item['item_basic']['image']))
        dict_shopee_product["Image_link  "] = image_link
        dict_shopee_product["name        "] = item['item_basic']['name']
        if (int(item['item_basic']['price_min']) != int(item['item_basic']['price_max'])):
            dict_shopee_product['price       '] = "price min : "+str(int(item['item_basic']['price_min'])/100000)+"บาท |  price max : "+str(int(item['item_basic']['price_max'])/100000) +"บาท"
            dict_shopee_product['originPrice '] = int(item['item_basic']['price_min'])/100000 #use price_min
        else:
            dict_shopee_product['price       '] = "price : "+str(int(item['item_basic']['price'])/100000)+"บาท"
            dict_shopee_product['originPrice '] = int(item['item_basic']['price'])/100000

        taillink = item['item_basic']['name']
        newtaillink = taillink.replace(" ","-")
        Product_link = URL_LINK_ITEM_SHOPEE+newtaillink
        Product_link = Product_link +'-i.'+ str(item['item_basic']['shopid'])+'.'+str(item['item_basic']['itemid'])
        dict_shopee_product["Product Link"] = Product_link
        a_float = float(item['item_basic']['item_rating']['rating_star'])
        formatted_float = '{:.2f}'.format(a_float)
        dict_shopee_product['Rating      '] = formatted_float
        Shopee_ll.append(dict_shopee_product)

    #Sort Price Min->Max
    if keyword_sort == 1:
        Shopee_ll.sortPrice_min_to_max()

    #Sort Price Max->Min
    elif keyword_sort == 2:
        Shopee_ll.sortPrice_max_to_min()

    #Sort Rating Min->Max
    elif keyword_sort == 3:
        Shopee_ll.sortRating_min_to_max()
    #Sort Rating Max->Min
    elif keyword_sort == 4:
        Shopee_ll.sortRating_max_to_min()

    Shopee_ll.output()


def JD_Central(res_Jd_central,keyword_sort):
    JD_Central_ll = link_list()  

    print('\n*****JD_CENTRAL*****\n')
    for item in res_Jd_central["wareInfo"]:
        dict_jd_product = {}
        dict_jd_product["Image_link  "] = item['imageurl']
        dict_jd_product["name        "] = item['wname']
        try:
            dict_jd_product['price       '] = 'original_price : '+item['originPrice']+'  บาท '+' JD price : '+item["jdPrice"]+'  บาท'
            dict_jd_product['originPrice '] = int(item['originPrice'])
        except KeyError:
            dict_jd_product['price       '] = 'JD price : '+item["jdPrice"]+'  บาท'
            dict_jd_product['originPrice '] = int(item['jdPrice'])
        wname_i = item['wname']
        wname_i = wname_i.replace(" ","%20")
        dict_jd_product["Product Link"] = URL_LINK_ITEM_JD_CENTRAL.format(wname = wname_i,wareId = item['wareId'])
        dict_jd_product['Rating      '] = float(item['starLevel'])
        JD_Central_ll.append(dict_jd_product)
        
    #Sort Price Min->Max
    if keyword_sort == 1:
        JD_Central_ll.sortPrice_min_to_max()

    #Sort Price Max->Min
    elif keyword_sort == 2:
        JD_Central_ll.sortPrice_max_to_min()

    #Sort Rating Min->Max
    elif keyword_sort == 3:
        JD_Central_ll.sortRating_min_to_max()
    #Sort Rating Max->Min
    elif keyword_sort == 4:
        JD_Central_ll.sortRating_max_to_min()

    JD_Central_ll.output()

if __name__ == "__main__":
    keyword_search = input("Enter item name for searching : ")
    print('Sort Price : \n  Case1 Min -> Max (Input 1): \n  Case2 Max -> Min (Input 2): \nSort Rating : \n  Case3 Min -> Max (Input 3): \n  Case4 Max -> Min (Input 4):')
    keyword_sort = int(input('Enter Type Sort : '))
    print('-' * 100)

    keyword_shopee = urllib.parse.quote(keyword_search)
    
    HEADER_SHOPEE["Referer"] = HEADER_SHOPEE["Referer"].format(shopee = URL_WEB_SHOPEE, keyword = keyword_shopee)
    URL_SEARCH_SHOPEE = URL_SEARCH_SHOPEE.format(keyword =keyword_shopee)

    res_shopee = requests.get(URL_SEARCH_SHOPEE, headers = HEADER_SHOPEE).json()

    keyword_jd_central = urllib.parse.quote(keyword_search)
    
    HEADER_JD_CENTRAL["Referer"] = HEADER_JD_CENTRAL["Referer"].format(jd_central = URL_WEB_JD_CENTRAL, keyword = keyword_jd_central)
    URL_SEARCH_JD_CENTRAL = URL_SEARCH_JD_CENTRAL.format(keyword =keyword_jd_central)
    

    res_Jd_central = requests.get(URL_SEARCH_JD_CENTRAL,headers=HEADER_JD_CENTRAL).json()  

    shopee(res_shopee,keyword_sort)

    JD_Central(res_Jd_central,keyword_sort)
    
