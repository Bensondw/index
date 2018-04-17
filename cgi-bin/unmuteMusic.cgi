#! /usr/bin/python

print "Content-type: application/json"
print

import os

os.system("sudo amixer -c 1 set PCM unmute")

print
