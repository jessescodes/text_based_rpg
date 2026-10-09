# nodes for graphmap
import random
from combat.combatengine import (
    player_does_damage,
    player_takes_damage
)
from items.items import Item, Weapon 
from entities.player import Player
from entities.monsters import (
    Boar,
    Wolf,
    Kobald,
    Bear,
    DefiasBagBoy,
    DefiasPickPocket,
    Warg,
    WitheredSkeleton,
    Banshee,
    Shambler,
    STVRaptor,
    STVPanther,
    AmaniBerserker,
    DarkIronBarMaid,
    DarkIronSapper,
)
from entities.bosses import (
    Boss,
    Stitches,
    ZulJun,
    Infernum,
    Ragnaros,
)


class Zone():
    def __init__(self, name: str):
        self.name = name
        self.connections = None
        

class Town(Zone):
    def __init__(self, name):
        super().__init__(
            "Stormwind City"
        )

        self.description = """\
        You have arrived at the alliance captial city of stormwind. Sun sun
        shines on your face, and the cobbled streets bustle with activity.
        This town has everything you might need on your coming adventures.
        where would you like to go?

        1. The sunny forest of Elewyn 
        2. The dark depths of Duskwood
        3. The Jungles of StrangleThorn
        4. The Depths of BlackRock
        5. Re-equip at the Smithy
        6. Rest and heal at the Inn
        7. Find a potion at the Apothecary
        """
        self.connections = {} 


class Blacksmith(Zone):
    def __init__(self, name):
        super().__init__(
        "Thor's smithy"
        )

        self.description = """\
        Welcom to Thor's smithy. Your one stop shop to help one shot one of two
        things....Kobalds or noobs. So if you're a swifty enjoyer, we're here
        for you. If not, let Thor help you suck less! How can Thor help you?

        1. Browse the shop
        2. return to town
        """
        self.connections = {}


class BlacksmithInventory(Zone):

    def __init__(self, name):
        super().__init__(
        "blacksmith_inventory"
        )
        self.description = """\
        Thor's wares! What would you like to buy? Please note, absolutely no
        refunds... We don't do business like goblins.

        1. Iron Sword - 20 gold
        2. Steel Sword - 50 gold
        3. Mithril Sword - 100 gold
        4. Return to the smithy
        """
        self.connections = {}
        self.actions = {}

    def buy(self, player, item: Weapon, gold):
        
        if player.gold < gold:
            print("not enough gold")
        else:
            purchased = item()
            player.inventory.append(purchased)
            player.gold -= gold
            print("Thanks for your patronage! I promise you didn't get gyped")
        

class Inn(Zone):

    def __init__(self, name):
        super().__init__(
        "Onyxia's rest"
        )
        self.description = """\
        Welcome to Onyxia's rest. The Inn so comfy even that hag Onyxia would
        sleep here without complaint. What can I do for you today? Would you 
        like a room, or just trying to get a world buff? Of course if you're 
        staying there's no such thing as a free lunch!

        1. Rest for the night 3 gold
        2. Return to town
"""
        self.connections ={}
        self.actions = {}

    def rest(self, player):
        if player.gold < 2:
            print("not enough gold")
        else:
            player.gold -= 2
            player.current_hp = player.max_hp



class Apothecary(Zone):
    def __init__(self, name):
        super().__init__(
                "Medihv's Medicinal Maladi's"
        )
        self.description = """\
        Welcome to Medihv's Medicial Maladi's! Where you might get cured, or
        you might die. You wanna roll the die?

        1. Browse the Shop
        2. Return to town
        """
        self.connections = {}
        self.actions = {}
       


class ApothecaryInventory(Zone):
    def __init__(self, name):
        super().__init__(
            "Medihv's wares"
        )
        self.description = """\
        Feel free to look around, though the inventory is a little sparse after
        the war with those damn green skinned orcs, so there's not much. Don't 
        worry, everything is sourced locally, and most definately...kind of
        vegan...

        1. Health Potion 5 gold
        2. Return to shop
        """
        self.connections = {}
        self.actions = {}

    def buy(self, player):
        if player.gold < 5:
            print("not enough gold")
        else:
            player.gold -= 5
            player.potion += 1

class Traversal(Zone):
    def __init__(self, name):
        super().__init__(name)
        self.description = None
        
       




class ElewynForest(Traversal):
    def __init__(self, name):
        super().__init__(
            "Elewyn Forest"
        )
        self.description = """\
        You walk into among the most beautiful places in Azeroth, and without
        a doubt an area most have adventured. Elewyn Forest. Beautiful blue skies
        green grass, trees as far as the eye can see. Definately noob friendly.
        as you walk you see a sign:

        1. Travel west to the fields of Boars Galore
        2. Travel north to Jana's farm
        3. Travel east an raid the Defias Hideout
        """
        self.connections = {}



