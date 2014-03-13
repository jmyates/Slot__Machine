import sys
##Player class
class Player:

	def __init__ (self, name, credits):
		self.name = name
		self.credits = credits
##Function to deduct 50 credits if Regex in main is true
	def payCredits (self, play):
		if  play == True:
			self.credits = self.credits - 50
		else:
			print ('Okay. Play another time')
			sys.exit()
##Funtion adding credits based on win
	def winCredits (self, youwon):
		self.credits = self.credits + youwon