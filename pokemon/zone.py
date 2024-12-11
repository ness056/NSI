from player import clear_screen, show_dialog, show_shop, wait_for_enter
from combat import combat
from pokemon import CreerPokemon
from random import randint, choice
from time import sleep

animation_speed = 0.05

# Les cases sont des str d'une seul lettre, sauf certaines qui ont des
#   propriétés unique et qui sont des listes. 
# cases:
#     "": case normal
#     "m": mur
#     "R": rocher
#     "p": portail/porte/sortie [cell_name, destination_zone_name, dest_x, dest_y]
#     "o": eau
#     "h": haute herbe
#     "d": dresseur             [cell_name, pnj_name, enabled, team: list[pokemon]]
#     "f": falaise
#     "r": pierre
#     "a": arbuste
#     "I": infirmière
#     "V": vendeur
#     "N": pnj                  [cell_name, pnj_name, dialog: list[str]]

# Hashmap des cases sur lesquels le joueur ne peut pas aller
solide_cells = {
    "m": True, "R": True, "o": True, "d": True, "r": True,
    "a": True, "I": True, "V": True, "N": True, "": False,
    "p": True, "h": False,"f": False 
}

cell_hits = {
    "m": "Mur",
    "R": "Rocher",
    "p": "Porte ou Portail",
    "o": "Eau",
    "h": "Haute herbe",
    "d": "Dresseur",
    "f": "Falaise",
    "r": "Pierre, entrez 'e' pour la pousser",
    "a": "Arbuste, entrez 'e' pour le couper avec 'Coupe'",
    "I": "Infirmière, entrez 'e' pour interagir",
    "V": "Vendeur, entrez 'e' pour interagir",
    "N": "JNP, entrez 'e' pour interagir"
}

patrick_balkany_team = [
    CreerPokemon("Salamèche", 10),
    CreerPokemon("Salamèche", 5),
    CreerPokemon("Dracofeu", 70)
]

