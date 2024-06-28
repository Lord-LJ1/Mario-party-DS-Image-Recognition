import pyautogui # interact with screen
import PIL          # take/read screenshots
import time

# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

minigameScript = ["Rail_Riders"]
minigameScriptIndex = 0
index = int

#temp input
def tempInput(index):
    index= 0
    while (index < 0 or index > len(minigameScript) - 1):
        index = int(input("input index of minigame: "))
    return index

if __name__ == "__main__":

    time.sleep(3)

    #imports the minigame scripts
    for script in minigameScript:
        exec(f"import {script}")

    #temp input system

    minigameScriptIndex=tempInput(index)

    exec(f"{minigameScript[minigameScriptIndex]}.run()")
















#controls for ds
# d-pad: W, A, S, D
# buttons: P, L, ;, '
# triggers: L-shift, R-shift
# mic: Space

#Size(width=1920, height=1080)
# corners, mid and 3rds
#top
#pyautogui.moveTo(630,45)
#pyautogui.moveTo(960,290)
#pyautogui.moveTo(1290,535)
#bot
#pyautogui.moveTo(630,545)
#pyautogui.moveTo(960,790)
#pyautogui.moveTo(1290,1035)

