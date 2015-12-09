import requests
import time
def polacz():
	try:
		requests.post("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
		print("ok")
		time.sleep(wait)
	except:
		print("not ok")
		time.sleep(wait)

if input("to start, press one ") == 1:
	connections = input("select number of connections ")
	wait = input("specyfy interval ")
	try:
		i = 0
		status = requests.get("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
		while status.text == "Congratulations! You've fired the 1 event" and i <= connections:
			i = i + 1
			polacz()
			print(i)
	except:
		print("chuj")