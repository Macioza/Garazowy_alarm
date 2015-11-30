from ubidots import ApiClient
import random
import time

api = ApiClient("92c3631d495bfff93d3d3cf043772d46003d9e5b")
test_variable = api.get_variable("565b6ef5762542203c6a4610")

def main():
	licznik = 0
	while True:
		test_value = random.randint(1,100)
		try:
			test_variable.save_value({'value':test_value})
			licznik = licznik + 1
			print "success nr %s" %licznik
		except:
			print "error"
			time.sleep(40)
			print "one more time"
			test_variable.save_value({'value':test_value})
			
		time.sleep(1)
		
main()
