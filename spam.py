import pyautogui, time, os, random
directory = "Scripts Data"

i = 0
while i<20:
	time.sleep(5)
	filename = random.choice(os.listdir("Scripts"))
	f = open(os.path.join(directory, filename),"r")
	for word in f:
	    pyautogui.typewrite(word)
	    pyautogui.press("enter")
	    time.sleep(5)