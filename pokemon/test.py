aspico = {
    "name": "La sous merde",
    "specie": "aspico",
    "hp": 30,
    "types": ["poison", "insecte"]
}

pokemons = [
    {
        "name": "dracofeu",
        ...
    },
    {
        "name": "aspico"
    },
    {

    }
]

aspico["xp"] +=

attacks = [
    {
        "name": "deflagration",
        "type": "feu",
        "base_damage": 50
    }
]

def damage_pokemon(pokemon, attack):
    aspico.hp = aspico.hp - attack.damage

damage_pokemon(aspico, attacks[0])













list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3]

list1[5] = list2[0]

a = 10
b = 5

temp = a
a = b
b = temp


def combat():
    poke1 = {}
    poke2 = {}
    turn = None # 1 = tour du joueur, 2 = tour ordi
    if poke1["speed"] > poke2["speed"]:
        turn = 1
    else:
        turn = 2

    while is_pokemon_alive(poke1) and is_pokemon_alive(poke2):
        if turn == 1:
            player_turn()
            turn = 2
        elif turn == 2:
            computer_turn()
            turn = 1

position = [1, 2]

zone = {
    "ville1": [
        ["H", ("P", "ville2", 3, 5), "R"],
        ["H", "E"                  , "R"],
        ["R", "E"                  , "H"]
    ],
    "ville2": {
        ...        
    }
}

pokemon_base = {
    "Pikachou": {
        "espèce": "Pikachou",
        "pv": 39
    }
}

def create_pokemon(specie: str):
    pokemon_base[specie]["pv"]
    pokemon_b = pokemon_base[specie]
    base_pv = pokemon_b["pv"]

    pokemon = {
        "espèce": specie
    }

    return pokemon

def test():
    
    if True:
        a = 1
    else:
        a = 1.5

    print(a)

pokemon_sauvage = create_pokemon("pikachou")

test = ["a", "b", "c"]

for item in test:
    pass

for index in range(len(test)):
    pass


exit = False

while(exit == False):
    input()

    déplace le joueur, ouvre un menu...

    update écran