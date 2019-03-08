import requests
import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 15)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

i = 1
j = 0

URL = "http://172.17.2.10:3000/api/imageReader"


try:
    while True:            # this will carry on until you hit CTRL+C
        if i == 1:
                print "Question 1"
                data = {
                "devID": "imageReader",
                "question": "How much is 1 + 1 ?",
                "boolean": 0,
                "value": ""
                }
                response = requests.request("POST", URL, data=data)
		print(response.text)
                j = 1
                while j == 1:
                        if GPIO.input(4):
				print "2"
                                print "CORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 1 + 1 ?",
                                "boolean": 0,
                                "value": "2"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
                                j = 0
                        elif GPIO.input(17):
                                print "3"
                                print "INCORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 1 + 1 ?",
                                "boolean": "False",
                                "value": "3"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
                                sleep (4)
                        elif GPIO.input(27):
                                print "4"
                                print"INCORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 1 + 1 ?",
                                "boolean": "False",
                                "value": "4"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
                                sleep(4)
                        else:
                                sleep(4)
                i = 2
        elif i == 2:
		print "Question 2"
                data = {
                "devID": "imageReader",
                "question": "How much is 5 - 2?",
                "boolean": "False",
                "value": ""
                }
                response = requests.request("POST", URL, data=data)
		print(response.text)
		sleep(5)
                j = 1
                while j == 1:
                        if GPIO.input(4):
                                print "2"
				print "INCORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 5 - 2 ?",
                                "boolean": "False",
                                "value": "2"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
				sleep(4)
                        elif GPIO.input(17):
                                print"3"
				print"CORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 5 - 2 ?",
                                "boolean": "True",
                                "value": "3"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
				j = 0
                        elif GPIO.input(27):
                                print "4"
				print"INCORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 5 - 2 ?",
                                "boolean": "False",
                                "value": "4"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
				sleep(4)
                        else:
                                sleep(4)
		i = 3
        elif i == 3:
		print "Question 3"
                data = {
                "devID": "imageReader",
                "question": "How much is 2 * 2 ?",
                "boolean": "False",
                "value": ""
                }
                response = requests.request("POST", URL, data=data)
		print(response.text)
		sleep(5)
                j = 1
                while j == 1:
                        if GPIO.input(4):
                                print "2"
				print"INCORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 2 * 2 ?",
                                "boolean": "False",
                                "value": "2"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
				sleep(4)
                        elif GPIO.input(27):
                                print "4"
				print "CORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 2 * 2 ?",
                                "boolean": "True",
                                "value": "4"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
				j = 0
                        elif GPIO.input(17):
                                print "3"
				print "INCORRECT"
                                data = {
                                "devID": "imageReader",
                                "question": "How much is 2 * 2 ?",
                                "boolean": "False",
                                "value": "3"
                                }
                                response = requests.request("POST", URL, data=data)
				print(response.text)
				sleep(4)
                        else:
                                sleep(4)
		i = 4
        elif i == 4:
                data = {
                "devID": "imageReader",
                "question": "YOU WIN THE GAME",
                "boolean": "True",
                "value": ""
                }
                response = requests.request("POST", URL, data=data)
		print(response.text)
                print "YOU WIN THE GAAME"
                i = 5
        elif i == 5:
                sleep(4)

finally:
        GPIO.cleanup()          #clean up
