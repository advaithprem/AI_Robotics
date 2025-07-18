from gpiozero import Button, LED
from time import sleep
button = Button(3)
led = LED(2)
while True:
    if button.is_pressed:
        led.on()  
    else:
        led.off()