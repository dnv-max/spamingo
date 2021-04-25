import pyautogui , time
a = $1
b = $2
c = $3
d = $4
time.sleep(a)
for z in range(1,b):
  pyautogui.typewrite(d)
  pyautogui.press("enter")
  time.sleep(d)
