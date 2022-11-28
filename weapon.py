import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
         between one half to the full attack power of the weapon.
        """
        weapon_power = random.randint(int(self.max_damage) // 2, int(self.max_damage))
        return weapon_power
