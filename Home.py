import random
from Monster import *
#house class that when constructed 
class House:
    def __init__(self):
    	#monster list that will keep track of the inhabitants in the house
        self.monster_list = []
        #number of monsters, need this because Persons cannot be killed
        self.monster_count = 0
        for i in range(10):
            self.monster_list.append(Monster())
            ran = random.randint(0,10)
            if (ran >8):
                self.monster_list[i]= Werewolf(self.monster_list[i])
                self.monster_count = self.monster_count+1
            elif (ran >6):
                self.monster_list[i]= Ghoul(self.monster_list[i])
                self.monster_count = self.monster_count+1
            elif (ran > 4):
                self.monster_list[i]= Vampire(self.monster_list[i])
                self.monster_count = self.monster_count+1
            elif (ran > 2):
                self.monster_list[i]= Zombie(self.monster_list[i])
                self.monster_count = self.monster_count+1
            else:
                self.monster_list[i]= Person(self.monster_list[i])

#updates
    def update(self, deathnum):
        self.monster_list.pop(deathnum)
        self.monster_count = self.monster_count -1
    
