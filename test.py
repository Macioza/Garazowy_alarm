from ubidots import ApiClient
import random
import time

def polacz_z_ubidots():
	try:
		api = ApiClient("92c3631d495bfff93d3d3cf043772d46003d9e5b")
		test_variable = api.get_variable("565b6ef5762542203c6a4610")
	except:
		print "Connection error, trying again"
		time.sleep(40)
		api = ApiClient("92c3631d495bfff93d3d3cf043772d46003d9e5b")
		test_variable = api.get_variable("565b6ef5762542203c6a4610")

def main():
	while True:
		test_value = random.randint(1,100)
		test_variable.save_value({'value':test_value})
		time.sleep(1)

polacz_z_ubidots()
main()
