from PIL import ImageGrab, ImageOps
import pyautogui
import time
from  numpy import *

class Coordinates():
    replayBtn = (674, 180)
    dinosaur = (442, 186)
    # 177 = x coordinate to check for obstacles
    # y coordinate= 212

def restartGame():
    pyautogui.click(Coordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')

def imageGrab():
    # box is the area where any obstacles is detected
    box = (489, 188, 524, 209)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if imageGrab() != 982:
            pressSpace()
            time.sleep(0.1)

restartGame()
time.sleep(1)
pressSpace()
main()
