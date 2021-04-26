import pyautogui
import time
print(" _  ___           _                 _       _     ")
print("| |/ (_)_ __   __| | __ _  ___ __ _| |_ ___| |__  ")
print("| ' /| | '_ \ / _` |/ _` |/ __/ _` | __/ __| '_ \ ")
print("| . \| | | | | (_| | (_| | (_| (_| | || (__| | | |")
print("|_|\_\_|_| |_|\__,_|\__,_|\___\__,_|\__\___|_| |_|")
a = int(input("enter the number of seconds to start the script : "))
b = int(input("number of messages to spam : "))
c = str(input("enter the message to spam : "))
d = int(input("enter the number of seconds between each  message (keep it 0 for fastest spam)  : "))
time.sleep(a)
for z in range(1,b+1):
  pyautogui.typewrite(c)
  pyautogui.press("enter")
  time.sleep(d)
