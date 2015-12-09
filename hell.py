import requests
import time
def polacz():
	try:
		requests.post("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
		print("ok")
		time.sleep(5)
	except:
		print("not ok")
		time.sleep(5)

if input("to start, press one ") == 1:
	try:
		i = 0
		status = requests.get("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
		while status.text == "Congratulations! You've fired the 1 event" and i <= 3:
			i = i + 1
			polacz()
			print(i)
	except:
		print("chuj")