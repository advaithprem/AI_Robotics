from gpiozero import DistanceSensor
from time import sleep

ultrasens = DistanceSensor(echo=17, trigger=27)
while True:
    print(ultrasens.distance * 100, 'cm')
    sleep(2)