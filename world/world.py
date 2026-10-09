#world building function
#called in main to instantize all the world nodes
from world.nodes import (
    Town,
    Blacksmith,
    BlacksmithInventory,
    Inn,
    Apothecary,
    ApothecaryInventory,
    Traversal,
    Zone,
    ElewynForest,
    Monster,
    BoarFields,
    JanasFarm,
    DefiasHideout,
    DuskWood,
    HauntedOrchard,
    Crypt,
    Boss,
    StitchesLair,
    StrangleThornVale,
    RaptorPit,
    TrollRuins,
    ZulJun_Lair,
    BlackRockDepths,
    GrimGuzzler,
    InfernumLair,
    RagnarosLair
)

def build_world(player):
    town = Town("Stormwind")
    blacksmith = Blacksmith("Thor's")
    blacksmith_inventory = BlacksmithInventory("Thor")
    inn = Inn("Onyxia's rest")
    apothecary = Apothecary("Midhiv's") 
    apothecary_inventory = ApothecaryInventory("Shady Supply")
    elewyn = ElewynForest("Elewyn Forest")
    boar_fields = BoarFields("Boar Field")
    janas_farm = JanasFarm("Jana's Farm")
    defias_hideout = DefiasHideout("Defias Hideout")
    duskwood = DuskWood("Duskwood")
    haunted_orchard = HauntedOrchard("Haunted Orchard")
    crypt = Crypt("Creepy Crypt")
    stitches = StitchesLair("Stiches Road")
    stranglethorn_vale = StrangleThornVale("STV")
    raptor_pit = RaptorPit("Raptor Pit")
    troll_ruins = TrollRuins("Troll Ruins")
    zul_juns_lair = ZulJun_Lair("ZulJuns Hangout")
    black_rock_depths = BlackRockDepths("BRD")
    grim_guzzler = GrimGuzzler("The Glizzy Guzler")
    infernum = InfernumLair("Infernum's place")
    ragnaros = RagnarosLair("Molten Core")







    town.connections = {
    "1": elewyn,
    "2": duskwood,
    "3": stranglethorn_vale,
    "4": black_rock_depths,
    "5": blacksmith,
    "6": inn,
    "7": apothecary
    }


    
    blacksmith.connections = {
    "1": blacksmith_inventory,
    "2": town
    }

     
    blacksmith_inventory.connections = {
    "4": blacksmith
    }
    blacksmith_inventory.actions = {
    "1": lambda: blacksmith_inventory.buy(player, IronSword, 20),
    "2": lambda: blacksmith_inventory.buy(player, SteelSword, 50),
    "3": lambda: blacksmith_inventory.buy(player, MithrilSword, 100),
    }


    inn.connections = {
    "2": town
    }
    inn.actions ={
        "1": lambda: inn.rest(player)
    }
    
    
    apothecary.connections = {
            "1": apothecary_inventory,
            "2": town
    }


    
    apothecary_inventory.connections = {
            "2": apothecary
    }
    apothecary_inventory.actions = {
            "1": lambda: apothecary_inventory.buy(player)
    }

    
    elewyn.connections = {
        "1": boar_fields,
        "2": janas_farm,
        "3": defias_hideout
    }

    
    boar_fields.connections = {
        "2": elewyn,
        "3": town
    }
    boar_fields.actions = {
        "1": lambda: boar_fields.explore(player)
    }


    
    janas_farm.connections = {
        "2": elewyn,
        "3": town
    }
    janas_farm.actions = {
        "1": lambda: janas_farm.explore(player)
    }
    

    
    defias_hideout.connections = {
        "2": elewyn,
        "3": town
    }
    defias_hideout.actions = {
        "1": lambda: defias_hideout.explore(player)
    }

    
    duskwood.connections = {
        "1": haunted_orchard,
        "2": crypt,
        "3": stitches
    }


    
    haunted_orchard.connections = {
        "2": duskwood,
        "3": town
    }
    haunted_orchard.actions = {
        "1": lambda: haunted_orchard.explore(player)
    }


    
    crypt.connections = {
        "2": duskwood,
        "3": town
    }
    crypt.actions = {
        "1": lambda: crypt.explore(player)
    }

    
    stitches.connections = {
        "2": duskwood,
        "3": town
    }
    stitches.actions = {
        "1": lambda: stitches.send_it(player)
    }


    
    stranglethorn_vale.connections = {
        "1": raptor_pit,
        "2": troll_ruins,
        "3": zul_juns_lair
    }


    
    raptor_pit.connections = {
        "2": stranglethorn_vale,
        "3": town
    }
    raptor_pit.actions = {
        "1": lambda: raptor_pit.explore(player)
    }

    
    troll_ruins.connections = {
        "2": stranglethorn_vale,
        "3": town
    }
    troll_ruins.actions = {
        "1": lambda: troll_ruins.explore(player)
    }
    
    
    zul_juns_lair.connections = {
        "2": stranglethorn_vale,
        "3": town
    }
    zul_juns_lair.actions = {
        "1": lambda: zul_juns_lair.send_it(player)
    }

    
    black_rock_depths.connections = {
        "1": grim_guzzler,
        "2": infernum,
        "3": ragnaros
    }

    
    grim_guzzler.connections = {
        "3": black_rock_depths,
        "4": town
    }
    grim_guzzler.actions = {
        "1": lambda: grim_guzzler.explore(player),
        "2": lambda: grim_guzzler.have_a_drink(player)
    }
    
    
    infernum.connections = {
        "2": black_rock_depths,
        "3": town
    }
    infernum.actions = {
        "1": lambda: infernum.send_it(player)
    }

    
    ragnaros.connections = {
        "2": black_rock_depths,
        "3": town
    }
    ragnaros.actions = {
        "1": lambda: ragnaros.send_it(player)
    }

    return town

