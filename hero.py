from ability import Ability
from armor import Armor

import random
# hero.py
class Hero:
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''
    
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  #add ability
  def add_ability(self, ability):
    ''' Add ability to abilities list '''
    self.abilities.append(ability)

  #fight
  def fight(self, opponent):
      rand_num = random.randint(0,1)
      if rand_num == 0:
        print(f"{opponent.name} defeats {self.name}!")
      elif rand_num == 1:
        print(f"{self.name} defeats {opponent.name}!")
 
  def attack(self):
    '''Calculate the total damage from all ability attacks.
      return: total_damage:Int
  '''
    total_damage = 0
    for ability in self.abilities:
        total_damage += ability.attack()
        return total_damage
  
  def add_armor(self, armor):
      '''Calculate the total damage from all ability attacks.
      return: total_damage:Int
  '''
      total_armor = 0
      for armor in self.armors:
        total_armor += armor.add_armor()
        return total_armor

  def defend(self):
    '''Calculate the total block amount from all armor blocks.
     return: total_block:Int
  '''
    total_block = 0
    for armor in self.armors:
      total_block += armor.block()
      return total_block

   
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

# if __name__ == "__main__":
#   # If you run this file from the terminal
#   # this block is executed.
#   hero1 = Hero("Wonder Woman")
#   hero2 = Hero("Dumbledore")

#   hero1.fight(hero2)


