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

	# display "load:" and 1 minute load average on first line
	lcd.lcd_display_string("  Sys Load Avg",1)

	# display 5 minute and 15 minute load averages on second line
	lcd.lcd_display_string(avg1 + "  " + avg5 + "  " + avg15,2)
	
	sleep(5)