from ui import clear
from time import sleep

animation_speed = 0.05

# cases:
#     "": case normal
#     "m": mur
#     "R": rocher
#     "p": portail/porte/sortie
#     "o": eau
#     "h": haute herbe
#     "d": dresseur
#     "f": falaise
#     "r": pierre
#     "a": arbuste
#     "I": infirmière
#     "V": vendeur
#     "N": pnj

cell_properties = {
    "solide": { "m": True, "R": True, "o": True, "d": True, "r": True,
                "a": True, "I": True, "V": True, "N": True, "": False,
                "p": False,"h": False,"a": False,"f": False }
}

## Dictonaire de toutes les zones
zones = {
    "test1": (
        ("R", "R", "R", "R", "R", "R", "R", "R", "R"),
        ("R", "",  "",  "",  "",  "",  "",  ("N", "Bonjour mon ami !"),  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "f", "f", "f", "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "o", "o", "o", "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  ("p", "test2", 3, 3),  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "R", "R", "R", "R", "R", "R", "R", "R")
    ),
    "test2": (
        ("m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  ("p", "test1", 1, 1),  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "f", "f", "f", "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "o", "o", "o", "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"),
        ("m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m")
    )
}

def get_zone_tuple(zone: str) -> tuple:
    return zones[zone]

# direction_vector doit être une list de deux int, un égal à 0
#   l'autre égal soit à -1 soit à 1
def move_player(player, distance: int, direction_vector: list) -> str:
    zone_tuple = get_zone_tuple(player["zone"])
    position = player["position"]
    x, y = position[0], position[1]
    x_, y_ = direction_vector[0], direction_vector[1]

    i = 1
    while i <= distance:
        cell = zone_tuple[x + x_ * i][y + y_ * i]
        cell_name = cell
        if type(cell) == tuple:
            cell_name = cell[0]

        if cell_properties["solide"][cell_name]:
            return
        elif cell_name == "f" and x_ != 1:
            return
        elif cell_name == "f" and x_ == 1:
            i = i + 1
        elif cell_name == "p":
            player["zone"] = cell[1]
            position[0] = cell[2]
            position[1] = cell[3]
            return

        position[0] = x + x_ * i
        position[1] = y + y_ * i
        show_zone(player)
        if i != distance:
            sleep(animation_speed)

        i = i + 1

def check_interaction(player):
    zone_tuple = get_zone_tuple(player["zone"])
    

def show_zone(player):
    clear()

    pos = player["position"]
    for x, column in enumerate(get_zone_tuple(player["zone"])):
        for y, cell in enumerate(column):
            cell_name = cell
            if type(cell) == tuple:
                cell_name = cell[0]
            
            if x == pos[0] and y == pos[1]:
                print("J", end = "")
            elif cell_name == "":
                print(" ", end = "")
            else:
                print(cell_name, end = "")
        print()



player = {
    "zone": "test1",
    "position": [1, 1]
}

show_zone(player)
while(True):
    i = input()
    direction = i[:1]
    amount = 1
    try:
        amount = int(i[1:])
    except:
        pass


    v = [0, 0]
    if direction == "z":
        v = [-1, 0]
    elif direction == "s":
        v = [1, 0]
    elif direction == "q":
        v = [0, -1]
    elif direction == "d":
        v = [0, 1]
    move_player(player, amount, v)
    show_zone(player)