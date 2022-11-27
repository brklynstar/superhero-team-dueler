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

  def take_damage(self, damage):
    damage_amt = damage - self.defend()
    self.current_health -= damage_amt
    if damage_amt >= 0:
      print(f"{self.name} lost {damage_amt} units of power!")
    else:
      print(f"{self.name} lost no power!")
      return self.current_health

  def is_alive(self):
    '''Return True or False depending on whether the hero is alive or not.
  '''
    if self.current_health <= 0:
      return False
    else: 
      return True

  def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in.'''
      fight = True
      while fight == True:
        damage_amt = self.attack()
        opponent_damage_amt = int(opponent.attack())
        self.take_damage(opponent_damage_amt)
        opponent.take_damage(damage_amt)
        if self.abilities and opponent.abilities == 0:
          print("Draw!")
        else: 
          if self.is_alive == False and opponent.is_alive == True:
            print(f"{self.name} has been defeated! {opponent.name} is the victor!")
          
          elif self.is_alive == True and opponent.is_alive == False:
            print(f"{opponent.name} has bee defeated! {self.name} is the victor!")

          elif self.is_alive and opponent.is_alive == 0:
            print(f"No one wins! ")  
      

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())


