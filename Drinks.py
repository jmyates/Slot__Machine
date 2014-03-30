class Drinks:

	def __init__ (self, winnings, name):
		self.winnings = winnings
		self.name = name
	
##Returns name of drink	
	def getName (self):
		return self.name
##Returns winning amount of Drink won		
	def getWinnings (self):
		return self.winnings

##Adds colors to drinks when printed

	def printName(self):
		#Make this a dictionary.  In the end it should say -JH
		#return dictName[self.name]
		#You should be able to explain why and how this works
		drinkcolors = {'coke': 'red', 'welchs': 'magenta', 'ibc': 'blue', 'jolt': 'green', 'bawls': 'cyan'}
		return drinkcolors[self.name]