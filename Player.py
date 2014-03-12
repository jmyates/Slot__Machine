import sys

class Player:

	def __init__ (self, name, credits):
		self.name = name
		self.credits = credits
		
	def payCredits (self, play):
		if self.credits >= 50 and play == True:
			self.credits = self.credits - 50
		else:
			print 'Okay. Play another time'
			sys.exit()

	def winCredits (self, youwon):
		self.credits = self.credits + youwon