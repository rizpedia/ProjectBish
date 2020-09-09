#rizpedia
#ngapain bruh?

import time
import requests
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.caping$")
async def pingme(pong):
    await pong.edit("`Tuyul dimulai`")
    url = 'https://ai.caping.co.id/v2/event/report'
    headers = { "Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": "u=73657394;n=ffffffffc86fb4dc4a9b6e244a9b6e24", "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": "BASIC MTM0OWYyMDU5NDg4NDIyZWIyNjY4YTQwYTI1M2YwMGY6MzNiMGM3NjUyN2I5OTBmNmQzN2I1NWRiYzZkNzI5NzQ=", "ts": "1597685499206", "index" : "39", "Content-Type": "application/json", "Connection": "Keep-Alive" }
    data = '{ "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":7609201, "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":7609201, "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":"7609201", "status": 1, "times": 2, "totalms": 39 } ] } ] }'
    respon = requests.post(url = url, headers = headers, data = data)
    responjson = (respon.json())
    await pong.edit("respon: "(responjson))

CMD_HELP.update({
     "caping":
     ">`.caping`"
     "\nUsage: Untuk nuyul caping, jika data 0 berarti kena limit harian."
})
