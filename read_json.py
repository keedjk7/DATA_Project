
import json
import requests
header_json = json.dumps(requests.get('https://api.jd.co.th/client.action?body=%7B%22page%22%3A%221%22%2C%22pagesize%22%3A%2260%22%2C%22cid%22%3A%22%22%2C%22filed%22%3A%22%22%2C%22expandName%22%3A%7B%7D%2C%22brand%22%3A%22%22%2C%22isCorrect%22%3A%221%22%2C%22sort%22%3A%220%22%2C%22stock%22%3A1%2C%22keyword%22%3A%22headphone%22%7D&functionId=search&client=pc&clientVersion=2.0.0&lang=th_TH&area=&jsonp=_jsonp69bimtzz1fs').content)
print(header_json)