import pyautogui # interact with screen
import PIL          # take/read screenshots
import time

# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

minigameScript = ["Rail_Riders","Study_Fall"]
minigameScriptIndex = int
index = int

#check for minigames
def MinigameIndex():
    index = 0
    while (index < len(minigameScript)):
        try:
            temp=pyautogui.locateOnScreen(f'{minigameScript[index]}.PNG', region=(650,50,600,50), confidence=.95)
            return(index)
        except Exception as e:
            index=index+1
    #universal not found
    index = -1 
    return index



if __name__ == "__main__":

    #imports the minigame scripts
    for script in minigameScript:
        exec(f"import {script}")

    x=1

    while (x==1):


        minigameScriptIndex=MinigameIndex()

        time.sleep(2)

        if (minigameScriptIndex > -1):
            print(f"{minigameScript[minigameScriptIndex]}")
            exec(f"{minigameScript[minigameScriptIndex]}.run()")








#{minigameScript[index]}



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

