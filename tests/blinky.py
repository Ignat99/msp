#!/usr/bin/python
# Source code: http://maxembedded.com/2014/07/25/using-raspberry-pi-gpio-using-python/
# LED Blinky code for Raspberry Pi
# Written in Python 2.7.3
import RPi.GPIO as GPIO     ## Import GPIO Library
import time                 ## Import 'time' library (for 'sleep')
 
## Define function named ledBlink()
def ledBlink(pin, numTimes, delay):
    for i in range(0,numTimes):         ## Run loop numTimes
        print "Iteration " + str(i+1)   ## Print current loop
        GPIO.output(pin, GPIO.HIGH)     ## Turn on GPIO pin (HIGH)
        time.sleep(delay)               ## Wait
        GPIO.output(pin, GPIO.LOW)      ## Turn off GPIO pin (LOW)
        time.sleep(delay)               ## Wait
    print "Done"            ## When loop is complete, print "Done"
 
## Prompt user for input
pin = raw_input("Enter GPIO pin to blink: ");
nTimes = raw_input("Enter the number of times to blink: ")
delay = raw_input("Enter the duration of each blink in seconds: ")
 
GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
GPIO.setup(int(pin), GPIO.OUT)  ## Set GPIO pin to OUTPUT
 
## Call ledBlink() function for GPIO pin
ledBlink(int(pin), int(nTimes),float(delay))
 
## Finally, clean up!
GPIO.cleanup()
