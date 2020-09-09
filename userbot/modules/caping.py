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
#headers
headers = { "Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": "u=73657394;n=ffffffffc86fb4dc4a9b6e244a9b6e24", "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": "BASIC MTM0OWYyMDU5NDg4NDIyZWIyNjY4YTQwYTI1M2YwMGY6MzNiMGM3NjUyN2I5OTBmNmQzN2I1NWRiYzZkNzI5NzQ=", "ts": "1597685499206", "index" : "39", "Content-Type": "application/json", "Connection": "Keep-Alive" }



#baner video
print("===== Nuyul Video ======")
time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609201, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609201, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609201", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609202, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609202, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609202", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())

time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609203, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609203, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609203", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609204, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609204, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609204", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609205, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609205, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609205", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609206, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609206, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609206", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609207, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609207, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609207", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609208, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609208, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609208", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609209, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609209, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609209", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609210, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609210, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609210", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609211, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609211, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609211", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609212, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609212, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609212", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609213, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609213, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609213", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609214, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609214, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609214", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609215, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609215, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609215", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609216, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609216, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609216", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609217, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609217, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609217", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609218, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609218, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609218", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609219, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609219, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609219", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())


time.sleep(3)
#data json
data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609220, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609220, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609220", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
#Post Data
respon = requests.post(url = url, headers = headers, data = data)
print(respon.json())

#baner berita
print("=====Nuyul Berita=====")
print("KAMBING SUN")
