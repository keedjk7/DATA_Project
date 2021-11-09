import re
import json
import requests
import pandas as pd


def get_ratings(shop_id, item_id):
    ratings_url = "https://shopee.sg/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0"

    offset = 0
    d = {"username": [], "rating": [], "comment": []}
    while True:
        data = requests.get(
            ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)
        ).json()

        # uncomment this to print all data:
        # print(json.dumps(data, indent=4))

        i = 1
        for i, rating in enumerate(data["data"]["ratings"], 1):
            d["username"].append(rating["author_username"])
            d["rating"].append(rating["rating_star"])
            d["comment"].append(rating["comment"])

        if i % 20:
            break

        offset += 20

    return d


Shopee_url = "https://shopee.sg"
keyword_search = "headphone"
headers = {
    "User-Agent": "Chrome",
    "Referer": "{}search?keyword={}".format(Shopee_url, keyword_search),
}

url = "https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&order=desc&page_type=search".format(
    keyword_search
)
print(type(url))
# can change "relevancy" to "latest": to sort by latest products instead

# Shopee API request
r = requests.get(url, headers=headers).json()
count = 0
for item in r["items"]:
    print(item["name"])
    #df = pd.DataFrame(get_ratings(item["shopid"], item["itemid"]))
    #print(df.head()) # print only the head for brevity
    print("-" * 80)
    count+=1
print(count)