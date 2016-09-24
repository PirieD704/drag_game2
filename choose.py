import random
import sys

# This will decide if what the user input is acceptable which happens to be only if they choose fight
def choose(user_choice):
	print user_choice
	if user_choice.upper() == "RUN":
		print "You cannot run!!! The Dragon will kill you, you must fight!"
		user_choice = raw_input(["Run of Fight?"])
		choose(user_choice)
	elif user_choice.upper() != 'FIGHT':
		print "Enter a meaningful choice you fool! Before we all burn!"
		user_choice = raw_input(["Run of Fight?"])
		choose(user_choice)
	else:
		print "Good choice..."

#this is how the dragon responds to my choices
def dragonChoice(choice, hero, dragon):
	dragon_choice = round(random.random() * 4)
	if (dragon_choice == 0.0) or (dragon_choice == 3.0): #this is fight
		dragon_fight(choice, hero, dragon)
	elif dragon_choice == 1.0: #this is defense
		dragon_defend(choice, hero, dragon)
	else: #this is distract
		dragon_distract(choice, hero, dragon)
	if hero.health <= 0 or dragon.health <= 0:
		print "Game Over"
		if hero.health <= 0:
			print "You dead."
			sys.exit()
		elif dragon.health <= 0:
			print "He dead."
			sys.exit()
		else:
			print "both dead."
			sys.exit()

#fight function
def dragon_fight(choice, hero, dragon):
	if choice == "DEFEND": #player choose to defend this turn
		hero.health -= (dragon.attack - hero.defense)
		print "-------------------------------"
		print "The dragon attacks you for " + str(dragon.attack) + " damage, you blocked " + str(hero.defense) + " of it."
		print "-------------------------------"
		print "Hero HP: " + str(hero.health)
		print "Dragon HP: " + str(dragon.health)
		print "+++++++++++++++++++++++++++++++"
	elif choice == "FIGHT": #player choose to attack
		dragon.health -= hero.attack
		hero.health -= dragon.attack
		print "-------------------------------"
		print "The dragon attacks you for " + str(dragon.attack) + " damage"
		print "You dealt " + str(hero.attack) + " damage to the dragon."
		print "-------------------------------"
		print "Hero HP: " + str(hero.health)
		print "Dragon HP: " + str(dragon.health)
		print "+++++++++++++++++++++++++++++++"
	else:
		print "-------------------------------"
		print "You derped when you should have herped. Dragon dealt " + str(dragon.attack) + " damage."
		print "-------------------------------"
		print "Hero HP: " + str(hero.health)
		print "Dragon HP: " + str(dragon.health)
		print "+++++++++++++++++++++++++++++++"


#defend function
def dragon_defend(choice, hero, dragon):
	if choice == "FIGHT":
		dragon.health -= (hero.attack - dragon.defense)
		print "-------------------------------"
		print "The dragon defended your attack of " + str(hero.attack) + ", and blocked " + str(dragon.defense) + " of it."
		print "You dealt " + str(hero.attack - dragon.defense) + " damage to the dragon"
		print "-------------------------------"
		print "Hero HP: " + str(hero.health)
		print "Dragon HP: " + str(dragon.health)
		print "+++++++++++++++++++++++++++++++"
	else:
		print "You both decided to defend."


#distract function
def dragon_distract(choice, hero, dragon):
	if choice == "FIGHT":
		dragon.health -= (hero.attack * dragon.distract)
		print "-------------------------------"
		print "The dragon is distracted! You deal critical damage of " + str((hero.attack * dragon.distract)) + "!"
		print "-------------------------------"
		print "Hero HP: " + str(hero.health)
		print "Dragon HP: " + str(dragon.health)
		print "+++++++++++++++++++++++++++++++"


#battle options
def battle(choice, hero, dragon):
	if choice.upper() == "EXIT":
		leave()
	if choice.upper() == "FIGHT":
		dragonChoice(choice.upper(), hero, dragon)
		new_choice = raw_input("Fight or Defend?")
		battle(new_choice.upper(), hero, dragon)
	elif choice.upper() == "DEFEND":
		dragonChoice(choice.upper(), hero, dragon)
		new_choice = raw_input("Fight or Defend?")
		battle(new_choice.upper(), hero, dragon)
	elif choice.upper() == "PLAGUE":
		dragonChoice(choice.upper(), hero, dragon)
	elif choice.upper() == "BUBONIC":
		hero.health = 0
		dragon.health = 0
		print "---X---X---X---X---X---X---X---X---X---X---X---"
		print "you both got the bubonic plague. the rats win."
		print "---X---X---X---X---X---X---X---X---X---X---X---"
		sys.exit()




