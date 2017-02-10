#The MIT License (MIT)
#
#Copyright (c) [2017] [Dillon 'abcleanonme' Angle] [https://blog.abcleanon.me]
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Import Modules
import lcddriver, sys, os
from time import *

# Set up LCD
lcd = lcddriver.lcd(0x27)
lcd.backlightOn()

while 1 == 1:
	
	# get load averages
	avg1 = "{0:.2f}".format(os.getloadavg()[0])
	avg5 = "{0:.2f}".format(os.getloadavg()[1])
	avg15= "{0:.2f}".format(os.getloadavg()[2])
	
	# print load averages to terminal
	#print "System Load Averages"
	#print "1 Minute:   " + avg1
	#print "5 Minutes:  " + avg5
	#print "15 Minutes: " + avg15

	# display "Sys Load Avg" on first line
	lcd.lcd_display_string("  Sys Load Avg",1)

	# display 1 minute, 5 minute, and 15 minute load averages on second line
	lcd.lcd_display_string(avg1 + "  " + avg5 + "  " + avg15,2)
	
	# check and display averages every 5 seconds
	sleep(5)
