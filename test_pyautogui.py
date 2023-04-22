# pip install pyautogui
# Pillow 에러 발생시 : pip install Pillow --upgrade
import pyautogui
import time
import pyperclip

# 1차 - 좌표 확인
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

time.sleep(3)
pyautogui.moveTo(1259,542)
while True:
    pyautogui.doubleClick()