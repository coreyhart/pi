#!/usr/bin/env python3
# *utf-8* [i think]
# takemypicture.py
# Python Script to take a picture
# Corey Hart
# corey@trusteddatapipeline.com
# 14 Feb 2026
# v0.12 alpha
# Usage: run in terminal, no good exit yet so just do interrupt [ctr+c]
# License: use at own risk, if it works mention me if not dont :)
#-----------------------------------------------
### Python Script to take a picture
### Is a work in progress 
### Change log at end
#-----------------------------------------------

# CONFIG
GRIN=['Smile!', 'Tractor Smoke!', 'Pickles!', 'Bunny Ears!', 'Now!','Nice!','Good One!']
PREVIEWTIME = 5 #how long to see pic after taking, in seconds
PIN = 10   #button
FLASH = 8  #led
#future stuff
#set filepath =
#set message =
#set pausetime = 
#set displayprevew = 1  #0 for off
#set saveprompt = 0
#set emailsend = 0

#-----------------------------------------------
# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO 
# would need more changes to use: import lgpio as GPIO

#for sleep
import time
#for camera control
#import libcamera
from picamera2 import Picamera2 #, Preview
#for preview
#from PIL import Image
import subprocess
#for lens catch phrases
import random



### setup camera function
def take_photo():
    cam = Picamera2()
    image_path = '/home/corey/Desktop/picam/images/image_%s.jpg' % int(round(time.time() * 1000))  
    config = cam.create_preview_configuration(main={"size": (1900,1440)})
    #1600, 1200
    #to flip add: config["transform"] = libcamera.Transform(hflip=1, vflip=1)
    cam.configure(config)
    #cam.start_preview(Preview.QTGL)
    cam.start()
    
    ### set auto-focus
    cam.set_controls({"AfMode": 1 ,"AfTrigger": 0})
    # {"AfMode": 0 ,"LensPosition": focus value}
    # AfMode Set the AF mode (manual, auto, continuous)
    # manual ({"AfMode": 0, "LensPosition": 425})
    # single focus: picam2.set_controls({"AfMode": 1 ,"AfTrigger": 0})
    # continuous focus: picam2.set_controls({"AfMode": 2 ,"AfTrigger": 0})
    # range of LensPosition changed from 0~15:
    
    ### countdown
    print("\n" * 10) #"clear" screen
    print("Get Ready")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(.7)
    #print("Smile!")
    print(random.choice (GRIN))
    ### light the light
    GPIO.output(FLASH, GPIO.HIGH) # on               
    time.sleep(.2)
    
    ### take pic
    cam.capture_file(image_path)
    #cam.capture(image_path)
    #rpicam-still -o %image_path
    
    ### Cleanup
    time.sleep(.1)
    GPIO.output(8, GPIO.LOW) # light off
    cam.close()
    print('...') 
    time.sleep(.5)
    print('Photo Saved') # text confirmation
    time.sleep(1)
    print("\n" * 10) #"clear" screen
    
    #show them what they did!
    p = subprocess.Popen(["feh", image_path])
    time.sleep(10)
    p.terminate()
    
    #prompt for next photo
    print("Push button to take a photo.")
### End take_photo()
    

### setup gpio
# Ignore warning for now
GPIO.setwarnings(False) 
# Use physical pin numbering
GPIO.setmode(GPIO.BOARD) 
# Set pin for button (usaully 10) to be an input pin and set initial value to be pulled low (off)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
# Set pin (8) for LED as output pin, initial value low (off)
GPIO.setup(FLASH, GPIO.OUT, initial=GPIO.LOW)   

### MAIN While
while True: # Run forever
    if GPIO.input(PIN) == GPIO.HIGH:
        take_photo()
        #time.sleep(1)
        
# Setup event on pin rising edge
# Note, this is better than "if GPIO.input(PIN) == GPIO.HIGH:" as detects the event and not the state, high state is true for multiple ticks
#GPIO.add_event_detect(PIN,GPIO.RISING,callback=take_picture)

# Run until someone presses enter
#message = input("Press enter to quit\n\n") 
GPIO.cleanup() # Clean up
 


#-- rpicam-still -o test.jpg
