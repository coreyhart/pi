#!/usr/bin/env python3
# *utf-8* [i think]
# showpicture.py
# Python Script to display an image
# Corey Hart
# corey@trusteddatapipeline.com
# 14 Feb 2026
# v0.01 beta
# Usage: run in terminal, no good exit yet so just do interrupt [ctr+c]
# License: use at own risk, if it works mention me if not dont :)
#-----------------------------------------------

#from skimage.viewer import ImageViewer
#from skimage.io import imread
import sys
import tkinter as tk

PIC = sys.argv[1]
photo = tk.PhotoImage(file = PIC)

root = tk.Tk()
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, width = 1920, height  = 1280)
canvas.create_image(0, 0, image = photo, anchor = tk.NW)
canvas.place(x = 0, y = 0)

root.bind('a', key)           
root.mainloop()


#img = imread(PIC) #path to IMG
#view = ImageViewer(img)
#view.show()