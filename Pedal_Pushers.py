import pyautogui 
import PIL       
import time

def mash():
    pyautogui.keyDown("l")
    pyautogui.keyUp("l")
    pyautogui.keyDown("a")
    pyautogui.keyUp("a")


def run():

    pyautogui.MINIMUM_DURATION = 0.1
    pyautogui.PAUSE = 0.1

    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1

    while (pyautogui.pixelMatchesColor(648,430, (98, 37, 174), tolerance = 40)==False):
        mash()
    pyautogui.MINIMUM_DURATION = 0.1
    pyautogui.PAUSE = 0.1
    while (pyautogui.pixelMatchesColor(648,412, (98, 37, 174), tolerance = 40)==False):
        mash()
    pyautogui.MINIMUM_DURATION = 0.05
    pyautogui.PAUSE = 0.05
    while (pyautogui.pixelMatchesColor(648,347, (98, 37, 174), tolerance = 40)==False):
        mash()
    pyautogui.MINIMUM_DURATION = 0.1
    pyautogui.PAUSE = 0.1
    while (pyautogui.pixelMatchesColor(648,273, (98, 37, 174), tolerance = 40)==False):
        mash()
    pyautogui.MINIMUM_DURATION = 0.05
    pyautogui.PAUSE = 0.05
    while (pyautogui.pixelMatchesColor(648,164, (98, 37, 174), tolerance = 40)==False):
        mash()
    pyautogui.MINIMUM_DURATION = 0.1
    pyautogui.PAUSE = 0.1
    while (pyautogui.pixelMatchesColor(648,146, (98, 37, 174), tolerance = 40)==False):
        mash()
    pyautogui.MINIMUM_DURATION = 0.05
    pyautogui.PAUSE = 0.05
    mash()
    mash()
    mash()
        