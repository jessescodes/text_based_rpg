# bosses subclass
from entities.entity import Entity
from items.items import ThunderfuryBlessedBlade, JudgementArmor, LoaArmor, DefiasArmor
import random


class Boss(Entity):

    def __init__(self, name: str, max_hp: int, base_damage: int, armor: int, experience_payload: int):

        super().__init__(name, max_hp, base_damage, armor)
        self.experience_payload = experience_payload
        self.attack_verb = None
        self.drop: Item = None


    def does_drop(self, player):
        if random.random() < .2:
            result = self.drop()
            print("god be with you my child, for you were chosen, check your inventory")
            player.inventory.append(result)
        else:
            print("RNGeesus didn't smile on you today, take some gold though!")
       

class Stitches(Boss):
    def __init__(self, name: str = "Stitches the Terrible"):
        super().__init__(
                name,
                140,
                50,
                15,
                200
        )

        self.attack_verb = "Throw's chain"
        self.gold_payload = 15 
        self.drop = DefiasArmor


class ZulJun(Boss):
    def __init__(self, name: str = "Zul'Jun the Traitor"):
        super().__init__(
                name,
                200,
                120,
                20,
                400
        )
        self.attack_verb = "Casts the woojoo voodoo"
        self.gold_payload = 25
        self.drop = LoaArmor


class Infernum(Boss):
    def __init__(self, name: str = "Infernum the Fierce"):
        super().__init__(
                name,
                500,
                400,
                50,
                700
        )


        self.attack_verb = "Casts inferno"
        self.gold_payload = 100
        self.drop = JudgementArmor


class Ragnaros(Boss):
    def __init__(self, name: str = "Ragnaros the Elemental King"):
        super().__init__(
                name,
                1000,
                500,
                60,
                900
        )
        
        self.attack_verb = "Unleashes the fury of thunder"
        self.gold_payload = 1000
        self.drop = ThunderfuryBlessedBlade
