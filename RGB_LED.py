from gpiozero import RGBLED
from time import sleep
led = RGBLED(red=17, green=27, blue=22)
while True:
    led.red = 0
    led.green = 0
    led.blue = 0