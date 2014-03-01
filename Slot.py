import random
class Slot:

	def __init__ (self):
		self.Drinks = []
	
	def addDrink (self, drink):
		self.Drinks.append(drink)
		
	def pickDrink (self):
		rand = random.randint(0, 14)
		return self.Drinks[rand]
		