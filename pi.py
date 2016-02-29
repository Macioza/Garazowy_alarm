import time, httplib, urllib, urllib2
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
pir_pin = 17
przek_pin = 22
wyl_pin = 25
kon_pin = 26
io.setup(pir_pin, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(wyl_pin, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(kon_pin, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(przek_pin, io.OUT)
licznik = 0
io.output(przek_pin, io.LOW)
while True:
	if io.input(kon_pin) == 0:
		licznik = licznik + 1
		print("wykryto %s") %licznik
		io.output(przek_pin, io.HIGH)
		time.sleep(5)
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		conn.request("POST", "/1/messages.json", urllib.urlencode({"token": "aMrBqbkbRRgjrEUn5HnDvJrikTnViT", "user": "ucyKVK6zEZ5LKe9kmS2cgPRgwvAyF3", "message": "Ktos wszedl do HQ", "sound": "siren" }), { "Content-type": "application/x-www-form-urlencoded" })
		print(conn.getresponse())
		
	time.sleep(1)
	
	if io.input(wyl_pin):
		io.output(przek_pin, io.LOW)
