#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:30:32 2017

@author: notered234
// Reference Start of Arduino:
// https://www.arduino.cc/en/Guide/LilyPadMacOSX
// tutorial of this Projec:
// https://www.instructables.com/id/Arduino-Python-Communication-via-USB/
"""

# Part 0 - do not comment this part.
import serial
arduino = serial.Serial('/dev/cu.usbmodem1411', 115200, timeout=.1)



# Part 1 - comment this part when using Part 2.
#while True:
#	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
#	if data:
#		print(data)



# Part 2  
import time
time.sleep(1) #give the connection a second to settle
#python2:
#arduino.write("Hello from Python!")
#python3: not very sure for this command.
arduino.write(("Hello from Python!").encode())

while True:
	data = arduino.readline()
	if data:
#		print(data.strip('\n')) #strip out the new lines for now
		# (better to do .read() in the long run for this reason
         print(data)


