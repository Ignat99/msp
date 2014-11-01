#!/usr/bin/python
# Source code: http://maxembedded.com/2014/07/25/using-raspberry-pi-gpio-using-python/
# LED Switch code for Raspberry Pi
# Written in Python 2.7.3
import RPi.GPIO as GPIO         ## Import GPIO Library
import time                     ## Import 'time' library (for 'sleep')
 
outPin = 7                      ## LED connected to pin 7
inPin = 13                      ## Switch connected to pin 13
count = 0                       ## Initialize counter to 0
GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
GPIO.setup(outPin, GPIO.OUT)    ## Set pin 7 to OUTPUT
GPIO.setup(inPin, GPIO.IN)      ## Set pin 13 to INPUT
 
while True:                     ## Do this forever
    value = GPIO.input(inPin)   ## Read input from switch
    if value:                   ## If switch is released
        GPIO.output(outPin, 1)  ## Turn on LED
    else:                       ## Else switch is pressed
        GPIO.output(outPin, 0)  ## Turn off LED
        count = count + 1       ## Increment counter
        print "count=" +str(count) ## Display counter on screen
    time.sleep(0.2)             ## Wait for things to settle down - debouncing
 
GPIO.cleanup()                  ## Cleanup
