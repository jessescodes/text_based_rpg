# main file for text_based_rpg
#we're finally here... this ended up being way bigger than i expected.
# day 32 and this absolute tank of a codebase is finally getting put together
from entities.entity import Entity
from entities.player import Player
from world.world import build_world

def main():

    running = True
    player = Player("Tester")
    current_location = build_world(player)


    while running:
        print(f"{current_location.description}")
        print(f"{player.name}: {player.level} hp: {player.current_hp}")
        player_choice = input()

        if player_choice in current_location.connections:
            current_location = current_location.connections[player_choice]

        elif player_choice in current_location.actions:
            current_location.actions[player_choice]()

        else:
            print("please make a valid numeric input")




if __name__ == "__main__":
    main()
