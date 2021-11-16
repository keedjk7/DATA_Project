import re
import json
import requests
import pandas as pd
from PIL import Image
from io import BytesIO


keyword_search = ("headphone")
print("-"*100)

Shopee_url = "https://www.lazada.co.th"
headers = {
    "User-Agent": "Chrome",
    "Referer": "{}catalog/?q={}".format(Shopee_url, keyword_search),
}

url = "https://www.lazada.co.th/catalog/?q=headphone&_keyori=ss&from=input&spm=a2o4m.home.search.go.11256f84umCbPa"


# Shopee API request
r = requests.get(url, headers=headers).json()
lstshopee = []
count = 0
for item in r["items"]:
    #img = Image.open(BytesIO(image_link.content))
    #img.show()
    print(item['item_basic']['name'])
    if (int(item['item_basic']['price_min']) != int(item['item_basic']['price_max'])):
        print("price min : ",int(item['item_basic']['price_min'])/100000,"บาท |  price max : ",int(item['item_basic']['price_max'])/100000 ,"บาท")
    else:
        print("price : ",int(item['item_basic']['price'])/100000,"บาท")
    taillink = item['item_basic']['name']
    newtaillink = taillink.replace(" ","-")
    #link = 'https://shopee.co.th/{}'.format(newtaillink)
    #link = link +'-i.'+ str(item['item_basic']['shopid'])+'.'+str(item['item_basic']['itemid'])
    #print(link)
    lstshopee.append(item['item_basic']['name'])
    df = pd.DataFrame(get_ratings(item["shopid"], item["itemid"]))
    print(df.head()) # print only the head for brevity
    print("-" * 100)
    count+=1
print(count)
