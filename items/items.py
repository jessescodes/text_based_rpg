# items class settings for text_based_rpg


class Item():
    def __init__(self, name: str, item_id: str):
        self.name = name
        self.id = item_id
        


           

class Weapon(Item):
    def __init__(self, name: str, item_id: str):
        super().__init__(
            name,
            item_id,
            add_damage,
            add_crit,
        )
        self.add_damage = add_damage
        self.add_crit = add_crit

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "add_damage": self.add_damage,
            "add_crit": self.add_crit
        }

    def equip(self, player):
        if player.equipped["weapon"] == None:
            player.equipped["weapon"] = self
        else:
            item = player.equipped.pop("weapon")
            player.inventory.append(item)
            player.equipped["worn_armor"] = self

    
class WornArmor(Item):
    def __init__(self, name: str, item_id: str):
        super().__init(
            name,
            item_id,
            add_armor,
        )
        self.add_armor = add_armor


    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "add_armor": self.add_armor
        }

    def equip(self, player):
        if player.equipped["worn_armor"] == None:
            player.equipped["worn_armor"] = self

        else:
            item = player.equipped.pop("worn_armor")
            player.inventory.append(item)
            player.equipped["warn_armor"] = self


class DefiasArmor(WornArmor):
    def __init__(self, name, item_id):
        super().__ini__(
            "Defias Blackend Armor",
            "defias_armor",
            "15"
        )


class LoaArmor(WornArmor):
    def __init__(self, name, item_id):
        super().__init__(
            "Dee Loa's Blessin",
            "loa_armor",
            "20"
        )


class JudgementArmor(WornArmor):
    def __init__(self, name, item_id):
        super().__init__(
            "Judgement",
            "judgement",
            "30"
        )


class IronSword(Weapon):
    def __init__(self, name, item_id):
        super().__init__(
            "Iron Sword",
            "iron_sword",
            "10",
            "0.05"
        )


class SteelSword(Weapon):
    def __init__(self, name, item_id):
        super().__init__(
            "Steel Sword",
            "steel_sword",
            50,
            0.1
        )


class MithrilSword(Weapon):
    def __init__(self, name, item_id):
        super().__init__(
            "Mithril Sword",
            "mithril_sword",
            100,
            0.2
        )


class ThunderfuryBlessedBlade(Weapon):
    def __init__(self, name, item_id):
        super().__init__(
            "Thunderfury Blessed Blade of the Windseeker",
            "thunderfury",
            400,
            .20
        )
