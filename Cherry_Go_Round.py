import pyautogui 
import PIL       
import time

def run():

    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.PAUSE = 0.007

    time_end = time.time() + 18

    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1

    time.sleep(6)

    pyautogui.moveTo(1050,800)
    pyautogui.mouseDown()

    while (time.time() < time_end):
        pyautogui.moveTo(965,700)
        pyautogui.moveTo(880,800)
        pyautogui.moveTo(965,900)
        pyautogui.moveTo(1050,800)