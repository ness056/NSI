def clear():
    # \033[ est un caractère special qui permet de controller un terminal
    # \033[H deplace le curseur au début du terminal
    # \033[J supprime tout le text entre le curseur et la fin
    print("\033[H\033[J", end="")

def move_cursor(x: int, y: int):
    print("\033[%d;%dH" % (y, x))