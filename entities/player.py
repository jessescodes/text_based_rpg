# player subclass
from entities.entity import Entity

class Player(Entity):

    def __init__(self, name: str):
        super().__init__(
            name,
            15,
            10,
            5
        )

        self.level = 1
        self.experience = 0
        self.crit_chance = .05            
        self.gold = 0
        self.potions = 0
        self.inventory = []
        self.equipped = {
                "weapon": None,
                "worn_armor": None,
        }


    def to_dict(self):
        return { 
                "name": self.name,
                "level": self.level,
                "XP": self.experience,
                "base damage": self.base_damage,
                "crit chance": self.crit_chance,
                "max HP": self.max_hp,
                "current hp": self.current_hp, 
                "armor": self.armor,
                "alive": self.is_alive,
                "inventory": [item.to_dict() for item in self.inventory],
                "equipped": {
                    "weapon": self.equipped["weapon"].to_dict() if self.equipped["weapon"] else None,
                    "worn_armor": self.equipped["worn_armor"].to_dict() if self.equipped["worn_armor"] else None,
                }
            }
      


    def use_potion(self):
        if player.potion >= 1:
            player.current_hp += (player.max_hp * .5)
            player.potion -= 1
        else:
            print("fresh outta potions pal")


    def _update_stats(self):
        self.crit_chance += .05
        self.base_damage += int(self.level**1.2)
        self.max_hp += int(self.level**1.3)

    def gains_experience(self, experience_gained: int):
        self.experience += experience_gained
        if self.experience >= self.level * 50:
            self.level += 1
            self._update_stats()
            self.current_hp = self.max_hp
