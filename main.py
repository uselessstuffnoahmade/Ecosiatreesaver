import time
import pyautogui
while True:
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')
    pyautogui.write('Iphone 14')
    pyautogui.press('enter')
    time.sleep(2.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')