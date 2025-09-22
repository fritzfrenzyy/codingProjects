import keyboard
import pyautogui

y = 1141

while True:
    key = keyboard.read_key()
    if key == "esc":
         break
    if key == "a":
        pyautogui.moveTo(811,y)
        pyautogui.click()
    if key == "s":
        pyautogui.moveTo(966,y)
        pyautogui.click()
    if key == "d":
        pyautogui.moveTo(y,y)
        pyautogui.click()
    if key == "f":
        pyautogui.moveTo(1292,y)
        pyautogui.click()
    if key == "g":
        pyautogui.moveTo(1488,y)
        pyautogui.click()
    if key == "t":
        pyautogui.moveTo(1639,y)
        pyautogui.click()
    if key == "y":
        pyautogui.moveTo(1796,y)
        pyautogui.click()
    if key == "h":
        pyautogui.moveTo(1959,y)
        pyautogui.click()
    if key == "j":
        pyautogui.moveTo(2130,y)
        pyautogui.click()
    if key == "k":
        pyautogui.moveTo(2286,y)
        pyautogui.click()
    if key == "l":
        pyautogui.moveTo(2470,y)
        pyautogui.click()
    if key == ";":
        pyautogui.moveTo(2616,y)
        pyautogui.click()