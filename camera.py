import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN)     
GPIO.setup(17, GPIO.IN)   
GPIO.setup(27, GPIO.IN)   

URL = "http://172.17.2.10:3000/api/imageReader"
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(4): 
            print "2"
            data = {
            "devID": "imageReader",
            "imageMessage": "2"
            }  
            sleep(5)         
        elif GPIO.input(17):
            data = {
            "devID": "imageReader",
            "imageMessage": "3"
            } 
            print "3"  
            sleep(5)         
        elif GPIO.input(27): 
            data = {
            "devID": "imageReader",
            "imageMessage": "4"
            }
            print "4"    
            sleep(5)         
        else:  
            print "NO NUMBER"  
        sleep(5)     

        try:
            response = requests.request("POST", URL, data=data)
            print(response.text)
        except:
            print("data not POSTED")
            print(data)
    
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  