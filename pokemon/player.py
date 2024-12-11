from pokemon import CreerPokemon

shop_items = [
    {
        "name": "pokeball",
        "price": 50,
        "description": "Permet de capturer des pokemon sauvage en combat."
    },
    {
        "name": "potion",
        "price": 100,
        "description": "Soigne un pokemon en combat de 20hp."
    }
]

# Renvoie un dictionnaire joueur avec les informations par défaut.
def new_player() -> dict:
    inventory = {}
    for i in shop_items:
        inventory[i["name"]] = 5

    return {
        "inventory": inventory,
        "badges": [],
        "money": 1000,
        "pokemons": [],
        "stored_pokemons": [],
        "zone": "test1",
        "position": [1, 1]
    }

# Déclenche la séquence de sélection du pokemon starter et le tuto
def show_intro(player):
    list.append(player["pokemons"], CreerPokemon("Salamèche", 15))
    player["pokemons"][0]["exp"] = 100
    list.append(player["pokemons"], CreerPokemon("Dracofeu", 100))
    pass #TODO

# Efface la console
def clear_screen():
    # \033[H et \033[J sont des caractères spéciaux qui permettent de controller le terminal
    print("\033[H\033[J", end="")

# Une version modifiée et plus simple à utiliser de la fonction input
# Renvoie un str si tous les params sont à False
# Vérifie le type et renvoie un float si number_expected est à True
# Vérifie le type et renvoie un int si int_expected est à True, en ignorant number_expected
# Vérifie si l'input est l'un des input_expected si c'est un tuple non vide. 
#   Si number_expected ou int_expected et que input_expected n'est pas un tuple, l'input est convertie avant.
def custom_input(msg: str = "", number_expected: bool = False, int_expected: bool = False, input_expected: tuple = ()):
    if msg != "":
        msg += "\n"

    result = None
    while result == None:
        s = input(msg + ">> ")

        if int_expected == True:
            try:
                s = int(s)
            except:
                continue
        
        elif number_expected == True:
            try:
                s = float(s)
            except:
                continue

        if len(input_expected) == 0 or s in input_expected:
            result = s
    
    return result

# Affiche un texte d'attente et pause l'execution jusqu'à que le joueur appuis sur entré
def wait_for_enter():
    custom_input("\nAppuyer sur entré pour continuer...")

# Affiche le nom du png et les str contenues dans la liste un à un.
def show_dialog(name: str, texts: list):
    for text in texts:
        clear_screen()

        print(f"{name}:\n")
        print(text)
        wait_for_enter()

def show_shop(player):
    while(True):
        clear_screen()
        print(f"Bienvenue dans le shop pokemon ! Ravie de vous revoir !")
        print(f"Vous avez {player["money"]}€. Entrez 0 pour revenir en arrière.\n")
        print("Voulez vous acheter (1) ou vendre (2) des objets ?")
        action = custom_input("Entrez un nombre.", int_expected=True, input_expected=(0,1,2))
        if action == 0: return

        action_name = "acheter"
        if action == 2:
            action_name = "vendre"
        clear_screen()

        print(f"Vous avez {player["money"]}€. Entrez 0 pour revenir en arrière.")
        print(f"Sélectionnez un objet en entrant un nombre\n")
        for i in range(len(shop_items)):
            item = shop_items[i]
            print(f"{item["name"]} {item["price"]}€ ({i + 1}): {item["description"]}")

        i = custom_input(int_expected=True, input_expected=tuple(range(0, 1 + len(shop_items))))
        if i == 0: continue
        item = shop_items[i - 1]
        clear_screen()

        print(f"Vous avez {player["money"]}€. Entrez 0 pour revenir en arrière.")
        amount = custom_input(f"Entrez le nombre de {item["name"]} ({item["price"]}€) que vous voulez {action_name}.", int_expected=True)
        if amount == 0: continue
        total_price = amount * item["price"]
        clear_screen()

        if total_price > player["money"] and action == 1:
            print("Vous n'avez pas assez d'argent pour acheter ça !")
            wait_for_enter()
            continue

        if amount > player["inventory"][item["name"]] and action == 2:
            print(f"Vous n'avez pas assez de {item["name"]} pour en vendre autant !")
            wait_for_enter()
            continue

        print(f"Êtes vous sûr de vouloir {action_name} {amount} {item["name"]} pour un total de {total_price}€ ?")
        confirm = custom_input("Entrez 0 pour annuler et 1 pour confirmer", int_expected=True, input_expected=(0,1))
        if confirm == 0: continue

        if action == 1:
            total_price *= -1
        else:
            amount *= -1
        player["money"] += total_price
        player["inventory"][item["name"]] += amount

        print("Merci de faire affaire avec moi !")
        wait_for_enter()

# Affiche l'inventaire et permet au joueur de choisir un item si choice = True
def show_inventory(player, choice: bool = False) -> str | None:
    while(True):
        clear_screen()
        print("Votre inventaire:")
        print(f"Vous avez {player["money"]}€\n")
        for (name, amount) in dict.items(player["inventory"]):
            print(f"{name}: {amount}")

        if choice:
            item = custom_input("Entrez le nom d'un objet à choisir ou 'retour' pour revenir en arrière",\
                                input_expected = ("retour",) + tuple(dict.keys(player["inventory"])))
            if item == "retour":
                return None
            elif player["inventory"][item] <= 0:
                clear_screen()
                print("Vous devez choisir un objet que vous avez.")
                wait_for_enter()
                continue
            return item
        else:
            wait_for_enter()
            return
    
# Affiche l'inventaire et permet au joueur de choisir un poke si choice = True
# Renvoie None ou l'index du pokemon dans l'équipe
def show_team(player, choice: bool = False) -> int | None:
    while(True):
        clear_screen()
        print("Votre équipe:\n")
        print("Retour (0)")
        for i in range(len(player["pokemons"])):
            pokemon = player["pokemons"][i]
            index = ""
            if choice:
                index = f" ({i + 1})"
            print(f"{pokemon["nom"]}{index}: {pokemon["espece"]}, {pokemon["pv"]}/{pokemon["pv_max"]}pv, lvl {pokemon["niveau"]}, {pokemon["exp"]}xp")

        if choice:
            i = custom_input("Entrez le numéro d'un pokemon à choisir", int_expected=True, input_expected=tuple(range(1, 1 + len(player["pokemons"]))))
            if i == 0:
                return None
            elif player["pokemons"][i - 1]["pv"] <= 0:
                clear_screen()
                print("Vous devez choisir un pokemon vivant.")
                wait_for_enter()
                continue
            return i - 1
        else:
            wait_for_enter()
            return

# Affiche le menu principal, renvoie True si l'option quitter le jeu a été choisi.
def show_menu(player) -> bool:
    while(True):
        clear_screen()
        print(f"Menu principal:\n")
        print(f"Retour (0)")
        print(f"Quitter le jeu (1)")
        print(f"Inventaire (2)")
        print(f"Équipe pokémon (3)")
        print(f"Pokedex (4)")

        action = custom_input("Entrez un nombre.", int_expected=True, input_expected=(0,1,2,3,4))
        if action == 0:
            return False
        
        elif action == 1:
            return True
        
        elif action == 2:
            show_inventory(player, False)

        elif action == 3:
            show_team(player, False)

        elif action == 4:
            # show_pokedex(player) # TODO
            pass