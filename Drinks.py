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
		if self.name == "coke":
			return "red"
		elif self.name == "welchs":
			return "magenta"
		elif self.name == "ibc":
			return "blue"
		elif self.name == "jolt":
			return "green"
		elif self.name == "bawls":
			return "cyan"