from gpiozero import Button
from picamera2 import Picamera2, Preview
from signal import pause
from datetime import datetime

pushbutton = Button(2)
picam = Picamera2()

def capture():
    picam.capture_file(f'/home/pi/Desktop/Ai/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')
    print("captured")

pushbutton.when_pressed = capture

picam.start_preview(Preview.QTGL)
picam.start()

pause()  # Keep the program running to allow button presses to be detected``