from zone import show_zone, check_interaction, move_player

player = {
    "name": "Le meilleur",
    "inventory": {},
    "badges": [],
    "money": "0",
    "pokemons": [],
    "stored_pokemons": [],
    "zone": "test1",
    "position": [1, 1]
}

show_zone(player)
while(True):
    i = input()
    first_char = i[:1]
    amount = 1
    try:
        amount = int(i[1:])
    except:
        pass


    v = [0, 0]
    if first_char == "e":
        check_interaction(player)
    elif first_char == "z":
        v = [-1, 0]
    elif first_char == "s":
        v = [1, 0]
    elif first_char == "q":
        v = [0, -1]
    elif first_char == "d":
        v = [0, 1]
    move_player(player, amount, v)
    show_zone(player)