a = int(input("enter the number of seconds to start the script : "))
b = int(input("number of messages to spam : "))
c = str(input("enter the message to spam"))
d = int(input("enter the number of seconds between each  message (keep it 0 for fastest spam)  : "))
time.sleep(a)
for z in range(1,b):
  pyautogui.typewrite(d)
  pyautogui.press("enter")
  time.sleep(d)
