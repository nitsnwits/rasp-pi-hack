import time
import picamera
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.IN, gpio.PUD_UP)

path = raw_input("Enter path to save capture: ")
with picamera.PiCamera() as camera:
	camera.start_preview()
	gpio.wait_for_edge(18, gpio.FALLING)
	camera.capture(path+'/test.jpg')
	camera.stop_preview()


