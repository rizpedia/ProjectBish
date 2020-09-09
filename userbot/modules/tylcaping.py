#rizpedia
#ngapain bruh?

import time
import requests
import os
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register
from dotenv import load_dotenv

load_dotenv("config.env")


#data
COOKIE_CAPING = os.environ.get("COOKIE_CAPING", None)
AUTH_CAPING = os.environ.get("AUTH_CAPING", None)
INDEX_CAPING = os.environ.get("INDEX_CAPING", None)
TS_CAPING = os.environ.get("TS_CAPING", None)


@register(outgoing=True, pattern="^.caping$")
async def pingme(pong):
   await pong.edit("Tuyul dimulai")
   sesi = 0
   url = 'https://ai.caping.co.id/v2/event/report'
   headers = { "Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": (COOKIE_CAPING), "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": (AUTH_CAPING), "ts": (TS_CAPING), "index" : (INDEX_CAPING), "Content-Type": "application/json", "Connection": "Keep-Alive" }
   id = 5105963
   json = { "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":(id), "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":(id), "status": 1, "times": 2, "totalms": 39 } ] } ] }
   datajson = "=======Nuyul Video======="
   while sesi < 20 :
        time.sleep(1)
        id = id + 1
        respon = requests.post(url = url, headers = headers, json = json)
        responjson = (respon.json())
        sesi = sesi + 1
        datajson = datajson + "\n" + (str(responjson))
        await pong.edit(str(datajson))
CMD_HELP.update({
     "caping":
     ">.caping"
     "\nUsage: Untuk nuyul caping, jika data 0 berarti kena limit harian."
})
