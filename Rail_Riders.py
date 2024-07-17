import pyautogui 
import PIL       
import time


def run():

    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.PAUSE = 0.007

    time_end = time.time() + 30

    #loop is bc somtimes press would drop, cant have higher duration
    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1


    while (time.time() < time_end):
        pyautogui.mouseUp(680,1000)
        pyautogui.dragTo(1240,570,0.1,button="left")


