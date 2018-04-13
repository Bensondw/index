#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

wp.pinMode(19, 1)
wp.pinMode(21, 1)
wp.pinMode(22, 1)

wp.digitalWrite(19, 0)
wp.digitalWrite(21, 0)
wp.digitalWrite(22, 0)
