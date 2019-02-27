import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN)    # set GPIO25 as input (button)  
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(4): 
            print "2"  
            sleep(5)         
        elif GPIO.input(17): 
            print "3"  
            sleep(5)         
        elif GPIO.input(27): 
            print "4"    
            sleep(5)         
        else:  
            print "NO NUMBER"  
        sleep(5)         
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  