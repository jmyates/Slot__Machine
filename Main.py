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

def makeSlot(drink_name, odds_name, slot_name, all_Drink, drink_Array):
	"""
	Purpose: Create the drink arrays for each slot using dictionaries for each drink and the addDrink function
	Parameters: drinkname- dict for specific drink, oddsname- array for that set odds in drink dict, 
	slotname- specific slot, allDrink- dict containt drink dicts, drinkArray- array with all drinks to compare with oddsnumbers
	"""
	for y in range (0,5):
		for x in range (0, all_Drink[drink_name][odds_name][y]):
			slot_name.addDrink(drink_Array[y])
			
##Checks version of Python, if it isn't python2, program tells user and quits
version_running = sys.version_info.major
version_needed = 2
if version_running != version_needed:
	print ("You are running Python " + str(version_running) + " Please switch to Python 2")
	exit()

##Gives name of player, and creates player object. Based on UID
name = pwd.getpwuid(os.getuid()).pw_name
print ("Hey there " + name)


##Uses BenCentra's drink API to pull user's credit value
##Request URL access, builds file, opens file
##If user does not have access to credit info, program tells user and quits
api = 'https://members.csh.rit.edu/~bencentra/webdrink/api/index.php?request=users/credits&api_key=&uid='+name
request = urllib2.Request(api)
opener = urllib2.build_opener()
file = opener.open(request)
user_data = simplejson.load(file)
status = user_data.get('status')
##For debugging/ checking error messages related to API Key
##print status
##print user_data
credits = user_data.get('data')
if status == False or credits == 'false':
	print 'You do not have access'
	exit()

##Creates player and prints credit amount
player1 = Player(name, int(credits))
player1.printCredits()
	##Creates the 5 Drink objects
coke = Drinks(50, "coke")
welchs = Drinks(75, "welchs")
ibc = Drinks(100, "ibc")
jolt = Drinks(125, "jolt")
bawls = Drinks(200, "bawls")
	
##Dictionaries for each drink with odds for each slot, winmessage, and credit value
##6th dictionary containing all drink dicts
##Odds numbers based on calculations in google docs spreadsheet
##drink_array and all 6 dicts used in makeSlot function
##Dicts also used in winCredit function when players wins or loses
dict_coke = {'odds1' : [5,4,3,2,1], 'odds2': [5,4,3,2,1], 'odds3' : [8,2,2,2,1], 'winmessage' : "You have won 50 credits", 'drinkobj': coke}
dict_welchs = {'odds1' : [5,4,3,2,1], 'odds2': [4,5,3,2,1], 'odds3' : [5,4,3,2,1], 'winmessage' : "You have won 75 credits", 'drinkobj': welchs}
dict_ibc = {'odds1' : [5,4,3,2,1], 'odds2': [2,2,7,2,2], 'odds3' : [3,4,4,2,3], 'winmessage' : "You have won 100 credits", 'drinkobj': ibc}
dict_jolt = {'odds1' : [5,4,3,2,1], 'odds2': [2,2,2,7,2], 'odds3' : [1,2,3,4,3], 'winmessage' : "You have won 125 credits", 'drinkobj': jolt}
dict_bawls = {'odds1' : [5,4,3,2,1], 'odds2': [1,1,1,1,11], 'odds3' : [4,4,3,3,1], 'winmessage' : "You have won 200 credits", 'drinkobj': bawls}
all_drink = {'coke': dict_coke, 'welchs': dict_welchs, 'ibc': dict_ibc, 'jolt': dict_jolt, 'bawls': dict_bawls}
drink_array = [coke, welchs, ibc, jolt, bawls]

