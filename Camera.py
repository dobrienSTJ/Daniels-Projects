#Allowing a preview of the Camera for 20 Seconds
#*Only on plugged in Monitors*
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(20)
camera.stop_preview()
