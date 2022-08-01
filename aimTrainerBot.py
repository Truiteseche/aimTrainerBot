"""
Game link : https://aimtrainer.io/challenge
Run the python script
"""

import time
import keyboard
import pyautogui

time.sleep(1)
userInput = pyautogui.confirm(
    "Welcome to aimTrainerBot, a bot made for aim trainer.\nFollow the procedure :"
    "\n1. Visit this link : https://aimtrainer.io/challenge/"
    "\n2. Launch the project by clicking on the green flag"
    "\n3. Press 'OK' to run the script"
    "\nThe bot plays independently. Press 'alt' button to pause/launch the process, press 'space' to stop the process...")

if userInput == "OK":
    # variables
    pyautogui.PAUSE = 0
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    botRunning = True
    botToggle = True
    FPS = 0
    targetR = 255
    targetG = 87
    targetB = 34
    screenShotRegion = (553, 302, 797, 476)
    # screenShotRegion = (0, 0, 1920, 1080)
    imgResearchStep = 5
    # (x=553, y=302)
    # Point(x=1350, y=778)

    # screenshot demo : pyautogui.screenshot("screenshot.png", region=screenShotRegion)

    # main loop
    while botRunning:
        # main script
        if botToggle:
            img = pyautogui.screenshot(region=screenShotRegion)
            imgX = 0
            imgY = 0
            while imgY < screenShotRegion[3]:
                if img.getpixel((imgX, imgY))[0] == targetR:
                    pyautogui.moveTo(screenShotRegion[0] + imgX, screenShotRegion[1] + imgY)
                    pyautogui.click()
                    break
                else:
                    imgX += imgResearchStep
                    if imgX > screenShotRegion[2]-1:
                        imgX = 0
                        imgY += imgResearchStep
                # print((imgX, imgY))

            # FPS manager
            if not FPS == 0:
                time.sleep(1 / FPS)

        try:
            if keyboard.is_pressed('alt'):
                botToggle = not botToggle
                while keyboard.is_pressed('alt'):
                    continue
            if keyboard.is_pressed('space'):
                botRunning = False
        except:
            print("Error : Something went wrong...")
            break
