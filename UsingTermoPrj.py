#!/usr/bin/python

import os
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-000007604d24/w1_slave'
temp_log = '/home/pi/Documents/WateringProject/temp_log'

def temp_raw():
	f = open(temp_sensor, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = temp_raw()
	temp_output = lines[1].find('t=')
	
	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string)/1000.0
		temp_f = temp_c*9.0/5.0+32.0
		return temp_c,temp_f

while True:
	f = open(temp_log, 'a')
	print read_temp()
	s = str(read_temp())
	f.write(s + '\n')
	f.close()
	time.sleep(1)
