import cv2
import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
import pyscreenshot as ImageGrab
from PIL import Image
import PIL
import win32api, win32con
import time
from decimal import Decimal

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


def getImage():
  #take screenshot
  #im= cv2.imread('cropped.png')
  im = ImageGrab.grab(bbox=(1842,685,2000,700))
  return im


def getRsi():
    while True:
      try:
          crop = getImage()
          text = pytesseract.image_to_string(crop)
          test =text[8:13] +'0'
          RSI = float(test)
          break
      except:
          print('Rsi Error')
    return RSI




def mouseMove(call):
    x =1900
    y=55
    bx = x+500
    sx = bx-200
    by = y+350
    xf=bx-100
    yf = by+40

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    if call ==1:
        win32api.SetCursorPos((bx,by))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, bx, by, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, bx, by, 0, 0)

    if call ==0:
        win32api.SetCursorPos((sx, by))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, sx, by, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, sx, by, 0, 0)

    win32api.SetCursorPos((xf,yf))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, xf, yf, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, xf, yf, 0, 0)
    closebuy(call)

def sell():
  mouseMove(0)


def buy():
  mouseMove(1)

def getProfit():
    while True:
        #im1.save('oprice.png')

        try:
            # im = ImageGrab.grab(bbox=(3350, 1035, 3500, 1055))
            im = ImageGrab.grab(bbox=(3375, 1020, 3415, 1040))
            # im.save('profit.png')
            im1 = ImageGrab.grab(bbox=(2510, 1020, 2560, 1040))
            im1.save('oprice.png')
            im2 = ImageGrab.grab(bbox=(2900, 1020, 2960, 1040))
            # im2.save('cprice2.png')
            profit = pytesseract.image_to_string(im, \
                                                 config='--psm 10 --oem 3 -c tessedit_char_whitelist=.012345678-9')
            time.sleep(1)
            oprice = pytesseract.image_to_string(im1, \
                                             config='--psm 10 --oem 3 -c tessedit_char_whitelist=.012345678-9')
            cprice = pytesseract.image_to_string(im2, \
                                             config='--psm 10 --oem 3 -c tessedit_char_whitelist=.012345678-9')
            o= float(oprice)
            c= float(cprice)
            res = c-(o)
            res = round(res, 3)
            break
        except:
            print('error')
    return o, c, res


def closebuy(bs):
    val = 0.05
    x=1
    input,output,result = getProfit()
    print('buy price:', input)
    print('sell price:',output)
    while x==1:
        if bs==1:
            input, output,result = getProfit()
            print(result)
            if (result>0.05):
                n()
                print('REACH')
                x==0
        if bs==0:
            input, output, result = getProfit()
            print(result)
            if(result<(0-0.05)):
                n()
                x==0
    n()


def n():
    x=2900
    y=1020
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    time.sleep(0.25)
    win32api.SetCursorPos((x+10, y+30))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x+10, y+30, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x+10, y+30, 0, 0)
    #main()
    main()





def main():
    flag = 2
    amount = 0.50
    while 1:
        if flag == 2:
            rs = getRsi()
            print(rs)
            if rs > 60:
                flag = 0
                print(rs)
                print('flag set to 0')
            if rs < 40:
                flag = 3
                print(rs)
                print('flag set to 3')

        if flag == 0:
            rs0 = getRsi()
            if rs0 < 60:
                flag = 1
                sell()
                print(rs0)
                print('flag set to 1')


        if flag == 3:
            rs3 = getRsi()
            if rs3 > 40:
                flag == 4
                buy()
                print(rs3)
                print('flag set to 3')

main()
