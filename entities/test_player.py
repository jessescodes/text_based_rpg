# test module for player.py

from player import Player

def test(player: Player):
    print("TESTING")

    result = player.to_dict()
    print(f"{result}")

    player.gains_experience(75)
    
    result_2 = player.to_dict()
    print(f"{result_2}")
    print("TEST OVER")


def main():
    player = Player("Scariel")

    test(player)


if __name__ == "__main__":
    main()
