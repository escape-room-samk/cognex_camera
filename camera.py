from gpiozero import LED
from time import sleep
from signal import pause
from gpiozero import Button

button2 = Button(4)
button3 = Button(17)
button4 = Button(27)

led2 = LED(18)
led3 = LED(23)
led4 = LED(24)

while True:
    
    if button2.is_pressed and button3.is_pressed and button4.is_pressed:
        print("SELECT ANY ANSWER")
    elif button3.is_pressed and button4.is_pressed:
        print("Answer 2")
    elif button2.is_pressed and button4.is_pressed:
        print("Answer 3")
    elif button2.is_pressed and button3.is_pressed:
        print("Answer 4")