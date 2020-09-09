#Ngapain lu bruh? 
#rizpedia

import os
import requests
from dotenv import load_dotenv

load_dotenv("config.env")


#data
COOKIE_CAPING = os.environ.get("COOKIE_CAPING", None)
AUTH_CAPING = os.environ.get("AUTH_CAPING", None)
INDEX_CAPING = os.environ.get("INDEX_CAPING", None)
TS_CAPING = os.environ.get("TS_CAPING", None)

#url host
url = 'https://ai.caping.co.id/v2/event/report'


#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":5105951, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":5105951, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":, "status": 1, "times": 2, "totalms": 39 } ] } ] }'


#headers
headers = {"Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": (COOKIE_CAPING), "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": (AUTH_CAPING), "ts": (TS_CAPING), "index" : (INDEX_CAPING), "Content-Type": "application/json", "Connection": "keep-alive"}


respon = requests.post(url, json = data, headers = headers)

print(respon)
