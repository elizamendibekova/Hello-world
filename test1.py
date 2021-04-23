import lab1.py

hero = Hero("Hero")
hero.level = 8
hero.max_hp = 10 + floor((hero.constitution - 10) / 2) + floor(randint(1, 11)) * hero.level
hero.hp = hero.max_hp
hero.strength = 18
hero.dexterity = 12
hero.constitution = 14
hero.wisdom = 10

dragon = Dragon("Dragon")
dragon.level = 10
dragon.max_hp = 10 + floor((dragon.constitution - 10) / 2) + floor(randint(1, 11)) * dragon.level
dragon.hp = dragon.max_hp
dragon.strength = 20
dragon.dexterity = 10
dragon.constitution = 16
dragon.wisdom = 20

hero_attacks_count = []
hero_perks_count = []
hero_heals_count = []
dragon_attacks_count = []
dragon_perks_count = []

def hero_average():
   for key in hero_attacks_count:
      return (key + key) / len(hero_attacks_count)

def dragon_average():
   for key in dragon_attacks_count:
      return (key + key) / len(dragon_attacks_count)

for i in range(dragon.hp + 1):
   if dragon.hp > 0:
      if hero.hp > 11:
         hero_abilities = 2 + floor((hero.charisma - 10) / 2)
         if hero_abilities > 0:
            hero_perk = hero.perk()
            dragon.hp = dragon.hp - hero_perk
            hero_perks_count.append(hero_perk)
         else:
            hero_atack = hero.attack()
            dragon.hp = dragon.hp - hero_atack
            hero_attacks_count.append(hero_atack)
      else:
         hero.hp = hero.hp + 12
   else:
      dragon.death()
      break;
for i in range(hero.hp + 1):
   if hero.hp > 0:
      dragon_abilities = 2 + floor((hero.charisma - 10) / 2)
      if dragon_abilities > 0:
         dragon_perk = dragon.perk()
         hero.hp = hero.hp - dragon_perk
         dragon_perks_count.append(dragon_perk)
      else:
         dragon_atack = dragon.attack()
         hero.hp = hero.hp - dragon_atack
         dragon_attacks_count.append(dragon_atack)
   else:
      hero.death()
      break;
	




