import random
import sys
from Monster import *
from Player import Player
from Home import House
from Weapon import Weapon

#I mixed up my class schedule and mistook that an assingment due for my other class was due today and that this assingment was due today

class Game:
    #constructor to set up the game! When instantiated, we will play!
    def __init__(self):
        
        #initializing the player
        player = Player()
        
        #variable to hold whether the game is over
        gameOver = False

        neighborhood = [[0 for y in range(5)] for x in range(5)]
        
        #variable to keep track of the number of monsters in the entire game
        monster_num = 0
        
        #populating the neighborhood and getting the number of monsters in the game
        for i in range(len(neighborhood)):
            for j in range(len(neighborhood[i])):
                neighborhood[i][j] = House()
                monster_num = monster_num + neighborhood[i][j].monster_count
                print("H", end=" ")
            print()

            #random start location stored as a tuple
        location = (random.randint(0,len(neighborhood)-1), random.randint(0,len(neighborhood)-1))


        #printing initial message
        print("----------------------------------------------------\n It's Halloween and the neighborhood has turned into monsters. It's up to you to save the neighborhood\n --------------------------------------------------- ")
        print("P is your current location")
        print("Your HP: " + str(player.hp))
        print ("And right now you are at this location: " + str(location))
        pName = input("Name?")

        #Counting the turns of the game
        turnCounter = -1

        #main game
        while gameOver != True:

            turnCounter = turnCounter +1
            for i in range(len(neighborhood)):
                for j in range(len(neighborhood[i])):
                    neighborhood[i][j] = House()
                    monster_num = monster_num + neighborhood[i][j].monster_count
                    if neighborhood[location[0]-1][location[1]-1] == neighborhood[i][j]:
                        print("P", end=" ")
                    else:
                        if str (neighborhood[i][j].monster_count) == 0:
                            print("X", end=" ")
                        else:
                            print("H", end=" ")
                print()
            if player.hp <0:
                print("YOU DIED\nGAME OVER")
                gameOver = True
            if str (neighborhood[location[0]-1][location[1]-1].monster_count) == 0:
            #print information for each turn
                print("\n\n\n\n\n")
                print("Turn: " +str(turnCounter))
                print("Name: " + pName)
                print("HP: " + str(player.hp))
                print ("Location: " + str(location))
                print ("Monsters in this house: " + str (neighborhood[location[0]-1][location[1]-1].monster_count))
                print("All Monsters left: "+ str(monster_num))
                option = input("Choose an action(move {up, down, left, right}, or exit (to end the game)):\n")
            else:
                print("\nThere are monsters in this house!\n Would you like to attack?")
                print(pName+"'s HP: " + str(player.hp))
                print("Monsters in this house: " + str(neighborhood[location[0] - 1][location[1] - 1].monster_count))
                option = input("Choose an action('attack' to attack or 'flee):\n")

            #checking gameOver Conditions
            if monster_num <=0:
                print("YOU WON\n")
                print("-----------------GAME OVER--------------------------")
                gameOver = True
            if player.hp < 0:
                print("YOU DIED\n")
                print("-----------------GAME OVER--------------------------")
                gameOver = True

            if option == option == option.lower() == "flee":
                option = input("Choose an action(move {up, down, left, right}, or exit (to end the game)):\n")
            #taking in commands
            #option = input("Choose an action:\n")
            #Exit the game
            if option == option.lower() == "exit":
                print("-----------------GAME OVER--------------------------")
                gameOver = True

            #go North
            elif option.lower().lstrip() == "move up":
                if location[0] != 0:
                    location= (location[0]-1, location[1])
                else:
                    print("You can't go that way")

            #go South
            elif option.lower().lstrip() == "move down":
                if location[0] != len(neighborhood):
                    location= (location[0]+1, location[1])
                else:
                    print("You can't go that way")

            #go East
            elif option.lower().lstrip() == "move right":
                if location[1] != len(neighborhood):
                    location= (location[0], location[1]+1)
                else:
                    print("You can't go that way")

            #Go West
            elif option.lower().lstrip() == "move left":
                if location[1] != 0:
                    location= (location[0], location[1]-1)
                else:
                    print("You can't go that way")


            #attacking Monsters logic
            elif option.lower().lstrip() == "attack":
                counter = 0
                #print out monster_list for conveniece :)
                for i in neighborhood[location[0]][location[1]].monster_list:
                    print (str(counter) +"-"+ str(i.Name) +" --" + str(i.Health))
                    counter = counter +1
                directed_attack = input("Who would you like to attack? If you 'attack' a person they will give you a peice of candy! \nChoose a number:")


                if directed_attack == exit:
                    pass


                #checking valid input for the list player is supposed to enter an index in order to do a lookup
                #One problem here is I could not find a way to check a string being an int without casting it as an int beforehand which is a problem :(
                elif type(int(directed_attack)) is int and int(directed_attack) < len(neighborhood[location[0]][location[1]].monster_list)  and int(directed_attack) >= 0:
                    counter = 0
                    print("\n\n\n")
                    for i in player.weapons:
                        print (str(counter) + "-" +str(i.Name) +" --qty: " + str(i.qty))
                        counter = counter +1


                    #wanting to know the index of what item the player wants
                    attackItem = input("Enter an index for which weapon you want to use: ")
                    if type(int(attackItem)) is int and int(attackItem) < len(player.weapons) and int(attackItem) >= 0 and player.weapons[int(attackItem)].qty > 0:

                    	#calling getAttackedBy on the monster that the player wants to attack
                        neighborhood[location[0]][location[1]].monster_list[int(directed_attack)].getAttackedBy(player.useItem(int(attackItem)), player.weapons[int(attackItem)].Name)

                        #The player used a weapon, so we now have 1 less of that item
                        player.weapons[int(attackItem)].qty = player.weapons[int(attackItem)].qty - 1

                        #getting the damage appropriate for the monster
                        damage = neighborhood[location[0]][location[1]].monster_list[int(directed_attack)].Attack()
                        #changing print message depending on whether or not the monster is a person or not
                        if neighborhood[location[0]][location[1]].monster_list[int(directed_attack)].Name == "Person":
                            #in case they want to get healed different message
                            print("Here's some candy! +"+ str(damage*-1) + " HP")
                        else:
                            #printing message for monster attacks
                            print("The " + neighborhood[location[0]][location[1]].monster_list[int(directed_attack)].Name + " Leaps towards you and attacks you for "+ str(damage) + " damage")
                        #updating player health
                        player.hp = player.hp - damage
                        #checking if monster dies, which then we wnat to notify the house and then that will mean that we have 1 less monster
                        if neighborhood[location[0]][location[1]].monster_list[int(directed_attack)].isDead():
                            neighborhood[location[0]][location[1]].update(int(directed_attack))
                            monster_num = monster_num-1
                            print("The monster has turned into a person!\n"
                                  "They've given you a piece of candy as a thank you +1HP")
                            player.hp = player.hp + 1
                    else:
                        print("Please enter a correct number next time")
                else:
                    print("please enter a correct number corresponding to a monster")
                    
            else:
                print("You can't fo that")

def main():
   	g = Game()


if __name__ == "__main__":
   	main()
