import pyautogui
import time

# Current size of display
#print(pyautogui.size())

# Current position of the mouse cursor
print(pyautogui.position())

# Mouse movement
pyautogui.moveTo(20, 268, 2) # x:100, y:200 으로 2초동안 이동하라

# Mouse Click
pyautogui.click() # Normal click
time.sleep(1) # Time stop for 1 sec

# Mouse right click
#pyautogui.click(button = "right")

# Mouse double click
pyautogui.moveTo(327, 211, 2)
pyautogui.doubleClick()

# Mouse Drag
pyautogui.moveTo(816, 200, 2)
pyautogui.dragTo(539, 400, 2, button="left")

#Mouse Scroll
pyautogui.scroll(1) # Up
pyautogui.scroll(-2) # Down
pyautogui.scroll(-3, x=50, y=366) # Move to 50, 366, and scroll up 3 clicks