# for class we want health attack-power and defense
# attackP subtracts from health
# Denfense subtracts from attack power
import sys # Allows the player to have the option exit the game
from hero import Hero #brings in our Hero class
from dragon import Dragon # brings in our Dragon class
import choose
import random # brings in the ability to call random
hero = Hero()
dragon = Dragon()

print "#################################"
print "THE LEGEND OF THE DRAGON SLAYER"
print "#################################"

print "LOOK! Up ahead... is that a Dragon?!"
print "It's coming straight for us!!!"
print "Quick, decide what to do"

# the user must input a choice
user_choice = raw_input(["Run or Fight?"])

choose.choose(user_choice)

if user_choice.upper() == 'FIGHT':
	print "your Health is " + str(hero.health)
	print "...."
	print "...."
	print "...."
	print "...."
	print "...."
	print "the Dragon's health is " + str(dragon.health) + "!!"
	print "Fight bravely!"

	battle_choice = raw_input(["Fight or Defend?"])
	choose.battle(battle_choice.upper(), hero, dragon)
