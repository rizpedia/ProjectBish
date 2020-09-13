# Rizpedia
# Jual Followers Subs Yt Dll
# Kontak @RizkiRmdhn (telegram)

# Import Module
import time
import requests
import os
import json
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register
from userbot import COOKIE_CAPING,AUTH_CAPING,TS_CAPING,INDEX_CAPING


# Env
# = 'u=73657394;n=ffffffffc86fb4dc4a9b6e244a9b6e24'
# = 'BASIC MTM0OWYyMDU5NDg4NDIyZWIyNjY4YTQwYTI1M2YwMGY6MzNiMGM3NjUyN2I5OTBmNmQzN2I1NWRiYzZkNzI5NzQ='
# = '1597685499206'
# = '39'

# Run
@register(outgoing=True, pattern="^.capingb$")
async def pingme(pong):
	await pong.edit("__Tuyul berita dimulai__")
	host = 'https://ai.caping.co.id/v2/event/report'
	header = { "Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": (COOKIE_CAPING), "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": (AUTH_CAPING), "ts": (TS_CAPING), "index" : (INDEX_CAPING), "Content-Type": "application/json", "Connection": "Keep-Alive" }
	id = 7609200
	start = True
	sesi = 0
	pesansiapkirim = "=====|Hasil Nuyul Berita|====="
	while start:
		# Post Data
		time.sleep(1)
		id += 1
		datapost = {"reports":[{"action":"browse_news","list":[{"articleType":1,"newsId":(id),"status":1,"times":3,"totalms":40},{"articleType":1,"newsId":(id),"status":1,"times":2,"totalms":37}]}]}
		post = requests.post(url = host, headers = header, json = datapost)
		respon = (post.text)
		# Json to str
		jsonload = json.loads(str(respon))	
		printjson = (jsonload["data"])
		pesansiapkirim += "\n" + "Point bertambah : " + (str(printjson))
		# Kirim Pesan
		if sesi == 79:
			await pong.edit(pesansiapkirim)
			start = False
		sesi += 1

@register(outgoing=True, pattern="^.capingv$")
async def pingme(pong):
	await pong.edit("__Tuyul video dimulai__")
	host = 'https://ai.caping.co.id/v2/event/report'
	header = { "Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": (COOKIE_CAPING), "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": (AUTH_CAPING), "ts": (TS_CAPING), "index" : (INDEX_CAPING), "Content-Type": "application/json", "Connection": "Keep-Alive" }
	id = 5105951
	start = True
	sesi = 0
	pesansiapkirim = "=====|Hasil Nuyul Video|====="
	while start:
		# Post Data
		time.sleep(1)
		id += 1
		datapost = { "reports": [ { "action": "watch_video", "list": [ { "articleType": 512, "newsId":(id), "status": 0, "times": 2, "totalms": 5 }, { "articleType": 512, "newsId":(id), "status": 0, "times": 1, "totalms": 0 }, { "articleType": 512, "newsId":(id), "status": 1, "times": 2, "totalms": 39 } ] } ] }
		post = requests.post(url = host, headers = header, json = datapost)
		respon = (post.text)
		# Json to str
		jsonload = json.loads(str(respon))	
		printjson = (jsonload["data"])
		pesansiapkirim += "\n" + "Point bertambah : " + (str(printjson))
		# Kirim Pesan
		if sesi == 20:
			await pong.edit(pesansiapkirim)
			start = False
		sesi += 1
		
@register(outgoing=True, pattern="^.capinginfo$")
async def pingme(pong):
	url = 'https://ai.caping.co.id/v2/user/login/visitor'
	headers = { "Accept": "application/json", "Accept-Language": "in", "NETWORKSTATE": "FouthG", "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;CapingNews/5.3.0", "Cookie": (COOKIE_CAPING), "Market": "googleplay", "AppId": "1", "loginType": "1", "Authorization": (AUTH_CAPING), "ts": (TS_CAPING), "index" : (INDEX_CAPING), "Content-Type": "application/json", "Connection": "Keep-Alive" }
	req = requests.post(url = url, headers = headers, json = {"city":"Jakarta"})
	json1 = json.loads(req.text)
	dump = json.dumps(json1["data"])
	json2 = json.loads(dump)
	user = str(json2["user_name"])
	userid = str(json2["user_id"])
	userscore = str(json2["user_score"])
	userhonor = str(json2["user_honor"])
	userlvl = str(json2["user_level"])
	await pong.edit("Username : "+(user)+"\nID : "+(userid)+"\nPoint : "+(userscore)+"\nLevel : "+(userlvl)+ "\nHonor : "+(userhonor))


# Help Cli
CMD_HELP.update({
     "caping":
     ">.capingv"
     "\nUsage: Untuk nuyul video caping, jika data 0 berarti kena limit harian.\n\n"
     ">.capingb"
     "\nUsage: Untuk nuyul berita caping, jika data 0 berarti kena limit harian.\n\n"
     ">.capinginfo"
     "\nUsage : Untuk mengetahui informasi akun caping anda"
})