## Dictionnaire de toutes les zones
zones = {
    "test1": {
        # Liste des noms des pokemons qui peuvent apparaître dans les hautes herbes de la zone
        "pokemons": [],
        # La range de niveau des pokemons qui apparaissent dans les hautes herbes de la zone
        "level_range": (5, 20),
        # Une liste à deux dimensions contenant des cases
        "map": (
            ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["R", "",  "",  "",  "",  "",  "",  ["N", "Le fou du village", ["Bonjour mon ami !"]],  "R"],
            ["R", "",  "",  "",  "",  "",  "",  "",  "R"],
            ["R", "",  "",  "",  "",  "f", "f", "f", "R"],
            ["R", "",  "",  "",  "",  "",  "",  "",  "R"],
            ["R", "",  "",  "",  "",  "",  "",  "",  "R"],
            ["R", "",  "",  "",  "",  "o", "o", "o", "R"],
            ["R", "",  "",  "",  "",  "",  "",  "",  "R"],
            ["R", "I", "",  "",  "",  "",  "",  "V", "R"],
            ["R", "",  "",  "",  "",  "",  "",  "",  "R"],
            ["R", ["N", "Le vieux random", ["Bonjour, je suis un PNJ de merde !", "Passe une bonne journée connard !"]],  "",  "",  "",  "",  "",  "",  "R"],
            ["R", "",  ["p", "test2", 3, 3],  "",  "",  "",  "",  "",  "R"],
            ["R", "",  "",  "",  "",  "",  "",  "",  "R"],
            ["R", "R", "R", "R", "R", "R", "R", "R", "R"]
        ),
    },
    "test2": {
        "pokemons": ["Salamèche"],
        "level_range": (5, 10),
        "map": (
            ["m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m"],
            ["m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "",  ["p", "test1", 1, 1],  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "",  "",  "",  "",  "",  "",  "a", "f", "f", "f", "m"],
            ["m", "",  "",  "",  "",  "",  "r", "",  "",  "",  "",  "m"],
            ["m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "",  "",  "",  "",  "",  "",  "",  "o", "o", "o", "m"],
            ["m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "",  "",  "",  "",  "",  "h", "h", "h", "h", "",  "m"],
            ["m", "",  "",  "",  "",  "",  "h", "h", "h", "h", "",  "m"],
            ["m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "",  ["d", "Patrick Balkany", True, patrick_balkany_team],  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "m"],
            ["m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m"]
        )
    }
}

# Renvoie False si la position est en dehors de la map ou True sinon
def is_valid_pos(map: list, pos: list) -> bool:
    if pos[0] < 0 or pos[0] >= len(map) or pos[1] < 0 or pos[1] >= len(map[pos[0]]):
        return False
    return True

# Vérifie si quelque chose peut ce déplacer sur une certaine case.
# direction_vector représente dans quel direction la chose s'est déplacer,
#   change le comportement des falaises.
# is_player représente si cette chose est le joueur ou pas,
#   change le comportement des falaises et des hautes herbes.
def can_move(cell_name: str, direction_vector: list, is_player: bool = True) -> bool:
    if solide_cells[cell_name] or \
        (cell_name == "h" and is_player == False) or \
        (cell_name == "f" and (direction_vector[0] != 1 or is_player == False)):
        return False
    return True
    
# Vérifie si il y a un dresseur dans les à au plus 5 cases de la position donnée.
# Si il y a un dresseur actif (qui n'a pas déjà été battu), lance le combat contre lui.
# Renvoie True si un combat à eu lieu ou False sinon.
def check_trainer(player, map: list, position: list) -> bool:
    for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        for i in range(1, 5):
            pos = [position[0] + i * v[0], position[1] + i * v[1]]
            if not is_valid_pos(map, pos): continue

            cell = map[pos[0]][pos[1]]
            if type(cell) != list or cell[0] != "d" or cell[2] == False:
                continue

            show_dialog(cell[1], ["Je te défis en duel !"])
            won = combat(player, cell[3], False)
            if won:
                clear_screen()
                print(f"{cell[1]}:\nT'es vraiment trop fort pour moi !")
                cell[2] = False
            wait_for_enter()

# Déplace le joueur de {distance} case dans la direction du vecteur.
# Si le joueur est bloqué par quelque une case, entre dans un portail ou
#   entre dans un combat, il s’arrêtera sans finir son déplacement.
# direction_vector doit être une list de deux int, un égal à 0 et
#   l'autre égal soit à -1 soit à 1
def move_player(player, distance: int, direction_vector: list):
    zone = zones[player["zone"]]
    map = zone["map"]
    position = player["position"]
    start_x, start_y = position[0], position[1]

    i = 1
    while i <= distance:
        next_pos = [start_x + direction_vector[0] * i, start_y + direction_vector[1] * i]
        if not is_valid_pos(map, next_pos): return

        cell = map[next_pos[0]][next_pos[1]]
        cell_name = cell
        if type(cell) == list:
            cell_name = cell[0]

        if cell_name == "p":
            player["zone"] = cell[1]
            position[0] = cell[2]
            position[1] = cell[3]
            return
        
        elif not can_move(cell_name, direction_vector):
            return

        elif cell_name == "f" and direction_vector[0] == 1:
            i = i + 1

        position[0] = start_x + direction_vector[0] * i
        position[1] = start_y + direction_vector[1] * i
        show_zone(player)

        if cell_name == "h" and randint(1, 10) == 1 and len(zone["pokemons"]) > 0:
            pokemon_name = choice(zone["pokemons"])
            level = randint(zone["level_range"][0], zone["level_range"][1])
            pokemon = CreerPokemon(pokemon_name, level)
            clear_screen()
            print(f"Un {pokemon["nom"]} sauvage est apparu !")
            wait_for_enter()
            combat(player, [pokemon], True)
            return

        if check_trainer(player, map, position):
            return

        if i != distance:
            sleep(animation_speed)

        i = i + 1

# Check les cases autour du joueur pour déclencher les interactions avec ces cases
# Cette fonction devrait être appeler quand le joueur entre "e"
def check_interaction(player):
    map = zones[player["zone"]]["map"]
    p_position = player["position"]
    for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        pos = [p_position[0] + v[0], p_position[1] + v[1]]
        if not is_valid_pos(map, pos): continue

        cell = map[pos[0]][pos[1]]
        cell_name = cell
        if type(cell) == list:
            cell_name = cell[0]

        if cell_name == "N":
            show_dialog(cell[1], cell[2])
            show_zone(player)

        elif cell_name == "V":
            show_shop(player)

        elif cell_name == "I":
            for p in player["pokemons"]:
                p["pv"] = p["pv_max"]
            show_dialog("Infirmière", ["Tous vos pokemons ont été soigné !"])

        elif cell_name == "a":
            has_attack = False
            for p in player["pokemons"]:
                for a in p["attaques"]:
                    if a["Nom"] == "Coupe":
                        has_attack = True
                        break
            
            if has_attack:
                map[pos[0]][pos[1]] = ""

        elif cell_name == "r":
            pos_ = [pos[0] + v[0], pos[1] + v[1]]
            if not is_valid_pos(map, pos_): continue

            cell_name_ = map[pos_[0]][pos_[1]]
            if type(cell_name_) == list:
                cell_name_ = cell_name_[0]

            if can_move(cell_name_, v, False):
                map[pos[0]][pos[1]] = ""
                map[pos_[0]][pos_[1]] = "r"

# Efface l'écran et affiche la zone où ce trouve le joueur
def show_zone(player):
    clear_screen()

    pos = player["position"]
    map = zones[player["zone"]]["map"]
    for x, column in enumerate(map):
        for y, cell in enumerate(column):
            cell_name = cell
            if type(cell) == list:
                cell_name = cell[0]
            
            if x == pos[0] and y == pos[1]:
                print("J", end = "")
            elif cell_name == "":
                print(" ", end = "")
            else:
                print(cell_name, end = "")
        print()

    print()
    showed_hits = []
    for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        pos_ = [pos[0] + v[0], pos[1] + v[1]]
        if not is_valid_pos(map, pos_): continue

        cell_name = map[pos_[0]][pos_[1]]
        if type(cell_name) == list:
            cell_name = cell_name[0]

        if cell_name in showed_hits or cell_name not in cell_hits:
            continue

        print(f"{cell_name}: {cell_hits[cell_name]}")
        showed_hits.append(cell_name)