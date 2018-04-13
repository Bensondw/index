#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

wp.pinMode(23, 1)

wp.digitalWrite(23, 1)
