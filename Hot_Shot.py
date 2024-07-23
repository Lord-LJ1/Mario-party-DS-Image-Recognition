import pyautogui 
import PIL       
import time


def run():

    pyautogui.MINIMUM_DURATION = 0.1
    pyautogui.PAUSE = 0.007

# top  left pyautogui.moveTo(900,900)
# down mid pyautogui.moveTo(950,850)
# down right pyautogui.moveTo(1025,850)

# top left sign pyautogui.moveTo(795,140)
# top mid pyautogui.moveTo(980,140)
# down right pyautogui.moveTo(1180,325)

# kamek (65, 219, 203)
# bowser (146, 243, 56)

    time_end = time.time() + 38

    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1

    while (time.time() < time_end):

        if  (pyautogui.pixelMatchesColor(795,140, (65, 219, 203), tolerance = 20) == True or pyautogui.pixelMatchesColor(795,140, (146, 243, 56), tolerance = 20) == True):
                pyautogui.mouseDown(1025,900)
                time.sleep(0.2)
                pyautogui.mouseUp()

        if  (pyautogui.pixelMatchesColor(980,140, (65, 219, 203), tolerance = 20) == True or pyautogui.pixelMatchesColor(980,140, (146, 243, 56), tolerance = 20) == True):
                pyautogui.mouseDown(950,900)
                time.sleep(0.2)
                pyautogui.mouseUp()


        if  (pyautogui.pixelMatchesColor(1175,142, (65, 219, 203), tolerance = 20) == True or pyautogui.pixelMatchesColor(1175,142, (146, 243, 56), tolerance = 20) == True):
                pyautogui.mouseDown(900,900)
                time.sleep(0.2)
                pyautogui.mouseUp()


        if  (pyautogui.pixelMatchesColor(795,326, (65, 219, 203), tolerance = 20) == True or pyautogui.pixelMatchesColor(795,326, (146, 243, 56), tolerance = 20) == True):
                pyautogui.mouseDown(1025,850)
                time.sleep(0.2)
                pyautogui.mouseUp()


        if  (pyautogui.pixelMatchesColor(980,326, (65, 219, 203), tolerance = 20) == True or pyautogui.pixelMatchesColor(980,326, (146, 243, 56), tolerance = 20) == True):
                pyautogui.mouseDown(950,850)
                time.sleep(0.2)
                pyautogui.mouseUp()


        if  (pyautogui.pixelMatchesColor(1175,331, (65, 219, 203), tolerance = 20) == True or pyautogui.pixelMatchesColor(1175,331, (146, 243, 56), tolerance = 20) == True):
                pyautogui.mouseDown(900,850)
                time.sleep(0.2)
                pyautogui.mouseUp()

