import time
import picamera
import RPi.GPIO as GPIO

with picamera.PiCamera() as camera:
	camera.start_preview()
	time.sleep(1)
	camera.start_recording('/home/pi/testVideo.h264')
	time.sleep(1)
	camera.stop_recording()
	camera.stop_preview()
