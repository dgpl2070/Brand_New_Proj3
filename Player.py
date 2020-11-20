#
import random
from Weapon import Weapon
class Player:
	
	def __init__( self ):
		self.hp = random.randint( 100 , 125 )
        #modified the attack rating to make destroying monsters more enjoyable
		self.attack = random.randint( 30,45)
		self.weapons = []
		for i in range(4):
			if i == 0:
				self.weapons.append(Weapon(False))
		#randomly assign other weapon types to 9 remaining open slots using weapon class
			else:
				self.weapons.append(Weapon())
    
    #method to calculate damage based off of what weapon the player chooses
	def useItem(self, weaponIndex):
		if self.weapons[weaponIndex].qty > 0:
			self.weapons[weaponIndex].qty - 1
			if self.weapons[weaponIndex].Name == "Sour Straw":
				return self.attack * random.uniform(1,1.75)
			elif self.weapons[weaponIndex].Name == "Nerd Bomb":
				return self.attack * random.uniform(3.5,5)
			elif self.weapons[weaponIndex].Name == "Chocolate Bar":
				return self.attack * random.uniform(2,2.4)
			else:
				return self.attack