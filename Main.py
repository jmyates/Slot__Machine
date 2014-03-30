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

def makeSlot(drinkname, oddsname, slotname):
	for y in range (0,5):
		for x in range (0, alldrink[drinkname][oddsname][y]):
			slotname.addDrink(drinkarray[y])
			
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
#Know what JSON is -JH
userdata = simplejson.load(file)
##print userdata
status = userdata.get('status')
print status
credits = userdata.get('data')
if status == False or credits == 'false':
	print 'You do not have access'
	exit()


player1 = Player(name, int(credits))

player1.printCredits()
##Keeps program running until player's credits are less than 50
while player1.credits >= 50:
	##Regex to see if the first character of user input is a 'y' for yes
	cprint ("Would you like to play the slots?[y(es)/n(o)]", 'blue')
	play = raw_input()
	playregex = re.match(r'^y',play,re.I)

	if  playregex:
		play = True
	else:
		play = False

	player1.payCredits(play)

	#Elimiate these duplicates with function in Player - JH XX
	player1.printCredits()
	
	
	#Dictionary allDrinks of drinkName - [[odds1, odds2, odds3], winMessage] - JH 
	
	dictcoke = {'odds1' : [5,4,3,2,1], 'odds2': [5,4,3,2,1], 'odds3' : [8,2,2,2,1], 'winMessage' : "You have won 50 credits"}
	dictwelchs = {'odds1' : [5,4,3,2,1], 'odds2': [4,5,3,2,1], 'odds3' : [5,4,3,2,1], 'winMessage' : "You have won 75 credits"}
	dictibc = {'odds1' : [5,4,3,2,1], 'odds2': [2,2,7,2,2], 'odds3' : [3,4,4,2,3], 'winMessage' : "You have won 100 credits"}
	dictjolt = {'odds1' : [5,4,3,2,1], 'odds2': [2,2,2,7,2], 'odds3' : [1,2,3,4,3], 'winMessage' : "You have won 125 credits"}
	dictbawls = {'odds1' : [5,4,3,2,1], 'odds2': [1,1,1,1,11], 'odds3' : [4,4,3,3,1], 'winMessage' : "You have won 200 credits"}
	alldrink = {'coke': dictcoke, 'welchs': dictwelchs, 'ibc': dictibc, 'jolt': dictjolt, 'bawls': dictbawls}
	
	##Creates the 5 Drink objects
	coke = Drinks(50, "coke")
	welchs = Drinks(75, "welchs")
	ibc = Drinks(100, "ibc")
	jolt = Drinks(125, "jolt")
	bawls = Drinks(200, "bawls")

	drinkarray = [coke, welchs, ibc, jolt, bawls]
	
	#Abstract slot makin into a Function to abstract out slot making - JH
	#Make for loops for these - JH
	#Put numbers in array as well - JH
	slot1 = Slot()
	makeSlot('coke', 'odds1', slot1)

	##For debugging
	##print (len(slot1.Drinks))
	
	##Pauses for suspense
	time.sleep(1)
	##Picks drink, assigns name, prints
	test1 = slot1.pickDrink()
	cprint (test1.getName(), test1.printName())
	
	##Creates slot 2
	slot2 = Slot()
	
	#computeFuntion(allDrinks[test1.getName()][1]) - Missleading, know what to do - JH
	##Numbers are based on a google docs spreadsheet
	
	makeSlot(test1.getName(), 'odds2', slot2)
	
	time.sleep(1)
	
	##Picks drink, assigns name, prints
	test2 = slot2.pickDrink()
	cprint (test2.getName(), test2.printName())
	
	##Creates third slot
	slot3 = Slot()
	makeSlot(test2.getName(), 'odds3', slot3)
		
	time.sleep(1)
	
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
		
	player1.printCredits()

##Prints why player can not play when they do not have enough credits
print ("You do not have enough credits to play. Go talk to a Drink Admin to add more. :)")