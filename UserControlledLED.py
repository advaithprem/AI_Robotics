from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(2, 3, 4, 17, 27, 22, 10, 9)

for i in range(len(leds)):
    x = int(input(f"Enter 1 to turn ON or 0 to turn OFF LED {i+1}: "))
    leds[i].value = x

pause()  # Keep the program running to allow user interaction