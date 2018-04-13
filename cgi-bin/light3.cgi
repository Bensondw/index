#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

wp.pinMode(22, 1)

wp.digitalWrite(22, 1)
