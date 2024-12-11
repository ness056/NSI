from zone import show_zone, check_interaction, move_player
from player import new_player, show_intro, custom_input, show_menu

player = new_player()

show_intro(player)

# Boucle principale du jeu.
# Gère les actions quand le joueur est sur la map.
exit = False
while(not exit):
    show_zone(player)
    i = custom_input()
    first_char = i[:1]
    amount = 1
    try:
        amount = int(i[1:])
    except:
        pass

    v = [0, 0]
    if first_char == "m":
        exit = show_menu(player)


    elif first_char == "e":
        check_interaction(player)

    elif first_char == "z":
        v = [-1, 0]
    elif first_char == "s":
        v = [1, 0]
    elif first_char == "q":
        v = [0, -1]
    elif first_char == "d":
        v = [0, 1]

    if v != [0, 0]:
        move_player(player, amount, v)