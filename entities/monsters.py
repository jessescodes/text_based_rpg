#monsters subclass
import random
from entities.entity import Entity

class Monster(Entity):

    def __init__(self, name: str, max_hp: int, base_damage: int, armor: int, experience_payload: int):

        super().__init__(name, max_hp, base_damage, armor)
        self.attack_verb = None
        self.experience_payload = experience_payload


class Boar(Monster):
    def __init__(self, name: str = "Goretusk Boar"):
        super().__init__(
                name,
                random.randint(18, 25),
                random.randint(3, 5),
                0,
                20
        )
        self.attack_verb = "charges"
        self.gold_payload = 2


class Wolf(Monster):

    def __init__(self, name: str="Grey Wolf"):
        super().__init__(
                name,
                random.randint(20, 27),
                random.randint(4, 8),
                0,
                25
        )
        self.attack_verb = "Bites"
        self.gold_payload = 2


class Kobald(Monster):

    def __init__(self, name: str="Kobald Miner"):
        super().__init__(
                name,
                random.randint(22, 30),
                random.randint(6, 10), 
                0,
                25
        )
        self.attack_verb = "Swings it's mining pick"
        self.gold_payload = 2

class Bear(Monster):
    def __init__(self, name: str="Bitchen Bear"):
        super().__init__(
                name,
                random.randint(24, 35),
                random.randint(9, 15),
                2,
                35
        )
        self.attack_verb = "Thrash"
        self.gold_payload = 4



class DefiasBagBoy(Monster):

    def __init__(self, name: str="Defias Bag Boy"):
        super().__init__(
                name,
                random.randint(5, 8),
                0,
                0,
                5
        )
        self.attack_verb = "Cowers"
        self.gold_payload = 0



class DefiasPickPocket(Monster):

    def __init__(self, name: str="Defias Pickpocket"):
        super().__init__(
                name,
                random.randint(30, 37),
                random.randint(11, 13),
                1,
                30
        )
        self.attack_verb = "vicious slash"
        self.gold_payload = 3


class Warg(Monster):
    
    def __init__(self, name: str="Haunted Warg"):
        super().__init__(
                name,
                random.randint(40, 45),
                random.randint(18, 22),
                3,
                50
        )
        self.attack_verb = "Rampages"
        self.gold_payload = 5


class WitheredSkeleton(Monster):
    
    def __init__(self, name: str="Weathered Skeleton"):
        super().__init__(
                name,
                random.randint(49, 54),
                random.randint(25, 28),
                2,
                65
        )
        self.attack_verb = "Casts Frostbolt"
        self.gold_payload = 4



class Banshee(Monster):
    
    def __init__(self, name: str="Shrieking Banshee"):
        super().__init__(
                name,
                random.randint(60, 73),
                random.randint(30, 41),
                3,
                90
        )
        self.attack_verb = "Screams"
        self.gold_payload = 5


class Shambler(Monster):
    def __init__(self, name: str="Shambling Horror"):
        super().__init__(
                name,
                random.randint(65, 77),
                random.randint(32, 50),
                5,
                95
        )


class STVRaptor(Monster):
    def __init__(self, name: str="Strangle Horn Raptor"):
        super().__init__(
                name,
                random.randint(70-100),
                random.randint(44-70),
                8,
                110
        )
        self.attack_verb = "Rips"
        self.gold_payload = 9


class STVPanther(Monster):
    def __init__(self, name: str="Black Panther"):
        super().__init__(
                name,
                random.randint(80-105),
                random.randint(57,74),
                7,
                100
        )
        self.attack_verb = "rends"
        self.gold_payload = 11


class AmaniBerserker(Monster):
    def __init__(self, name: str="Amani Berserker"):
        super().__init__(
                name,
                random.randint(100, 120),
                random.randint(50, 84),
                10,
                125
        )
        self.attack_verb = "Swings his axe"
        self.gold_payload = 7


class DarkIronBarMaid(Monster):
    def __init__(self, name: str="Bar Maiden"):
        super().__init__(
                name,
                random.randint(200, 250),
                random.randint(150, 175),
                11,
                210
        )
        self.attack_verb = "Lashes out with her Flaggon"
        self.gold_payload = 10


class DarkIronSapper(Monster):
    def __init__(self, name: str="Sapper"):
        super().__init__(
                name,
                random.randint(210,300),
                random.randint(200, 210),
                10,
                250
        )
        self.attack_verb = "Throw's dynamite"
        self.gold_payload = 15
