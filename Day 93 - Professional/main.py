import pyautogui
import keyboard
from PIL import Image
from time import sleep
import numpy

# https://elgoog.im/t-rex/

# print(pyautogui.position())  # (500, 395) (500, 405)
# pyautogui.screenshot("temp.png", region=(500, 395, 80, 10))  # use this to get the region
# exit()

print("Program started!")
print("Get ready! The program will start in...")
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("Started... Press or Hold 's' to stop the program!")
pyautogui.press("space")

while True:  # 681 points
    img = pyautogui.screenshot("temp.png", region=(500, 395, 80, 10))
    img_array = numpy.array(img)
    grey_pixels = len(numpy.where(numpy.all(img_array == (83, 83, 83), axis=-1))[1])
    if grey_pixels:
        pyautogui.press("space")
