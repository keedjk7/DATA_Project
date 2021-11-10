import re
import json
import requests
import pandas as pd

#test
def get_ratings(shop_id, item_id):
    ratings_url = "https://shopee.sg/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0"

    offset = 0
    d = {"username": [], "rating": [], "comment": []}
    while True:
        data = requests.get(
            ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)
        ).json()

        i = 1
        for i, rating in enumerate(data["data"]["ratings"], 1):
            d["username"].append(rating["author_username"])
            d["rating"].append(rating["rating_star"])
            d["comment"].append(rating["comment"])

        if i % 20:
            break

        offset += 20

    return d

keyword_search = input("Search : ")
print("-"*100)

Shopee_url = "https://shopee.th"
headers = {
    "User-Agent": "Chrome",
    "Referer": "{}search?keyword={}".format(Shopee_url, keyword_search),
}

url = "https://shopee.co.th/api/v4/search/search_items?by=relevancy&keyword={}&limit=100&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2".format(
    keyword_search
)


# Shopee API request
r = requests.get(url, headers=headers).json()
lst = []
count = 0
for item in r["items"]:
    print(item['item_basic']['name'])
    if (int(item['item_basic']['price_min']) != int(item['item_basic']['price_max'])):
        print("price min : ",int(item['item_basic']['price_min'])/100000,"บาท |  price max : ",int(item['item_basic']['price_max'])/100000 ,"บาท")
    else:
        print("price : ",int(item['item_basic']['price'])/100000,"บาท")
    taillink = item['item_basic']['name']
    newtaillink = taillink.replace(" ","-")
    link = 'https://shopee.co.th/{}'.format(newtaillink)
    link = link +'-i.'+ str(item['item_basic']['shopid'])+'.'+str(item['item_basic']['itemid'])
    print(link)
    lst.append(item['item_basic']['name'])
    #df = pd.DataFrame(get_ratings(item["shopid"], item["itemid"]))
    #print(df.head()) # print only the head for brevity
    print("-" * 100)
    count+=1
print(count)
