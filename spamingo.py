import pyautogui
import time
sleep = time.sleep
typewrite = pyautogui.typewrite
press = pyautogui.press
a = int(input("enter the number of seconds to start the script : "))
b = int(input("number of messages to spam : "))
c = str(input("enter the message to spam : "))
d = int(input("enter the number of seconds between each  message (keep it 0 for fastest spam)  : "))
sleep(a)
for z in range(1,b):
  typewrite(c)
  press("enter")
  sleep(d)
