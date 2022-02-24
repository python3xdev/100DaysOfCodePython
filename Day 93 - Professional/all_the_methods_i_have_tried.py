import pyautogui
import keyboard
from PIL import Image
from time import sleep

import numpy

# https://elgoog.im/t-rex/

# many values will need changing depending on what screen size you have!

print("Program started!")
print("Get ready! The program will start in...")
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("Started... Press or Hold 's' to stop the program!")


def press_space():
    # pyautogui.keyDown("space")
    # sleep(0.1)
    # pyautogui.keyUp("space")
    pyautogui.press("space")


press_space()

view_distance = 85  # some methods use this
jumps_owed = 0  # and this
play = True
while play:
    # The method below reaches ~681 points
    img = pyautogui.screenshot("temp.png", region=(500, 395, 80, 10))
    img_array = numpy.array(img)
    grey_pixels = len(numpy.where(numpy.all(img_array == (83, 83, 83), axis=-1))[1])
    if grey_pixels:
        pyautogui.press("space")


# most methods below use these variables: (remember! these values will vary depending on your screen size)
# area1 = pyautogui.pixelMatchesColor(590, 410, (83, 83, 83))
# area2 = pyautogui.pixelMatchesColor(464, 405, (83, 83, 83))

# - - - - - - - - - - - - - - - - - - - - - - -

# The method below reaches ~680 points
# area2 = pyautogui.pixelMatchesColor(463, 405, (83, 83, 83), tolerance=50)
# img = pyautogui.screenshot(region=(500, 380, 80, 30))
# img_array = numpy.array(img)
# grey_pixels = len(numpy.where(numpy.all(img_array == (83, 83, 83), axis=-1))[1])
# # print(jumps_owed)
# if grey_pixels and area2:
#     jumps_owed += 1
# if area2:
#     while jumps_owed:
#         press_space()
#         jumps_owed -= 1

# - - - - - - - - - - - - - - - - - - - - - - -

# The method below reaches ~318 points
# img = pyautogui.screenshot(region=(500, 380, 70, 30))
# img_array = numpy.array(img)
# print(len(numpy.where(numpy.all(img_array == (83, 83, 83), axis=-1))[1]))
# if len(numpy.where(numpy.all(img_array == (83, 83, 83), axis=-1))[1]):
#     press_space()

# - - - - - - - - - - - - - - - - - - - - - - -

# The method below reaches ~256 points
# area2 = pyautogui.pixelMatchesColor(463, 405, (83, 83, 83))
# img = pyautogui.screenshot(region=(500, 380, view_distance, 30))
# img_array = numpy.array(img)
# grey_pixels = len(numpy.where(numpy.all(img_array == (83, 83, 83), axis=-1))[1])
# # print(jumps_owed)
# if grey_pixels and area2:
#     jumps_owed += 1
# if area2:
#     while jumps_owed:
#         press_space()
#         jumps_owed -= 1
#
# if view_distance <= 125:
#     view_distance += 0.1
# # print(view_distance)
# print(jumps_owed)
# if pyautogui.pixelMatchesColor(707, 363, (83, 83, 83)):  # this restarts the game if the game is over
#     view_distance = 80
#     press_space()

# - - - - - - - - - - - - - - - - - - - - - - -

# The method below reaches ~245 points
# if area1:
#     jumps_owed += 1
# if area2:
#     while jumps_owed:
#         press_space()
#         jumps_owed -= 1

# - - - - - - - - - - - - - - - - - - - - - - -

# The method below reaches ~ 163 points
# for pixel in range(590, 491, -10):
#     area1 = pyautogui.pixelMatchesColor(pixel, 409, (83, 83, 83), tolerance=50)
#     if area1:
#         while not area2:
#             area2 = pyautogui.pixelMatchesColor(463, 405, (83, 83, 83), tolerance=50)
#         print("JUMP")
#         press_space()
#         break

# - - - - - - - - - - - - - - - - - - - - - - -

# The method below reaches ~160 points
# if area1:
#     while not area2:
#         area2 = pyautogui.pixelMatchesColor(463, 405, (83, 83, 83), tolerance=50)
#     if area2:
#         press_space()

# - - - - - - - - - - - - - - - - - - - - - - -

# This is optional, it will restart the game if you lose...
# if pyautogui.pixelMatchesColor(707, 363, (83, 83, 83)):  # this restarts the game if the game is over
#     press_space()
