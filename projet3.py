## Louis Vey
## Projet 3 : Le jeu du nombre mystère

import sys
from random import randint
from enum import Enum
import math

class Window(Enum):
    MAIN = 1
    CONFIG = 2
    CONFIG_MODIFY = 3
    ASK_GUESS = 4
    ASK_SECRET_NUMBER = 5
    ASK_IS_CORRECT = 6
    END_SCREEN = 7
    
class GameMode(Enum):
    PLAYER_GUESS = 1
    COMPUTER_GUESS = 2
    TWO_PLAYERS = 3

class Winner(Enum):
    PLAYER = 1
    COMPUTER = 2
    PLAYER1 = 3
    PLAYER2 = 4

game_mode = None
secret_number = None
winner = None
guess_left = None

# Pour le mode ordi devine
computer_guess = None
min_computer_guess = None
max_computer_guess = None

# Pour le mode 2 joueurs
secret_number2 = None
turn = None

current_window = Window.MAIN
previous_window = None

selected_config = None

invalid_input_print = None

# 0 signifie pas de limite
guess_limit = {"name": "la limite de coups", "value": 0}
min_number = {"name": "le nombre minimum", "value": 1}
max_number = {"name": "le nombre maximum", "value": 100}

def get_current_player_name() -> str:
    if turn == 1:
        return "joueur 1"
    else:
        return "joueur 2"

def is_int(n: any) -> bool:
    try:
        i = int(n)
        if i != float(n):
            return False
        return True
    except:
        return False

def change_window(window: Window):
    global previous_window, current_window
    previous_window = current_window
    current_window = window

def clear():
    # \033[ est un caractère special qui permet de controller un terminal
    # \033[H deplace le curseur au début du terminal
    # \033[J supprime tout le text entre le curseur et la fin
    print("\033[H\033[J", end="")

def init_game():
    global guess_left, turn, min_computer_guess, max_computer_guess
    min_computer_guess = min_number["value"]
    max_computer_guess = max_number["value"]
    turn = 1
    if guess_limit["value"] == 0:
        guess_left = math.inf
    else:
        guess_left = guess_limit["value"]
    clear()

def reset_game():
    global game_mode, secret_number, guess_left, turn
    game_mode = None
    secret_number = None
    guess_left = None
    turn = None
    change_window(Window.MAIN)
    
def set_invalid_input(msg):
    global invalid_input_print
    invalid_input_print = ">> entrée invalide ({}).".format(msg)

def print_main_menu():
    print(
"""Bonjour dans le jeu du nombre mystère !

Pour terminer le programme, écrivez "exit" à n'import quel moment,
pour revenir au menu principal, écrivez "menu",
pour revenir en arrière écrivez "back".

Rentrez un nombre pour selectionner le mode de jeu:
    (0) Menu de configuration
    (1) Le joueur devine le nombre
    (2) L'ordinateur devine le nombre
    (3) Mode 2 joueurs""")
    
def response_main_menu(r: str):
    global game_mode, secret_number
    if r == "0":
        change_window(Window.CONFIG)
    elif r == "1":
        game_mode = GameMode.PLAYER_GUESS
        secret_number = randint(min_number["value"], max_number["value"])
        change_window(Window.ASK_GUESS)
        init_game()
    elif r == "2":
        game_mode = GameMode.COMPUTER_GUESS
        change_window(Window.ASK_SECRET_NUMBER)
        init_game()
    elif r == "3":
        game_mode = GameMode.TWO_PLAYERS
        change_window(Window.ASK_SECRET_NUMBER)
        init_game()
    else:
        set_invalid_input("Doit être un nombre entre 0 et 3")
    
def print_config_menu():
    global guess_limit, min_number, max_number
    print(
"""Menu de configuration

Rentrez un nombre pour selectionner un paramètre à changer:
    (1) Limite de coups, {} (0 = pas de limit)
    (2) Nombre minimum, {}
    (3) Nombre maximum, {}"""
    .format(guess_limit['value'], min_number['value'], max_number['value']))

def response_config_menu(r: str):
    global selected_config
    if r == "1":
        selected_config = guess_limit
        change_window(Window.CONFIG_MODIFY)
    elif r == "2":
        selected_config = min_number
        change_window(Window.CONFIG_MODIFY)
    elif r == "3":
        selected_config = max_number
        change_window(Window.CONFIG_MODIFY)
    else:
        set_invalid_input("Doit être un nombre entre 1 et 3")

def print_config_modify_menu():
    global guess_limit, min_number, max_number, selected_config
    print(
"""Entrez un nombre pour changer {}, actuellement égal à : {}"""
    .format(selected_config["name"], selected_config["value"]))

def response_config_modify_menu(r: str):
    if is_int(r):
        selected_config["value"] = int(r)
        change_window(Window.CONFIG)
    else:
        set_invalid_input("Doit être un nombre entier.")

def decrease_guess_left():
    global guess_left, winner

def print_ask_guess():
    global min_number, max_number, game_mode
    s = "Entrez un nombre"
    if game_mode == GameMode.TWO_PLAYERS:
        s = "Le {} doit entrer un nombre".format(get_current_player_name())
    print(s + " entre {} et {}:".format(min_number["value"], max_number["value"]))

