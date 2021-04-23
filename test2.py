import lab.py

class Hero(Character)
	def __init__(average.damage, attack.damage, perk.damage):
		Hero = Hero("Hero")
		hero.level = 8
		hero.hp = 10 + floor((hero.constitution -10) / 2) + floor(randint(1,11)) * hero.level
		hero.strength = 18
		hero.dexterity = 12
		hero.constitution = 14
		hero.wisdom = 10

class Dragon(Character) 
	def __init__(average.damage, attack.damage, perk.damage):
		dragon = Dragon("Dragon")
		dragon.level = 10
		dragon.hp = 10 + floor((dragon.constitution - 10) / 2) + floor(randint(1,11)) * dragon.level
		dragon.strength = 20
		dargon.dexterity = 10
		dragon.constitution = 16
		dragon.wisdom = 20
		
hero_attacks_count = []
hero_perks_count = []
hero_heals_count = []
dragon_attacks_count = []
dragon_perks_count = []

def hero_average():
		for key in hero_attacks_count
			return (key + key) / len(dragon_attacks_count)

def dragon_average():
   for key in dragon_attacks_count:
      return (key + key) / len(hero_attacks_count)

def abilitie():
	abilities = 2 + floor((hero.charisma - 10) / 2)
	if(abilities > 0):
		abilities = abilities - 1
		return hero.perk()
	else:
		return None

if hero.initiative > dragon.initiative:
   for i in range(dragon.hp):
      if dragon.hp > 0:
         if hero.hp > 11:
            if abilitie() == True:
               hero_perk = abilitie()
               dragon.hp = dragon.hp - hero_perk
               hero_perks_count.append(hero_perk)
            else:
               hero_atack = hero.attack()
               dragon.hp = dragon.hp - hero_atack
               hero_attacks_count.append(hero_atack)
         else:
            healing = hero.save_throw(hero.wisdom)
            hero.hp = hero.hp + healing
            hero_heals_count.append(healing)
      else:
         dragon.death()
         break;
else:
   for i in range(hero.hp):
      if hero.hp > 0:
         if abilitie() == True:
            dragon_perk = abilitie()
            hero.hp = hero.hp - dragon_perk
            dragon_perks_count.append(dragon_perk)
         else:
            dragon_atack = dragon.attack()
            hero.hp = hero.hp - dragon_atack
            dragon_attacks_count.append(dragon_atack)
      else:
         hero.death()
         break;




