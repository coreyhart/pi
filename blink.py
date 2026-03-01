#!/usr/bin/env python3
# *utf-8* [i think]
# blink.py
# Python Script to take a picture
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

LIGHT = 1.5
DELAY = .5

###right side 20 pin  
LED_1 = 16
LED_2 = 18
LED_3 = 22

###left side 20 pin
LED_6 = 11
LED_7 = 13
LED_8 = 15

##addl w 40 pin ,r then l
#LED_4 = 32
#LED_5 = 36

#LED_9 = 29
#LED_10 = 31
#LED_11 = 33
#LED_12 = 37

#-----------------------------------------------
# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO 
# would need more changes to use: import lgpio as GPIO

#for sleep
import time


GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_8, GPIO.OUT, initial=GPIO.LOW)

### light leds in order
def chase():
    
    while True: # Run forever
   
        print("\n" * 3) #"clear" screen
        
        print(f'pin {LED_1}')
        GPIO.output(LED_1, GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(LED_1, GPIO.LOW) # off               
        time.sleep(DELAY)
       
        print(f'pin {LED_2}')
        GPIO.output(LED_2, GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(LED_2, GPIO.LOW) # off               
        time.sleep(DELAY)
        
        print(f'pin {LED_3}')
        GPIO.output(LED_3, GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(LED_3, GPIO.LOW) # off               
        time.sleep(DELAY)
        
        print(f'pin {LED_6}')
        GPIO.output(LED_6, GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(LED_6, GPIO.LOW) # off               
        time.sleep(DELAY)
        
        print(f'pin {LED_7}')
        GPIO.output(LED_7, GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(LED_7, GPIO.LOW) # off               
        time.sleep(DELAY)
        
        print(f'pin {LED_8}')
        GPIO.output(LED_8, GPIO.HIGH) # on
        time.sleep(LIGHT)
        GPIO.output(LED_8, GPIO.LOW) # off               
        time.sleep(DELAY)
       
  
chase()

GPIO.cleanup() # Clean up


