import pyautogui 


def run():
    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1