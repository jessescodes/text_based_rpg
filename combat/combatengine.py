# text_based_rpg combat engine
from config import CRIT_MULTIPLIER
from entities.player import Player
from entities.entity import Entity
import random


def damage_post_mitigation(damage: int, armor):
    return int(damage * (100 / (100 + armor)))


def does_damage(base_damage, crit_chance):
    if random.random() < crit_chance:
        return base_damage * CRIT_MULTIPLIER
    else:
        return base_damage



def player_does_damage(player: Player, enemy: Entity):
    weapon = player.equipped.get("weapon")
    bonus_damage = weapon.add_damage if weapon else 0
    added_damage = player.base_damage + bonus_damage

    player_damage = does_damage(added_damage, player.crit_chance)

    total_damage = damage_post_mitigation(player_damage, enemy.armor)

    return total_damage


def player_takes_damage(player: Player, enemy: Entity):
    armor = player.equipped.get("worn_armor")
    bonus_armor = armor.add_armor if armor else 0

    player_armor = player.armor + bonus_armor
    
    return damage_post_mitigation(enemy.base_damage, player_armor)
    
