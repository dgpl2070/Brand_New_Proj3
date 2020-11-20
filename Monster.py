import random
#general Monster class that essentially all monsters 'inherit'
class Monster:
	def __init__ (self):
		pass
	def Attack(self):
		pass
	def getAttackedBy(self,playerAttack, playerItem):
		pass
	def isDead(self):
		pass
    

#A person has 100 health and will heal the player 50 points in order to keep gameplay more fun!
class Person:
	def __init__(self, Monster):
		self.Name = "Person"
		self.Health = 100
    
    #decided to heal 20 hp points due to number of monsters to kill
	def Attack(self):
		print("Here's some candy \n +1HP")
		return -1
	#never is attacked
	def getAttackedBy(self,playerAttack, playerItem):
		pass
	#will never die
	def isDead(self):
		return False
  
#Vampires!! These guys don't play around
class Vampire:
	#constructor to initialize health
	def __init__(self, Monster):
		self.Name = "Vampire"
		self.Health = random.randint(100,200)

	#method to get an attack value appropriate for a vampire
	def Attack(self):
		attack = random.randint(10,20)
		return attack

	#defined getting attacked by a player
	def getAttackedBy(self,playerAttack, playerItem):
		#not affected by chocolate Bars
		if (playerItem != "Chocolate Bar"):
			self.Health = self.Health - playerAttack
		else:
			pass
    #if it is dead
	def isDead(self):
		if self.Health < 0:
			return True
		else:
			return False
  
#Werewolves!! Time to get nerd bombs ready
class Werewolf:
	def __init__(self, Monster):
		self.Name = "Werewolf"
		self.Health = 200

	def Attack(self):
		attack = random.randint(0,40)
		return attack
    
	def getAttackedBy(self, playerAttack, playerItem):
		if playerItem == "Chocolate Bar" or playerItem == "Sour Straw":
			pass
		else:
			self.Health = self.Health - playerAttack
            
	def isDead(self):
		if self.Health < 0:
			return True
		else:
			return False

class Ghoul:
	def __init__(self, Monster):
		self.Name = "Ghoul"
		self.Health = random.randint(40,80)

	def Attack(self):
		attack = random.randint(15,30)
		return attack
    
	def getAttackedBy(self,playerAttack, playerItem):
		if playerItem == "Nerd Bomb":
			self.Health = self.Health - 5*playerAttack
		else:
			self.Health = self.Health - playerAttack
    
	def isDead(self):
		if self.Health < 0:
			return True
		else:
			return False


#Zombies!! 
class Zombie():
	def __init__(self, Monster):
		self.Name = "Zombie"
		self.Health = random.randint(50,100)

	def Attack(self):
		attack = random.randint(0,10)
		return attack

	def getAttackedBy(self,playerAttack, playerItem):
		if playerItem == "Sour Straw":
			self.Health = self.Health - 2*playerAttack
		else:
			self.Health = self.Health - playerAttack
            
	def isDead(self):
		if self.Health <= 0:
			return True
		else:
			return False