class Monster(Zone):
    def __init__(self, name):
        super().__init__(name)

        self.description: str = None
        self.connections = {}
        self.actions = {}
        self.monsters_list = []
        self.scenery: str = None


    def spawn(self):
        spawned_monster = random.choice(self.monsters_list)
        return spawned_monster

    def explore(self, player):
        print("You decided to explore the area, and take an adventure.")
        active_monster = self.spawn()
        monster = active_monster()
        print(f"While exploring the {self.scenery}, a {monster.name} appears")
        while player.is_alive == True and monster.is_alive == True:
            print("=" * 70)
            print(f"{player.name} is engaged in combat with {monster.name}")
            print(f"{player.name}: {player.current_hp} | {monster.name}: {monster.current_hp}")
            print(f"[1] attack | [2] use potion {player.potions} | [3] flee")

            combat_choice = input("\nChoose combat action. 1, 2 or 3")
            if combat_choice == "1":
                player_damage_done = player_does_damage(player, monster)
                monster_damage_done = player_takes_damage(player, monster)

                print(f"{player.name} does {player_damage_done}")
                monster.current_hp -= player_damage_done

                if monster.current_hp <= 0:
                    print(f"""\
                    You deafeated {monster.name}! You've gained {monster.experience_payload}
                    experience and {monster.gold_payload} gold! Well fought!
                          """)
                    player.gains_experience(monster.experience_payload)
                    player.gold += monster.gold_payload
                    monster.is_alive = False
                    break
                
                
                print(f"{monster.name} does {monster_damage_done}")
                player.current_hp -= monster_damage_done

                if player.current_hp <= 0:
                    print("you have died... this is hardcore mode")
                    sys.exit()
                

            elif combat_choice == "2":
                player.use_potion()

            elif combat_choice == "3":
                return
            else:
                print("user input incorrect")






class BoarFields(Monster):
    def __init__(self, name):
        super().__init__(
            "Fields of Boars Galore"
        )
        self.description = """\
        After travelling west some time you've come across the most iconic fields
        in azeroth. The fields where 4 young adventurers fought for months to
        obtain the sword of 1000 truths... Now removed from the game for being
        far too OP. How will you proceed? Shall we also slay boars?

        1. Explore the fields of boars galore, and battle
        2. Travel back to Elewyn Forest
        3. Hearthstone back to Stormwind
        """
        self.connections = {}
        self.actions = {}
        self.scenery = "fields of endless boars"
        self.monsters_list = [
            Boar,
            Wolf
        ]


class JanasFarm(Monster):
    def __init__(self, name):
        super().__init__(
            "Jana's Grape Farm"
        )
        self.description = """\
        You've travelled north and stumbled upon a beautiful vinery. There are
        plentiful grapes, but it seems the owner hasn't been around for some time.
        as you walk around you spot dozens of Kobald miner's screaming about...
        candles? TF do they want candles for? What will you do? I guess...

        1. Debo those Kobalds, and make them regret losing their candle
        2. Go back to Elewyn, this doesn't pay enough for huge rats
        3. Hearth to Stormwind
        """
        self.connections = {}
        self.actions ={}
        self.scenery = "downtrodden grap fields"
        self.monsters_list = [
            Wolf,
            Kobald,
            Bear
        ]
        

class DefiasHideout(Monster):
    def __init__(self, name):
        super().__init__(
            "Defias Hideout"
        )
        self.description = """\
        You've walked into the shadies (both literally and figuratively) part of
        Elewyn Forest. There must be a disgruntled brick layer around here or
        something like that... Where do you want to go next?

        1. Explore the area, and search for Van Cleef
        2. I'll bounce back to Elewyn, I'm not trying to beat brick layers
        3. Hearth to stormwind
        """
        self.connections ={}
        self.actions = {}
        self.scenery = "Shaded alcoves and trees"
        self.monsters_list = [
            Bear,
            DefiasBagBoy,
            DefiasPickPocket,
        ]
        


class DuskWood(Traversal):
    def __init__(self, name):
        super().__init__(
            "Duskwood"
        )
        self.description = """\
        Well if you thought the Defias Hideout was bad, now you're in a whole 
        different league. TF is this skelly's and haunted stuff all over?
        To top if off theres and obese zombie carrying a kusarigama?!? How he
        even get that? We really going in here?

        1. Hell yea, but lets start easy and go to the haunted orchards
        2. Maybe the Crypts aren't as ominous as the name implies? Lets go!
        3. Giant obese kusarigama toting zombie? Sounds like free XP!
        """
        self.connections = {}
        

