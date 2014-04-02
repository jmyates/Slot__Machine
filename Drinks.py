class Drinks:

	def __init__ (self, winnings, name):
		self.winnings = winnings
		self.name = name
	
##Returns name of drink	
	def getName (self):
		"""
		Purpose: Return drink name so it can be printed  
		Returnn: Drink name
		"""
		return self.name
##Returns winning amount of Drink won		
	def getWinnings (self):
		"""
		Purpose: Return drink credit value so it can be added to winnings amount
		Returnn: Drink credit value
		"""
		return self.winnings

##Adds colors to drinks when printed

	def printName(self):
		"""
		Purpose: Create a color for each drink when it is printed using a dictionary
		Returnn: Color value in a string
		"""
		drink_colors = {'coke': 'red', 'welchs': 'magenta', 'ibc': 'blue', 'jolt': 'green', 'bawls': 'cyan'}
		return drink_colors[self.name]