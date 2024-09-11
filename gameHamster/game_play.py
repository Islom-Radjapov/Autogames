import pyautogui
import time
from location import list
time.sleep(5)
print("start")
def play(x1, y1):
    pyautogui.mouseDown(1222,907)
    pyautogui.moveTo(x1, y1)
    #time.sleep(0.03)
    pyautogui.mouseUp(x1,y1)
    #time.sleep(0.03)
while True:
    for x in list:
        play(x[0], x[1])
        pyautogui.click(1111, 860)
        pyautogui.click(1151, 406)
        time.sleep(0.03)
        pyautogui.click(1326, 934)
