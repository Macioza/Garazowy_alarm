import httplib, urllib
import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('https://www.google.pl',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False
print(internet_on())
x = internet_on()
if x == True: 
	conn = httplib.HTTPSConnection("api.pushover.net:443") #determinuje conn jako obiekt 	klasy HTTPSConnection
	conn.request("POST", "/1/messages.json",
             # wywoluje funcje request z klasy HTTPSConnection.
             # POST to metoda,
             # "1/messages.json" to chyba url,
             # urllib.urlencode to body, a Content-type to header.
             # Funkcja request przyjmuje cztery zmienne, urllib.urlencode to stanowi jedna z nich.
	urllib.urlencode({
		"token": "aMrBqbkbRRgjrEUn5HnDvJrikTnViT",
		"user": "ucyKVK6zEZ5LKe9kmS2cgPRgwvAyF3",
		"message": "wiem, ze mnie lubisz",
		"sound": "siren" }), { "Content-type": "application/x-www-form-urlencoded" })
	print(conn.getresponse())