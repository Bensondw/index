#!/usr/bin/python

import wiringpi as wp
import time

wp.wiringPiSetupGpio()

sensor = 20
LED = 19

wp.pinMode(sensor, 0)
wp.pinMode(LED, 1)

blue = True

while blue:
	hey = wp.digitalRead(sensor)
	if hey == 1:
		print "Old BEN KeNOBI"
		wp.digitalWrite(LED, 1)
		time.sleep(1)
	else:
		print "NO BEN HERE"
		wp.digitalWrite(LED, 0)
		time.sleep(1)



