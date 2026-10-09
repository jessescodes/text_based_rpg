# entity parent class


class Entity:
    def __init__(self, name: str, max_hp: int, base_damage: int, armor :int):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.base_damage = base_damage
        self.armor = armor
        self.is_alive: bool = True


    def takes_damage(self, damage):
        if self.current_hp > damage:
            return self.current_hp - damage

        if self.current_hp <= damage:
            self.current_hp = 0
            self.is_alive = False
       





