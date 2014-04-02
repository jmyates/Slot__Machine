import random
class Slot:

	def __init__ (self):
		self.Drinks = []

##Adds drinks to array		
	def addDrink (self, drink):
		"""
		Purpose: Add drinks into an array to selected from in future
		Parameters: drink (name of drink)
		"""
		self.Drinks.append(drink)

##Selects random drink from array		
	def pickDrink (self):
		"""
		Purpose: Randomly selects drink from the drink array created before
		Returnn: drink that was randomly selected
		"""
		rand = random.randint(0, len(self.Drinks) - 1)
		return self.Drinks[rand]
		