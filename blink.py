#!/usr/bin/env python3
# *utf-8* [i think]
# blink.py
# Python Script to blink some leds
# Corey Hart
# corey@trusteddatapipeline.com
# 28 Feb 2026
# v0.1 alpha
# Usage: run in terminal, no good exit yet so just do interrupt [ctr+c]
# License: use at own risk; if it works mention me, if not don't :)
#-----------------------------------------------
### Python Script to blink some leds
### Is a work in progress 
### Change log at end
#-----------------------------------------------

# CONFIG
##set pin numbers

LIGHT = 2
DELAY = 1.5
PINS = [11,13,15,16,18]
#APINS = [29,31,33,37,22,32,36]

#-----------------------------------------------
# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO 

#for sleep
import time

#setup pins
GPIO.setmode(GPIO.BOARD)
T=0
while T < len(PINS):
    GPIO.setup(PINS[T], GPIO.OUT, initial=GPIO.LOW)
    T = T+1
GPIO.output(11, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)

### make function to light leds in order of array
def chase():
    
    C = 0
    
    while True: # Run forever
        print("\n" * 1) #"clear" screen
        
        #manage counter
        if C >=5:
            C =0
        
        #blink pin
        print(f'pin {PINS[C]}')
        GPIO.output(PINS[C], GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(PINS[C], GPIO.LOW) # off               
        time.sleep(DELAY)
       
        #increment counter
        C = C+1
      
#Call chase function we just defined      
chase()

GPIO.cleanup() # Clean up


