# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:07:03 2017

@author: alsherman
"""

import win32gui, win32ui, win32con, win32api
import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2
import time
import matplotlib.pyplot as plt
import cv2
import face_recognition
import numpy as np
from PIL import ImageGrab
import cv2
import time
from time import sleep

screen_record()


def screen_record(): 
    last_time = time.time()
    num = 1

    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar. 
        image =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))

        face_locations = face_recognition.face_locations(image)

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))            
            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            
        cv2.imshow('window',cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
        
        output_path = r'C:\Users\alsherman\Desktop\General_Assembly\self_driving_car\images\trevor_noah\img{}.jpg'.format(num)
        num += 1
        cv2.imwrite(output_path, face_image)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def grab_screen(region=None):

    hwin = win32gui.GetDesktopWindow()

    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

"""
image_path = "1545065_10152255319188169_1338789760_n.jpg"

# Load the jpg file into a numpy array
image = face_recognition.load_image_file(image_path)

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
"""