class HauntedOrchard(Monster):
    def __init__(self, name):
        super().__init__(
            "Haunted ahh Orchard"
        )
        self.description = """\
        Well, i guess this is easy. Orchard is a bit of a lie because nothing 
        seems to be alive. There are giant clawwed footprints everywhere, and 
        and un-natural chill in the air... Um adventure? We really down for this?

        1. Let's go see what makes footprints that big!
        2. I might not be down for this... return to duskwood
        3. Yea so, I think Stormwind sounds better. Hearth out.
        """
        self.connections = {}
        self.actions = {}
        self.scenery = "desolate copse of trees"
        self.monsters_list = [
            Warg,
            WitheredSkeleton
        ]



class Crypt(Monster):
    def __init__(self, name):
        super().__init__(
            "Crypts"
        )
        self.description = """\
        You've travelled far through the depths of duskwood, and come upon an
        old crypt... Grave for you zoomers. The air is pungeunt with death and 
        decay. Whats the next move?

        1. Time to go grave robbing!
        2. Return to duskwood, this looks like a spawn trap
        3. Hearth back to stormwind
        """
        self.connections = {}
        self.actions = {}
        self.scenery = "the decaying tombs"
        self.monsters_list = [
            Banshee,
            Shambler
        ]


class Boss(Zone):
    def __init__(self, name):
        super().__init__(name)
        self.description = None
        self.connections = {}
        self.actions = {}
        self.boss_name = None


    def send_it(self, player, boss: Boss):
        boss = self.boss_name()
        print(f"Well here we are... {boss.name} stands before us!")
        while player.is_alive == True and boss.is_alive == True:
            print("=" * 70)
            print(f"{player.name} is engaged in combat with {boss.name}")
            print(f"{player.name}: {player.current_hp} | {boss.name}: {boss.current_hp}")
            print(f"[1] attack | [2] use potion {player.potion} | [3] flee")

            combat_choice = input("\nChoose combat action. 1, 2 or 3")
            if combat_choice == "1":
                player_damage_done = player_does_damage(player, boss)
                boss_damage_done = player_takes_damage(player, boss)

                print(f"{player.name} does {player_damage_done}")
                boss.current_hp -= player_damage_done

                if boss.current_hp <= 0:
                    print(f"""\
                    You deafeated {boss.name}! You've gained {boss.experience_payload}
                    experience and {boss.gold_payload} gold! Well fought!
                          """)
                    boss.does_drop(player)
                    player.experience += boss.experience_payload
                    player.gold += boss.gold_payload
                    boss.is_alive = False
                    break
                
                
                print(f"{boss.name} does {boss_damage_done}")
                player.current_hp -= boss_damage_done

                if player.current_hp <= 0:
                    print("you have died... this is hardcore mode")
                    sys.exit()
                

            elif combat_choice == "2":
                player.use_potion()

            elif combat_choice == "3":
                return
            else:
                print("user input incorrect")        



class StitchesLair(Boss):
    def __init__(self, name):
        super().__init__(
            "Stiche's Long Road"
        )
        self.description = """\
        As you travel through the nightmare fuel that is duskwood you find 
        yourself on a long, suspiciously quiet road... Until you hear the sound
        of a chain dragging, and thump thump of footsteps... It's the classic
        hardcore run ender Stiches. We running?

        1. Guess it's time to see if that grinding was worth it. No way its that
        bad right?
        2. I think grinding a bit more is in line with the experience...
        3. NOPE hearth 
        """
        self.connections = {}
        self.actions = {}
        self.boss_name = Stitches



class StrangleThornVale(Traversal):
    def __init__(self, name):
        super().__init__(
            "Strangle Thorn Vale"
        )
        self.description = """\
        Welcome to the jungle! Home of that Dwarf named after the greatest American
        author, and wildlife far bigger than is necessary! Beware of trolls!

        1. Go North! I hear there are raptors.
        2. Go East, and see what's got the trolls so riled up... wait, are they
        the enemy or not?
        3. Head back to Stormwind
        """
        

class RaptorPit(Monster):
    def __init__(self, name):
        super().__init__(
            "Raptor Pit"
        )
        self.description = """\
        You've walked north for some time. The deeper you delve into the jungle
        the more frequently you see the signs of wildlife... Large wildlife. 
        Scratches from claws on trees, and torn up soil. You're not ending the
        adventure here right?

        1. Of course, lets go find what's so large about this wildlife!
        2. Might just head back and kick it with my boy Hemmingway.
        3. I think Stormwind is calling... Hearth
        """
        self.connections = {}
        self.actions = {}
        self.scenery = "ravaged jungle"
        self.monsters_list = [
            STVRaptor,
            STVPanther
        ]


