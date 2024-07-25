import pyautogui 
import PIL       
import time

def run():

    pyautogui.MINIMUM_DURATION = 0.1
    pyautogui.PAUSE = 0.1

    time_end = time.time() + 45

    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1

    while (time.time() < time_end):
        if (pyautogui.pixelMatchesColor(730,180, (150, 146, 101))== True):
            print(pyautogui.pixel(730,380))
            if (pyautogui.pixelMatchesColor(730,380, (35, 123, 199),tolerance = 20)== True):
               print("1")
               pyautogui.moveTo(730,800)
               time.sleep(0.1)
               pyautogui.mouseDown()
               time.sleep(0.1)
               pyautogui.mouseUp()
            elif  (pyautogui.pixelMatchesColor(730,380, (15, 84, 146),tolerance = 20)== True):
               print("2")
               pyautogui.moveTo(1230, 800)
               time.sleep(0.1)
               pyautogui.mouseDown()
               time.sleep(0.1)
               pyautogui.mouseUp()
        if (pyautogui.pixelMatchesColor(730,180, (150, 146, 101))== False):
            print("false")