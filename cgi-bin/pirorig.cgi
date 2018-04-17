#!/usr/bin/python

import wiringpi as wp
import time
import json

print "Content-type: application/json"
print

wp.wiringPiSetupGpio()

sensor = 20

wp.pinMode(sensor, 0)

blue = True

while blue:
	hey = wp.digitalRead(sensor)
	if hey == 1:
		print "It's BEN!"
		response = "present"
		time.sleep(1)
	else:
		print "Who's There?"
		time.sleep(1)
		response = "no present"

print(json.JSONEncoder().encode(response))
