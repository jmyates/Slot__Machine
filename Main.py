from Slot import Slot
from Drinks import Drinks
from Player import Player

name = raw_input('Who are you')

player1 = Player(name, 100)

print 'You have ' + str(player1.credits) + ' credits'

play = raw_input('Would you like to play the slots?')
if len(play) == 3:
	play = True
else:
	play = False

player1.payCredits(play)

print 'You have ' + str(player1.credits) + ' credits'

coke = Drinks(1, "coke")
welchs = Drinks(2, "welchs")
ibc = Drinks(10, "ibc")
jolt = Drinks(50, "jolt")
bawls = Drinks(100, "bawls")

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
#print len(slot1.Drinks)

test1 = slot1.pickDrink()
print test1.getName()

slot2 = Slot()
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
	print "Slot machine broken. Report to Jamie or Drink Admin"
	exit()

test2 = slot2.pickDrink()
print test2.getName()

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
	print "Slot machine broken. Report to Jamie or Drink Admin"
	exit()
	
test3 = slot3.pickDrink()
print test3.getName()