def response_ask_guess(r: str):
    global winner, game_mode, turn, guess_left
    if not is_int(r):
        set_invalid_input("Doit être un nombre entier.")
        return
    
    n = int(r)
    if n > secret_number:
        print("Le nombre mystère est plus petit.")
    elif n < secret_number:
        print("Le nombre mystère est plus grand.")
    else:
        change_window(Window.END_SCREEN)
        if game_mode == GameMode.PLAYER_GUESS:
            winner = Winner.PLAYER

        elif game_mode == GameMode.TWO_PLAYERS:
            if turn == 1:
                winner = Winner.PLAYER1
            else:
                winner = Winner.PLAYER2
        return
    
    # Pas de limite de guess dans le mode 2 joueurs
    if guess_left == math.inf or game_mode == GameMode.TWO_PLAYERS:
        return

    guess_left -= 1
    if guess_left == 0:
        change_window(Window.END_SCREEN)
        print("Vous avez utilisé tout vos essais")
        winner = Winner.COMPUTER
    else:
        print("Il vous reste {} essais".format(guess_left))

def print_ask_secret_number():
    global min_number, max_number, game_mode
    s = "Choisi le nombre mystère"
    if game_mode == GameMode.TWO_PLAYERS:
        s = "Le {} doit choisir son nombre mystère".format(get_current_player_name())
    print(s + " entre {} et {}.".format(min_number["value"], max_number["value"]))

def response_ask_secret_number(r: str):
    global min_number, max_number, secret_number, secret_number2, turn
    if not is_int(r):
        set_invalid_input("Doit être un nombre entier.")
        return

    n = int(r)
    if n < min_number["value"] or n > max_number["value"]:
        print("Vous devez choisir un nombre entre {} et {}".format(min_number["value"], max_number["value"]))
        return

    if game_mode == GameMode.COMPUTER_GUESS:
        secret_number = n
        change_window(Window.ASK_IS_CORRECT)

    elif game_mode == GameMode.TWO_PLAYERS:
        if turn == 1:
            secret_number = n
            turn = 2
        else:
            secret_number2 = n
            turn = 1
            change_window(Window.ASK_GUESS)


def print_ask_is_correct():
    global computer_guess, min_computer_guess, max_computer_guess
    computer_guess = (min_computer_guess + max_computer_guess) // 2
    print(
        "L'ordinateur a choisi le nombre {}. Indiquez si votre nombre est plus petit (1), plus grand (2) ou est le bon (3)."
        .format(computer_guess)
    )

def response_ask_is_correct(r: str):
    global computer_guess, min_computer_guess, max_computer_guess, winner, guess_left
    if not is_int(r):
        set_invalid_input("Doit être soit 1 soit 2.")
        return

    if (r == "1" and secret_number >= computer_guess) \
    or (r == "2" and secret_number <= computer_guess) \
    or (r == "3" and secret_number != computer_guess):
        print("Stop right there, criminal scum! Vous avez menti !")
        winner = Winner.COMPUTER
        change_window(Window.END_SCREEN)
        return

    if r == "1":
        max_computer_guess = computer_guess - 1
    elif r == "2":
        min_computer_guess = computer_guess + 1
    elif r == "3":
        winner = Winner.COMPUTER
        change_window(Window.END_SCREEN)
        return
    else:
        set_invalid_input("Doit être soit 1 soit 2")

    # Pas de limite de guess dans le mode 2 joueurs
    if guess_left == math.inf or game_mode == GameMode.TWO_PLAYERS:
        return

    guess_left -= 1
    if guess_left == 0:
        change_window(Window.END_SCREEN)
        print("L'ordinateur a utilisé tout ses essais.")
        winner = Winner.COMPUTER
    else:
        print("Il reste {} essais à l'ordinateur".format(guess_left))

def print_end_screen():
    global winner

    m = ""
    if winner == Winner.COMPUTER:
        m = "Vous avez perdu... Essayez encore, vous allez y arriver !"
    elif winner == Winner.PLAYER:
        m = "Vous avez gagné ! Bien jouer !"
    else:
        w = "Joueur 1"
        if winner == Winner.PLAYER2:
            w = "Joueur 2"
        m = "Le {} a gagné ! Bien jouer à lui !".format(w)

    print(
"""\n{}

Ecrivez n'importe quoi pour revenir au menu principale.
""".format(m))

def response_end_screen():
    reset_game()
    change_window(Window.MAIN)

def show_text():
    global current_window
    if current_window == Window.MAIN:
        print_main_menu()
    elif current_window == Window.CONFIG:
        print_config_menu()
    elif current_window == Window.CONFIG_MODIFY:
        print_config_modify_menu()
    elif current_window == Window.ASK_GUESS:
        print_ask_guess()
    elif current_window == Window.ASK_SECRET_NUMBER:
        print_ask_secret_number()
    elif current_window == Window.ASK_IS_CORRECT:
        print_ask_is_correct()
    elif current_window == Window.END_SCREEN:
        print_end_screen()
        
def get_response():
    global current_window, previous_window, selected_config, invalid_input_print
    r = input(">> ")
    invalid_input_print = None
    if r == "exit":
        sys.exit()
    elif r == "menu":
        change_window(Window.MAIN)
        if game_mode != None:
            reset_game()
        return
    elif r == "back" and previous_window != None:
        if game_mode == None:
            change_window(previous_window)
            return
        else:
            set_invalid_input("Vous ne pouvez pas utiliser cette commande pendant le jeu.")
    
    
    if current_window == Window.MAIN:
        response_main_menu(r)           
    elif current_window == Window.CONFIG:
        response_config_menu(r)
    elif current_window == Window.CONFIG_MODIFY:
        response_config_modify_menu(r)
    elif current_window == Window.ASK_GUESS:
        response_ask_guess(r)
    elif current_window == Window.ASK_SECRET_NUMBER:
        response_ask_secret_number(r)
    elif current_window == Window.ASK_IS_CORRECT:
        response_ask_is_correct(r)
    elif current_window == Window.END_SCREEN:
        response_end_screen()
        

if __name__ == "__main__":
    while(True):
        if game_mode == None:
            clear()
        
        show_text()
        
        if invalid_input_print != None:
            print(invalid_input_print)
        
        get_response()