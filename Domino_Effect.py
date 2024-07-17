import pyautogui 
import PIL       
import time


def run():

    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.PAUSE = 0.007

    time_end = time.time() + 30

    i=0
    while (i<10):
        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        i=i+1

    button_list = ["Domino_Effect_A","Domino_Effect_B","Domino_Effect_X","Domino_Effect_Y"]
    conversion_list = ["l","k","i","j"]
    index = 0
    button = -1
    finish = False
    time.sleep(6)
    print("start")
    while (finish == False):
        while (button == -1):
            try:
                pyautogui.locateOnScreen(f'{button_list[index]}.PNG',region=(1040,630,45,55), confidence=.95)
                button = conversion_list[index]
            except Exception as e:
                if(index < 3):
                    index=index+1
                else:
                    index = 0
            if (button != -1):
                i=0    
                while (i<8):
                    pyautogui.keyDown(button)
                    pyautogui.keyUp(button)
                    i=i+1
                button = -1
                
            try:
                temp=pyautogui.pixelMatchesColor(700, 1000, (0, 0, 0), tolerance = 0)                
                if (temp == True):
                    finish = True
                    button = 5
            except Exception as e:
                finish = False