class TrollRuins(Monster):
    def __init__(self, name):
        super().__init__(
            "Amani Ruins"
        )
        self.description = """\
        Not really sure if we can actually debo trolls anymore... are alliance
        and horde enemies or allies? Well best not to fret over that. Seems like
        there's some pissed trolls around. Want to see if we can roll em?

        1. Of course, Dees Troll gon learn today.
        2. Naw I like trolls lets leave them be.
        3. hearth
        """
        self.connections = {}
        self.actions = {}
        self.scenery = "dilapidated ruins"
        self.monsters_list = [
            STVRaptor,
            STVPanther,
            AmaniBerserker
        ]


class ZulJun_Lair(Boss):
    def __init__(self, name):
        super().__init__(
            "Zul Jun's Lair"
        )
        self.description = """\
        You travel deeper into the troll ruins, there must be a baddie in here...
        But isn't that Zul'Jun? Isn't he a Midnight boss, and this is like very
        classic-ish? Well Guess beggers can't be choosers. This gotta be easier
        than coiled alter, whats you move?

        1. Killed him once w/ the ghost dude, cant be that hard with him alone...
        2. Gunna prepare a bit more first, potions are low...
        3. hearth back to Stormwind, maybe I'll talk to that Thor guy?
        """
        self.connections = {}
        self.actions = {}
        self.boss_name = ZulJun


class BlackRockDepths(Traversal):
    def __init__(self, name):
        super().__init__(
            "Black Rock Depths"
        )
        self.description = """\
        Well we made it... This is the end game. All those spooky ahh forests and
        whompus monsters led us here. Aint no way we're gunna back down now. Where
        we going?

        1. I hear there's some dwarfs drinking down the corridor there.
        2. The other way is a huge ahh fire elemental, maybe bring some water.
        3. The Firelord is in the depths of the core... make sure you're geared
        """
        self.connections = {}


class GrimGuzzler(Monster):
    def __init__(self, name):
        super().__init__(
            "The Grim Guzzler"
        )
        self.description = """\
        You walk into the loudest, rowdiest... strangest tavern in Azeroth. The
        Grim Guzzler. Where Dark Iron Dwarves and succubi live in peace, and really
        only worry about getting plastered. We gunna come in and wreck the place?
        Or we gunna join in?

        1. A bar night aint that without a bar fight right?
        2. Why fight when we can choose peace, sit down and have an ale.
        3. Head back down the mountain. You're not in the mood.
        4. Hearth back, and drink with the night elf at the Inn.
        """
        self.connections = {}
        self.actions = {}
        self.scenery = "the bar"
        self.monsters_list = [
            DarkIronBarMaid,
            DarkIronSapper
        ]

    def have_a_drink(self, player):
        if player.gold < 5:
            print("you're too broke to buy a beer at endgame?")
        elif player.current_hp < 5:
            print("careful that drink'll kill ya pal")
        else:
            player.gold -= 5
            player.current_hp -= 5
            print("you're feelin pretty drunk... tf these dwarfs drink?")


class InfernumLair(Boss):
    def __init__(self, name):
        super().__init__(
            "Infernums fire field"
        )
        self.description = """\
        We're definately not in Stormwind anymore. There's hecka fire in here. As 
        you walk forward the heat radiating from the black mountain walls is 
        unbearable. That's when you see him A giant fire elemental. We gunna
        raid the end game bosses, boss?

        1. Strap up yer boots, its clobberin time.
        2. Naw need some more gear/ potions, return to BlackRock.
        3. Lets talk to midhiv first... he's not doing his job. hearth.
        """
        self.connections = {}
        self.actions = {}
        self.boss_name = Infernum


class RagnarosLair(Boss):
    def __init__(self, name):
        super().__init__(
            "Ragnaros the Fire Lord"
        )
        self.description = """\
        We've made it... got attuned to Molten Core, and here we are. A huge ahh
        dude made of lava and fire. Homie was litterally king of this world in the 
        past... We got the stones to fight him? Also this guy doesn't just drop
        the bindings... He drops the actual sword...Did somebody say...

        1. Thunderfury?!?! Yes attack now!
        2. TF is Thunderfury? I'll head out...
        3. hearth.
        """
        self.connections = {}
        self.actions = {}
        self.boss_name = Ragnaros
