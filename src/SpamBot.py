import pyautogui
import os
import time
word = input("Which word do you want to spam: ")
i = input("How many times do you want to spam: ")
print("The program will now wait for 5 secs. In this time, open the social media app where you want to spam and select the textbox.")
time.sleep(5)
j = int(i)
k = 1

while k<=j:
	pyautogui.typewrite(word)
	pyautogui.press('enter')
	k=k+1


print("Thanks for using this program")
print("Operation completed successfully. The program will now exit.")
os.system("pause")
