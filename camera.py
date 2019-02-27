from gpiozero import LED
from time import sleep
from signal import pause
from gpiozero import Button
import requests

URL = "http://172.17.2.99:3000/api/imageReader"


button2 = Button(4)
button3 = Button(17)
button4 = Button(27)

led2 = LED(18)
led3 = LED(23)
led4 = LED(24)

while True:
    
    if button2.is_pressed and button3.is_pressed and button4.is_pressed:
        print("SELECT ANY ANSWER")
        sleep(4)
    elif button3.is_pressed and button4.is_pressed:
        print("Answer 2")
        data = {
        "devID": "imageReader",
        "imageMessage": "2"
        }
        sleep(4)
    elif button2.is_pressed and button4.is_pressed:
        print("Answer 3")
        data = {
        "devID": "imageReader",
        "imageMessage": "3"
        }
        sleep(4)
    elif button2.is_pressed and button3.is_pressed:
        print("Answer 4")
        data = {
        "devID": "imageReader",
        "imageMessage": "4"
        }
        sleep(4)
    try:
        response = requests.request("POST", URL, data=data)
        print(response.text)
    except:
        print("data not POSTED")
        print(data)
