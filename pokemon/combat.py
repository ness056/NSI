from random import randint, choice
from math import floor

from pokemon import gain_exp
from player import clear_screen, custom_input, wait_for_enter, show_inventory, show_team

Faiblesse = {   'normal' : ['combat'],
                'feu' : ['eau','sol','roche'],
                'eau' : ['elec','plante',],
                'plante' : ['feu','glace','poison','vol','insecte'],
                'elec' : ['sol'],
                'glace' : ['feu','combat','roche'],
                'combat' : ['vol','psy'],
                'poison' : ['sol','psy','insecte'],
                'sol' : ['eau','plante','glace'],
                'vol' : ['elec','glace','roche'],
                'psy' : ['insecte'],
                'insecte' : ['feu','poison','combat'],
                'roche' : ['eau','plante','roche','combat'],
                'spectre' : ['spectre'],
                'dragon' : ['glace','dragon']}

Resistance = {  'normal' : ['spectre'],
                'feu' : ['feu','plante','insecte'],
                'eau' : ['feu','eau','glace'],
                'plante' : ['eau','plante','elec','sol'],
                'elec' : ['elec','vol'],
                'glace' : ['glace'],
                'combat' : ['roche','insecte'],
                'poison' : ['plante','combat','poison'],
                'sol' : ['roche','poison'],
                'vol' : ['combat','plante','insecte'],
                'psy' : ['psy','combat'],
                'insecte' : ['plante','combat','sol'],
                'roche' : ['normal','feu','poison','vol'],
                'spectre' : ['normal','combat','poison','insecte'],
                'dragon' : ['feu','eau','plante','elec']}


def verif_ko(equipe)->bool:
    for pokemon in equipe :
        if pokemon["pv"] > 0 :
            return False
    return True




def stab(pokemon,attaque) -> int:
    if pokemon["type"] == attaque["Type"]:
        return 1.2
    else : 
        return 1




def critique(pokemon):
   critique = randint(1,100)   
   if critique > 80 :
       return 2
   else : 
       return 1
   

def verif_type(type_pokemon,attaque):
    type_attaque = attaque["Type"]
    if type_attaque in Faiblesse[type_pokemon] :
        return 2
    elif type_attaque in Resistance[type_pokemon] :
        return 0.5
    else:
        return 1

def degat_attaque(pokemon_attaquant,pokemon_defenseur,attaque):

    STAB = stab(pokemon_attaquant,attaque)

    critique2 = critique(pokemon_attaquant)

    type1 = verif_type(pokemon_defenseur['type'][0],attaque)
    type2 = 1
    
    if len(["type"]) == 2 :
        type2 = verif_type(pokemon_defenseur['type'][1],attaque)
    
    degat = ((((((2*pokemon_attaquant['niveau']*critique2)/5)+2)*attaque['Degats']*(pokemon_attaquant['attaque']/pokemon_defenseur['defense']))/50)+2)*STAB*type1*type2*(randint(217, 255)/255)
    
    return floor(degat)


