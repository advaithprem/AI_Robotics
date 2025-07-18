from gpiozero import LEDBoard
from time import sleep
from signal import pause
leds = LEDBoard(2,3,4,17,27,22,10,9)
for i in leds:
    x = int(input("Enter 1 to turn on LED or 0 to turn off LED: "))
    leds[i].value = x
pause()  # Keep the program running to allow user interaction


    