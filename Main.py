from Slot import Slot
from Drinks import Drinks
from Player import Player
from termcolor import cprint, colored
import sys
import re
import os 
import time
import urllib2
import simplejson
import pwd

##Checks version of Python
versionrunning = sys.version_info.major
versionneeded = 2

if versionrunning != versionneeded:
	print ("You are running Python " + str(versionrunning) + " Please switch to Python 2")
	exit()

##Gives name of player, and creates player object
name = pwd.getpwuid(os.getuid()).pw_name
print ("Hey there " + name)

api = 'https://members.csh.rit.edu/~bencentra/webdrink/api/index.php?request=users/credits&api_key=APIKEY&uid='+name
request = urllib2.Request(api)
opener = urllib2.build_opener()
file = opener.open(request)
userdata = simplejson.load(file)
##print userdata
status = userdata.get('status')
print status
credits = userdata.get('data')
if status == False or credits == 'false':
	print 'You do not have access'
	exit()


player1 = Player(name, int(credits))

print ('You have ' + str(player1.credits) + ' credits')
##Keeps program running until player's credits are less than 50
while 1==1 and player1.credits >= 50:
	##Regex to see if the first character of user input is a 'y' for yes
	cprint ("Would you like to play the slots?[y(es)/n(o)]", 'blue')
	play = raw_input()
	playregex = re.match(r'^y',play,re.I)

	if  playregex:
		play = True
	else:
		play = False

	player1.payCredits(play)

	print ('You have ' + str(player1.credits) + ' credits')
	
	##Creates the 5 Drink objects
	coke = Drinks(50, "coke")
	welchs = Drinks(75, "welchs")
	ibc = Drinks(100, "ibc")
	jolt = Drinks(125, "jolt")
	bawls = Drinks(200, "bawls")

	##Creates first slot
	##for loop to add drinks
	slot1 = Slot()
	for x in range (0, 5):
		slot1.addDrink(coke)
	for x in range (0, 4):
		slot1.addDrink(welchs)
	for x in range (0, 3):
		slot1.addDrink(ibc)
	for x in range (0, 2):
		slot1.addDrink(jolt)
	slot1.addDrink(bawls)

	#For debugging
	#print (len(slot1.Drinks))
	
	##Pauses 2 seconds for suspense
	time.sleep(2)
	##Picks drink, assigns name, prints
	test1 = slot1.pickDrink()
	cprint (test1.getName(), test1.printName())
	
	##Creates slot 2
	slot2 = Slot()
	
	##Numbers are based on a google docs spreadsheet
	if test1.getName() == "bawls":
		for x in range (0, 11):
			slot2.addDrink(bawls)
		slot2.addDrink(coke)
		slot2.addDrink(welchs)
		slot2.addDrink(ibc)
		slot2.addDrink(jolt)

	elif test1.getName() == "coke":
		for x in range (0,5):
			slot2.addDrink(coke)
		for x in range (0, 4):
			slot2.addDrink(welchs)
		for x in range (0, 3):
			slot2.addDrink(ibc)
		for x in range (0, 2):
			slot2.addDrink(jolt)
		slot2.addDrink(bawls)

	elif test1.getName() == "welchs":
		for x in range (0,5):
			slot2.addDrink(welchs)
		for x in range (0, 4):
			slot2.addDrink(coke)
		for x in range (0, 3):
			slot2.addDrink(ibc)
		for x in range (0, 2):
			slot2.addDrink(jolt)
		slot2.addDrink(bawls)

	elif test1.getName() == "ibc":
		for x in range (0,7):
			slot2.addDrink(ibc)
		for x in range (0, 2):
			slot2.addDrink(coke)
		for x in range (0, 2):
			slot2.addDrink(welchs)
		for x in range (0, 2):
			slot2.addDrink(jolt)
		for x in range (0,2):
			slot2.addDrink(bawls)

	elif test1.getName() == "jolt":
		for x in range (0,7):
			slot2.addDrink(jolt)
		for x in range (0, 2):
			slot2.addDrink(coke)
		for x in range (0, 2):
			slot2.addDrink(welchs)
		for x in range (0, 2):
			slot2.addDrink(ibc)
		for x in range (0,2):
			slot2.addDrink(bawls)
			
	else:
		print ("Slot machine broken. Report to Jamie or Drink Admin")
		exit()
	
	time.sleep(2)
	
	##Picks drink, assigns name, prints
	test2 = slot2.pickDrink()
	cprint (test2.getName(), test2.printName())
	
	##Creates third slot
	slot3 = Slot()
	if test2.getName() == test1.getName() and test2.getName() == "bawls":
		slot3.addDrink(bawls)
		for x in range (0,4):
			slot3.addDrink(coke)
		for x in range (0,4):
			slot3.addDrink(welchs)
		for x in range (0,3):
			slot3.addDrink(ibc)
		for x in range (0,3):
			slot3.addDrink(jolt)
			
	elif test2.getName() == test1.getName() and test2.getName() == "coke":
		for x in range (0,8):
			slot3.addDrink(coke)
		for x in range (0,2):
			slot3.addDrink(welchs)
		for x in range (0,2):
			slot3.addDrink(ibc)
		for x in range (0,2):
			slot3.addDrink(jolt)
		slot3.addDrink(bawls)
		
	elif test2.getName() == test1.getName() and test2.getName() == "welchs":
		for x in range (0,5):
			slot3.addDrink(coke)
		for x in range (0,4):
			slot3.addDrink(welchs)
		for x in range (0,3):
			slot3.addDrink(ibc)
		for x in range (0,2):
			slot3.addDrink(jolt)
		slot3.addDrink(bawls)
		
	elif test2.getName() == test1.getName() and test2.getName() == "ibc":
		for x in range (0,3):
			slot3.addDrink(coke)
		for x in range (0,3):
			slot3.addDrink(welchs)
		for x in range (0,4):
			slot3.addDrink(ibc)
		for x in range (0,2):
			slot3.addDrink(jolt)
		for x in range (0,3):
			slot3.addDrink(bawls)
			
	elif test2.getName() == test1.getName() and test2.getName() == "jolt":
		for x in range (0,3):
			slot3.addDrink(coke)
		for x in range (0,2):
			slot3.addDrink(welchs)
		for x in range (0,3):
			slot3.addDrink(ibc)
		for x in range (0,4):
			slot3.addDrink(jolt)
		for x in range (0,3):
			slot3.addDrink(bawls)
		
	elif test2.getName() != test1.getName():
		for x in range (0,3):
			slot3.addDrink(coke)
		for x in range (0,3):
			slot3.addDrink(welchs)
		for x in range (0,3):
			slot3.addDrink(ibc)
		for x in range (0,3):
			slot3.addDrink(jolt)
		for x in range (0,3):
			slot3.addDrink(bawls)
			
	else:
		print ("Slot machine broken. Report this to Jamie or Drink Admin")
		exit()
		
	time.sleep(2)
	
	##Picks drink, assigns name, prints
	test3 = slot3.pickDrink()
	cprint (test3.getName(), test3.printName())

	##Checks for three in a row, prints win/ loss statement, add credits to account
	if test1.getName() == test2.getName() and test1.getName() == test3.getName() and test1.getName() == "coke":
		print ("Congratulations you win 50 Credits!")
		youwon = coke.getWinnings()
		player1.winCredits(youwon)
		
	elif test1.getName() == test2.getName() and test1.getName()== test3.getName() and test1.getName() == "welchs":
		print ("Congratulations you win 75 Credits!")
		youwon = welchs.getWinnings()
		player1.winCredits(youwon)
		
	elif test1.getName() == test2.getName() and test1.getName() == test3.getName() and test1.getName() == "ibc":
		print ("Congratulations you win 100 Credits!")
		youwon = ibc.getWinnings()
		player1.winCredits(youwon)
		
		
	elif test1.getName() == test2.getName() and test1.getName() == test3.getName() and test1.getName() == "jolt":
		print ("Congratulations you win 125 Credits!")
		youwon = jolt.getWinnings()
		player1.winCredits(youwon)
		
	elif test1.getName() == test2.getName() and test1.getName() == test3.getName() and test1.getName() == "bawls":
		print ("Congratulations you win 200 Credits!")
		youwon = bawls.getWinnings()
		player1.winCredits(youwon)
		
	else:
		print ("I'm sorry, you have lost. Please play again another time")
		
	print ("You have " + str(player1.credits) + " credits")

##Prints why player can not play when they do not have enough credits
print ("You do not have enough credits to play. Go talk to a Drink Admin to add more. :)")