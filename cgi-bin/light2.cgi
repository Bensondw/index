#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

wp.pinMode(21, 1)

wp.digitalWrite(21, 1)
