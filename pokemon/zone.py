from ui import clear

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
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "f", "f", "f", "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "o", "o", "o", "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "",  "",  "",  "",  "",  "",  "",  "R"),
        ("R", "R", "R", "R", "R", "R", "R", "R", "R")
    )
}

def get_zone_tuple(zone: str) -> tuple:
    return zones[zone]

# direction_vector doit être une list de deux int, un égal à 0
#   l'autre égal soit à -1 soit à 1
def move_player(zone: str, position: list, distance: int, direction_vector: list) -> str:
    tuple = get_zone_tuple(zone)
    allowed_distance = 0
    x, y = position[0], position[1]
    x_, y_ = direction_vector[0], direction_vector[1]

    while(allowed_distance < distance):
        i = allowed_distance + 1
        cell = tuple[x + x_ * i][y + y_ * i]
        if cell_properties["solide"][cell]:
            break
        else:
            allowed_distance = i

    position[0] = x + x_ * i
    position[1] = y + y_ * i


def show_zone(zone: str, player_position: tuple):
    clear()

    for x, column in enumerate(get_zone_tuple(zone)):
        for y, cell in enumerate(column):
            if x == player_position[0] and y == player_position[1]:
                print("J", end = "")
            elif cell == "":
                print(" ", end = "")
            else:
                print(cell, end = "")
        print()



player_pos = [1, 1]
zone = "test1"

while(True):
    show_zone(zone, player_pos)
    move_player(zone, player_pos, 1, [0, 1])

    input()