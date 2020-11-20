#Common class for all weapons
import random
class Weapon:
	def __init__( self , other = True ):

		# not Hershey Kisses
		if( other == True ):
			r = random.randint( 7 , 9 )
			if r == 7:
				self.Name = "Sour Straw"
				self.damage = random.uniform( 1 , 1.75 )
				self.qty = 2
			elif r == 8:
				self.Name = "Chocolate Bar"
				self.damage = random.uniform( 2 , 2.4 )
				self.qty = 4
			elif r == 9:
				self.Name = "Nerd Bomb"
				self.damage = random.uniform( 3.5 , 5 )
				self.qty = 1

		# Hershey Kisses
		else :
			self.Name = "Hershey Kisses"
			self.damage = 1
			self.qty = 1000000