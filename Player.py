import sys
##Player class
class Player:

	def __init__ (self, name, credits):
		self.name = name
		self.credits = credits
##Function to deduct 50 credits if Regex in main is true
	def payCredits (self, play):
		"""
		Purpose: Deducts/ pays credits if player wants to play the slots. Wuits if they don't
		Parameter: play (variable based on regex in main file)
		"""
		if  play == True:
			self.credits = self.credits - 50
		else:
			print ('Okay. Play another time')
			sys.exit()
##Funtion adding credits based on win
	def winCredits (self, you_won):
		"""
		Purpose: Adds credits that user wins after the slots
		Parameter: you_won
		"""
		self.credits = self.credits + you_won
		
#Make function to print the current credit string - JH
	def printCredits (self):
		"""
		Purpose: Print player's credit value  
		"""
		print "You have " + str(self.credits) + " credits"