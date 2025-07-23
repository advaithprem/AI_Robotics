from gpiozero import DigitalInputDevice, LED
irsenor = DigitalInputDevice(17)
led = LED(2)
from time import sleep

while True:
    if irsenor.value:
        print("IR Sensor is not triggered")
        led.on()
    else:
        print("IR Sensor is triggered")
        led.off()
    sleep(1)  # Check every second






    