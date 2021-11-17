import http.client

conn = http.client.HTTPSConnection("lazada-product-data.p.rapidapi.com")

payload = "https://www.lazada.co.th/catalog/?spm=a2o4m.home.search.1.11256f84z5u1JK&q=headphone&_keyori=ss&from=search_history&sugg=headphone_0_1"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "lazada-product-data.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

conn.request("POST", "/service/get_lzd_detail.json", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))