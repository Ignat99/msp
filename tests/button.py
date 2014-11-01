#!/usr/bin/python
# Source of program: http://sourceforge.net/p/raspberry-gpio-python/tickets/77/#85b8
# But PIN_IN=23 and pull_up_down = GPIO.PUD_DOWN changed to 27 and GPIO.PUD_UP
import RPi.GPIO as GPIO
import time

# Good diagram http://maxembedded.com/2014/07/25/using-raspberry-pi-gpio-using-python/
# button connected to 27 (P1-13) and Ground (P1-14)
PIN_IN = 27

# Use CPU name of GPIO27 (not P1-13)
GPIO.setmode(GPIO.BCM)
# http://elinux.org/RPi_Low-level_peripherals#Internal_Pull-Ups_.26_Pull-Downs
# Default PIN_IN set to 3.3 volt through resistance Pull-up is Min. 50K Ohm, Max 65 KOhm
# For more info look to http://raspberrypi.ru/blog/readblog/133.html 
GPIO.setup(PIN_IN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# This function we call every time, when state of PIN_IN cange by push button
def printFunction(channel):
    print("Button 1 pressed!")
    localtime = time.asctime( time.localtime(time.time()) )
    print("Local current time :", localtime)
    time.sleep(3)
    print('Finished callback')

# http://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# Add falling edge detection on a PIN_IN, ignoring further edges for 300ms for switch bounce handling
GPIO.add_event_detect(PIN_IN, GPIO.FALLING, callback=printFunction, bouncetime=300)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
