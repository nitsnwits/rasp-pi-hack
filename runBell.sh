#!/bin/bash
#
# 	This script will make rasp pi hack run forever
#
#

PIPATH = "/home/pi/Desktop/hangout"

echo "/usr/bin/sudo /usr/bin/python ${PIPATH}/hangout.py" | at now
if [ $? -eq 0 ]
	then
	echo "Scheduled script to run forever.."
else
	echo "Error scheduling script."
fi