def combat(joueur: dict, equipe_adversaire: list, sauvage: bool) -> bool:
    """
    Fonction de combat principale ou se passe toutes les étapes d'un combat pokemon
    paramètre d'entrée :
    joueur : correspond au dictionnaire player
    equipe_adversaire : correspond à l'équipe jouée par l'adversaire
    sauvage : True si c'est un combat contre un pokemon sauvage, False si c'est contre un dresseur.
    """

    i_poke_j = 0 # Indice du pokemon actif du joueur
    i_poke_a = 0 # poke actif bot. = -1 pour affiché le pokémon
    capture = False # si True -> poke capturé
    fuite = False # si True -> joueur fuit
    tour_joueur = True # si True -> tour joueur, tour bot sinon
    equipe_joueur = joueur["pokemons"]

    clear_screen()
    print(f"Votre pokémon actif est {equipe_joueur[i_poke_j]["nom"]}, lvl {equipe_joueur[i_poke_j]["niveau"]}")
    print(f"Le pokémon actif adverse est {equipe_adversaire[i_poke_j]["nom"]}, lvl {equipe_adversaire[i_poke_j]["niveau"]}")
    wait_for_enter()
    clear_screen()

    while not verif_ko(equipe_joueur) and not verif_ko(equipe_adversaire) and not capture and not fuite:
        while equipe_joueur[i_poke_j]["pv"] <= 0:
            i_poke_j += 1
            if len(equipe_joueur) >= i_poke_j:
                i_poke_j = -1
    
        while equipe_adversaire[i_poke_a]["pv"] <= 0:
            i_poke_a += 1
            clear_screen()
            print("L’adversaire a changé de pokémon !")
            print(f"Il joue désormait avec {equipe_adversaire[i_poke_a]["nom"]} !")
            wait_for_enter()

        poke_actif_j = equipe_joueur[i_poke_j] # poke actif du joueur
        poke_actif_a = equipe_adversaire[i_poke_a] # poke actif du bot

        if poke_actif_j["vitesse"] > poke_actif_a["vitesse"]:
            tour_joueur = True
        else:
            tour_joueur = False

        if tour_joueur == False:
            attaque = choice(poke_actif_a["attaques"])
            degat = degat_attaque(poke_actif_a, poke_actif_j, attaque)
            poke_actif_j["pv"] -= degat
            clear_screen()
            print("L’adversaire a utilité l'attaque " + attaque["Nom"])
            if poke_actif_j["pv"] < 0:
                poke_actif_j["pv"] = 0
                print(f"Votre pokémon {poke_actif_j["nom"]} est KO !")
            else:
                print(f"Votre pokémon {poke_actif_j["nom"]} a pris {degat} dégâts et il lui reste {poke_actif_j["pv"]}pv")
            wait_for_enter()

        tour_fini = False
        while not tour_fini and poke_actif_j["pv"] > 0:
            clear_screen()
            print(f"Votre pokemon: {poke_actif_j["nom"]}, {poke_actif_j["pv"]}/{poke_actif_j["pv_max"]}pv, lvl {poke_actif_j["niveau"]}.")
            print(f"Pokemon adverse: {poke_actif_a["nom"]}, {poke_actif_a["pv"]}/{poke_actif_a["pv_max"]}pv, lvl {poke_actif_a["niveau"]}.")
            print("Sélectionnez l'action que vous voulez faire:\n")
            print("Attaquer (1)")
            print("Ouvrir sac (2)")
            print("Changer Pokemon (3)")
            print("Fuir (4)")

            i = custom_input("Entrez le nombre correspond à votre choix", int_expected = True, input_expected = (1,2,3,4))
            if i == 1: # Attaque
                clear_screen()
                print("Sélectionnez l'attaque que vous voulez faire:\n")
                print("Revenir en arrière (0)")
                for i in range(len(poke_actif_j["attaques"])):
                    attaque = poke_actif_j["attaques"][i]
                    print(f"{attaque["Nom"]} ({i + 1}): {attaque["Degats"]} dégâts de type {attaque["Type"]}")
                
                i = custom_input("Entrez le nombre correspond à votre choix", int_expected=True, input_expected=tuple(range(0,len(poke_actif_j["attaques"]) + 1)))

                if i != 0:
                    attaque = poke_actif_j["attaques"][i - 1]
                    degat = degat_attaque(poke_actif_j, poke_actif_a, attaque)
                    poke_actif_a["pv"] -= degat
                    clear_screen()
                    if poke_actif_a["pv"] < 0:
                        poke_actif_a["pv"] = 0
                        print(f"Le pokémon ennemi {poke_actif_a["nom"]} est KO !")
                    else:
                        print(f"Le pokémon ennemi {poke_actif_a["nom"]} a pris {degat} dégâts et il lui reste {poke_actif_a["pv"]}pv")
                    
                    wait_for_enter()
                    tour_fini = True

            elif i == 2:
                item = show_inventory(joueur, True)
                clear_screen()

                if item != None and joueur["inventory"][item] > 0:
                    if item == "pokeball" and sauvage == False:
                        print("Vous ne pouvez pas capturer les pokémons des dresseur")
                        wait_for_enter()
                    elif item == "pokeball":
                        p = (1 - (2/3) * (poke_actif_a['pv']/poke_actif_a['pv_max'])) * 255 + randint(0,90)
                        if p >= 255:
                            capture = True
                        else:
                            print("50€ de perdu !")
                            wait_for_enter()
                        joueur['inventory']["pokeball"] -= 1
                        tour_fini = True

                    elif item == "potion":
                        index = show_team(joueur, True)
                        poke = joueur["pokemons"][index]
                        poke["pv"] += 20
                        if poke["pv"] > poke["pv_max"]:
                            poke["pv"] = poke["pv_max"]
                        print("Pokémon soigner !")
                        wait_for_enter()
                        joueur['inventory']["potion"] -= 1
                        tour_fini = True

            elif i == 3:
                index = show_team(joueur, True)
                if index != None:
                    i_poke_j = index
                    poke_actif_j = equipe_joueur[i_poke_j]
                    clear_screen()
                    print("Pokémon active changé !")
                    wait_for_enter()
                    tour_fini = True

            elif i == 4:
                if sauvage == True:
                    fuite = True
                    tour_fini = True
                else:
                    print("Vous ne pouvez pas fuir un combat contre un dresseur, affronte ton destin maintenant !")

        if tour_joueur == True and capture == False and fuite == False and poke_actif_a["pv"] > 0:
            attaque = choice(poke_actif_a["attaques"])
            degat = degat_attaque(poke_actif_a, poke_actif_j, attaque)
            poke_actif_j["pv"] -= degat
            clear_screen()
            print("L’adversaire a utilité l'attaque " + attaque["Nom"])
            if poke_actif_j["pv"] < 0:
                poke_actif_j["pv"] = 0
                print(f"Votre pokémon {poke_actif_j["nom"]} est KO !")
            else:
                print(f"Votre pokémon {poke_actif_j["nom"]} a pris {degat} dégâts et il lui reste {poke_actif_j["pv"]}pv")
            wait_for_enter()

    won = False
    clear_screen()
    if fuite:
        print("Gros lâche !")
        print("Vous n'avez gagné aucune récompense...")

    elif capture:
        if len(joueur["pokemons"]) >= 6:
            list.append(joueur['stored_pokemons'], equipe_adversaire[0])
        else:
            list.append(joueur["pokemons"], equipe_adversaire[0])
        print(f"Vous avez capturé un {equipe_adversaire[0]["espece"]} !")
        won = True

    elif verif_ko(equipe_joueur):
        print("Tout vos pokémon son mort ! Vous être nul !")
        print("Vous n'avez gagné aucune récompense...")

    elif verif_ko(equipe_adversaire):
        gain_exp(equipe_joueur[i_poke_j], equipe_adversaire[0], sauvage)
        joueur["money"] += 50
        print("Vous avez gagné. Vous êtes le GOAT !")
        print("Vous avez gagné 50€.")
        won = True

    wait_for_enter()
    return won