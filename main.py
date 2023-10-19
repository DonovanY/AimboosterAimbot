# This is a sample Python script.
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
time.sleep(2)
img = pyautogui.screenshot(region=(400,0,1100,1000))
img.save(r"./savedimage.png")
# 32 230 229

def click(x,y):
    win32api.SetCursorPos((x,y))

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# Press the green button in the gutter to run the script.
while keyboard.is_pressed('z') == False:
    image = pyautogui.screenshot(region=(660,370,600,400))
    width, height = image.size
   # location = pyautogui.locateOnScreen('a.png', region=(400,0,1100,1000), confidence = 0.9)

    #if(location != None):
      ##  pyautogui.moveTo(location)



    for x in range(0,width,5):
       for y in range (0,height,5):
            r,g,b = image.getpixel((x,y))
            if (b in range(190,200)):
              click(x+660,y+370)
              time.sleep(0.05)
              break
 # See PyCharm help at https://www.jetbrains.com/help/pycharm/
