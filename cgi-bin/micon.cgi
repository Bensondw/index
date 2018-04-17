#!/usr/bin/python

import os

print "Content-type: application/json"
print

os.system("sudo chmod 777 /dev/ttyS0")
os.system("sudo service icecast2 start")
os.system("sudo darkice")

print
