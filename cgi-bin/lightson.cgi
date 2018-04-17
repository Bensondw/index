#!/usr/bin/python

print "Content-type: application/json"
print

import wiringpi as wp

import time

wp.wiringPiSetupGpio()

wp.pinMode(19, 1)
wp.pinMode(21, 1)
wp.pinMode(22, 1)


#while (True):

wp.digitalWrite(19, 1)
#time.sleep(2)
#wp.digitalWrite(19, 0)
wp.digitalWrite(21, 1)
#time.sleep(2)
#wp.digitalWrite(21, 0)
wp.digitalWrite(22, 1)
#time.sleep(2)
#wp.digitalWrite(22, 0)

print
