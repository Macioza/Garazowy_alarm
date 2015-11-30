from ubidots import ApiClient
import random
import time
import requests

api = ApiClient("92c3631d495bfff93d3d3cf043772d46003d9e5b")
test_variable = api.get_variable("565c48007625425dd74d15c7")

def main():
	licznik = 0
	while True:
		test_value = random.randint(1,100)
		try:
			test_variable.save_value({'value':test_value})
			requests.post("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
			licznik = licznik + 1
			print "success nr %s" %licznik
		except:
			print "error"
			time.sleep(40)
			print "one more time"
			test_variable.save_value({'value':test_value}
			requests.post("https://maker.ifttt.com/trigger/1/with/key/RpT2e05KGbf-5B4jO00o7")
			
		time.sleep(5)
	
main()
