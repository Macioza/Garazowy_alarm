import httplib, urllib, urllib2, time

def internet_on():
	try:
		esponse=urllib2.urlopen('https://www.google.pl',timeout=1)
		return True
	except: 
		pass
		return False
print(internet_on())

while True:
	try:
		if internet_on() == True:
			conn = httplib.HTTPSConnection("api.pushover.net:443")
			conn.request("POST", "/1/messages.json",
				urllib.urlencode({
					"token": "aMrBqbkbRRgjrEUn5HnDvJrikTnViT",
					"user": "ucyKVK6zEZ5LKe9kmS2cgPRgwvAyF3",
					"message": "wiem, ze mnie lubisz",
					"sound": "siren" }), { "Content-type": "application/x-www-form-urlencoded" })
		print(conn.getresponse())
		time.sleep(5)
	except:
		pass