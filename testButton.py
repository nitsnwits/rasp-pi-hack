#test button

import RPi.GPIO as GPIO
import time
import pdb
#pdb.set_trace()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print "button pressed"
		time.sleep(0.2)

