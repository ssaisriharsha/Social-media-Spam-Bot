import pyautogui
import os
import time
while True:
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

	print("Operation completed successfully.")
	repetion = input("Do you want to use the program again(Y/N): ").upper()
	if repetion == "Y":
		continue
	elif repetion == "N":
		print("Thanks for using this program")
		print("The program will now exit.")
		time.sleep(2)
		break
	else:
		print("You have to enter Y/N only.")
		print("The program will now exit.")
		time.sleep(2)
		break
