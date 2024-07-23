import pyautogui 
import PIL       
import time

def run():

    pyautogui.MINIMUM_DURATION = 0.000000000000000000001
    pyautogui.PAUSE = 0.000000000000000000001

    time_end = time.time() + 20

    while (time.time() < time_end):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
