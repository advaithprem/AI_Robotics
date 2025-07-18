from gpiozero import Button
from picamera2 import Picamera2, Preview
from signal import pause

pushbutton = Button(3)
picam = Picamera2()

def capture():
    picam.capture_file("/home/pi/Desktop/Ai/picture.jpg")

pushbutton.when_pressed = capture

picam.start_preview(Preview.QTGL)
picam.start()

pause()  # Keep the program running to allow button presses to be detected