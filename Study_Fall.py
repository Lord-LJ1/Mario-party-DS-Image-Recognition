import pyautogui 
import PIL       
import time


def run():
    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.PAUSE = 0.01

    i=0
    while (i<10):
        pyautogui.keyDown("'")
        pyautogui.keyUp("'")
        i=i+1

    check = False

    time.sleep(3)

    #checks if red line has reached position (latest it can be pressed)
    while(check == False):
        check = pyautogui.pixelMatchesColor(650, 340, (241, 40, 40), tolerance = 20)
        print(check)

    i=0
    while (i<10):
        pyautogui.keyDown("'")
        pyautogui.keyUp("'")
        i=i+1

