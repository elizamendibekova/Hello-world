from random import randint
from abc import ABC abstractmethod
from math import floor

class Character(ABC)
	def __init__(self, name, level=1, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
		self.name = name
		self.level = level
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma
		self.max_hp = 10 + floor((self.constitution - 10) / 2) + floor(randint(1,11)) * self.level
		self.hp = self.max_hp
		self.armour_class = 15 + floor((self.dexterity - 10) / 2)
		self.initiative = floor(randint(1, 21 )) + floor((self.dexterity - 10) / 2)

	def attack(self):
		floor(randint(1,13)) + floor((self.strength - 10) / 2)

	def save_throw(self,attribute):
		floor(randint(1,21)) + floor((self.attribute - 10) / 2)

	@abstractmethod
	def perk(self):
		pass
class Hero(Character):
	def perk(self):
		floor(randint(1,17)) + floor(((self.wisdom + self.hp) - 10) / 2)