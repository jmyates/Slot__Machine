import random
class Slot:

	def __init__ (self):
		self.Drinks = []

##Adds drinks to array		
	def addDrink (self, drink):
		self.Drinks.append(drink)

##Selects random drink from array		
	def pickDrink (self):
		rand = random.randint(0, 14)
		return self.Drinks[rand]
		