#combat system test file


from entities.player import Player
from entities.monsters import Monster, Boar
from combat.combatengine import player_does_damage, player_takes_damage


def test(player, monster):
   
    playerDamage = player_does_damage(player, monster)

    playerTakesDamage = player_takes_damage(player, monster)


    print(f"{playerDamage}")
    print(f"{playerTakesDamage}")


def main():
    player = Player("dude guy")
    monster = Boar()

    test(player, monster)



if __name__ == "__main__":
    main()
