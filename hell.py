import requests
import time
def polacz(): 
	status = requests.get("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
	#print(status.text)
	while status.text == "Congratulations! You've fired the 1 event":
		try:
			requests.post("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
			print("ok")
		except:
			print("error")

polacz()

