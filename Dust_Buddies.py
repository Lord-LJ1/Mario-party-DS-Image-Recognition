import pyautogui 
import PIL       
import time


def run():

    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.PAUSE = 0.01


    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1

    time.sleep(4.5)

    i=0
    while (i<10):
        print("w")
        pyautogui.keyDown("w")
        pyautogui.keyDown("a")
        i=i+1

    Fin = False

    while (Fin == False):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        print("1")
        if (pyautogui.pixelMatchesColor(660,670, (109, 45, 13),tolerance=20)== True):
            i=0
            while (i<10):
                print(pyautogui.pixel(660,650))
                pyautogui.keyUp("a")
                pyautogui.keyDown("d")
            i=i+1
        try:
            pyautogui.locateOnScreen('Dust_Buddies_Fin.PNG', region=(840,750,240,50), confidence=.95,grayscale=True)
            Fin=True
            print("3")
        except Exception as e:
            Fin=False

    i=0
    while (i<10):
        pyautogui.keyUp("w")
        pyautogui.keyUp("a")
        pyautogui.keyUp("d")
        i=i+1