##Keeps program running until player's credits are less than 50
while player1.credits >= 50:
	##Regex to see if the first character of user input is a 'y' for yes
	##Sets Sets value of regex to play
	##Uses this in the payCredit function, and then executes payCredits function
	##Prints user's credits so they can see the pay has occurred.
	cprint ("Would you like to play the slots?[y(es)/n(o)]", 'blue')
	play = raw_input()
	play_regex = re.match(r'^y',play,re.I)
	if play_regex:
		play = True
	else:
		play = False
	player1.payCredits(play)
	player1.printCredits()
	
	##Creates the 5 Drink objects
	coke = Drinks(50, "coke")
	welchs = Drinks(75, "welchs")
	ibc = Drinks(100, "ibc")
	jolt = Drinks(125, "jolt")
	bawls = Drinks(200, "bawls")
	
	##Dictionaries for each drink with odds for each slot, winmessage, and credit value
	##6th dictionary containing all drink dictionaries for makeSlot function
	##Odds numbers based on calculations in google docs spreadsheet
	dict__coke = {'odds1' : [5,4,3,2,1], 'odds2': [5,4,3,2,1], 'odds3' : [8,2,2,2,1], 'winmessage' : "You have won 50 credits", 'drinkobj': coke}
	dict_welchs = {'odds1' : [5,4,3,2,1], 'odds2': [4,5,3,2,1], 'odds3' : [5,4,3,2,1], 'winmessage' : "You have won 75 credits", 'drinkobj': welchs}
	dict_ibc = {'odds1' : [5,4,3,2,1], 'odds2': [2,2,7,2,2], 'odds3' : [3,4,4,2,3], 'winmessage' : "You have won 100 credits", 'drinkobj': ibc}
	dict_jolt = {'odds1' : [5,4,3,2,1], 'odds2': [2,2,2,7,2], 'odds3' : [1,2,3,4,3], 'winmessage' : "You have won 125 credits", 'drinkobj': jolt}
	dict_bawls = {'odds1' : [5,4,3,2,1], 'odds2': [1,1,1,1,11], 'odds3' : [4,4,3,3,1], 'winmessage' : "You have won 200 credits", 'drinkobj': bawls}
	all_drink = {'coke': dict_coke, 'welchs': dict_welchs, 'ibc': dict_ibc, 'jolt': dict_jolt, 'bawls': dict_bawls}
	drink_array = [coke, welchs, ibc, jolt, bawls]
	
	##Creates slot1
	##Executes makeSlot to add drinks ino slot1's array based on coke's odds1
	slot1 = Slot()
	makeSlot('coke', 'odds1', slot1, all_drink, drink_array)

	##For debugging
	##print (len(slot1.Drinks))
	
	##Pauses for suspense
	time.sleep(1)
	##Picks drink, assigns name, prints
	test1 = slot1.pickDrink()
	cprint (test1.getName(), test1.printName())
	
	##Creates slot2
	##Executes makeSlot to add drinks ino slot2's array based on first slot's drink using odds 2
	slot2 = Slot()
	makeSlot(test1.getName(), 'odds2', slot2, all_drink, drink_array)
	
	time.sleep(1)
	
	##Picks drink, assigns name, prints
	test2 = slot2.pickDrink()
	cprint (test2.getName(), test2.printName())
	
	##Creates slot3
	##Executes makeSlot to add drinks ino slot3's array based on first and second slots' drinks using odds 3
	##If the first two slots are not the same, then odds1 for coke are used
	slot3 = Slot()
	if test1 == test2:
		makeSlot(test2.getName(), 'odds3', slot3, all_drink, drink_array)
	else:
		makeSlot('coke', 'odds1', slot3, all_drink, drink_array)
	
	time.sleep(1)
	
	##Picks drink, assigns name, prints
	test3 = slot3.pickDrink()
	cprint (test3.getName(), test3.printName())
	
	##Pauses before printing win/ loss info
	time.sleep(1)
	
	##Checks for three in a row, prints win/ loss statement, add credits to account
	##If player loses, prints loss statement
	if test1.getName() == test2.getName() and test1.getName() == test3.getName():
		print all_drink[test1.getName()]['winmessage']
		you_won = all_drink[test1.getName()]['drinkobj'].getWinnings()
		player1.winCredits(you_won)
		
	else:
		print ("I'm sorry, you have lost. Please play again another time")
	
##Prints users credits so they know credits were added if they won, and to decide whehter to play again	
	player1.printCredits()
	
	##Hopefully "adds" credits when I have access (commented out until then)
	##'https://members.csh.rit.edu/~bencentra/webdrink/api/?api_key=&request=users/credits&uid=jmyates&value='+youwon

##Prints why player can not play when they do not have enough credits
print ("You do not have enough credits to play. Go talk to a Drink Admin to add more. :)")