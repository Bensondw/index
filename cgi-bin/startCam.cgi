#!/usr/bin/python

print("Content-type: text/html\n\n")
print("<!DOCTYPE html>\n<head>")

import os

os.system("sudo chmod 777 /dev/vchiq")

os.system("LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i 'input_raspicam.so -fps 15 -q 50 -x 640 -y 480' -o 'output_http.so -p 9001 -w /opt/mjpg-streamer/www' &")

print
