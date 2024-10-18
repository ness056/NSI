from typing import List, Callable, Tuple
from random import choice
from time import sleep

type Grille = List[List[int]]

def grille_vide() -> Grille:
    colonne = [0 for _ in range(6)]
    return [colonne.copy() for _ in range(7)]

def affiche(g: Grille):
    clear()
    nums = "1 2 3 4 5 6 7"
    print(nums)
    for ligne in range(5, -1, -1):
        for colonne in range(7):
            n = g[colonne][ligne]
            out = "_ "
            if n == 1:
                out = "X "
            elif n == 2:
                out = "O "
            print(out, end = "")
        print("")
    print(nums)

def coup_possible(g: Grille, c: int) -> bool:
    if g[c][5] == 0:
        return True
    else:
        return False

def animation(g: Grille, j: int, c: int):
    g_ = g.copy()
    for l in range(5, -1, -1):
        if g_[c][l] != 0:
            break
        else:
            g_[c][l] = j
        
        affiche(g_)
        g_[c][l] = 0
        sleep(0.2)

def jouer(g: Grille, j: int, c: int):
    animation(g, j, c)
    i = g[c].index(0)
    g[c][i] = j

def is_pos_valid(pos: Tuple[int, int]) -> bool:
    return pos[0] >= 0 and pos[0] <= 6 and pos[1] >= 0 and pos[1] <= 5

## le param fn doit être une function qui prend un int qui
## varie entre -3 et 3 et doit être utilisé pour faire varier
## la ligne et/ou la colonne pour vérifier soit à l'horizontal,
## en vertical ou en diagonal, le premier élément du tuple est
## la colonne, le deuxième est la ligne
def win_check(g: Grille, j: int, fn: Callable[[int], Tuple[int, int]]):
    pos = fn(0)
    if g[pos[0]][pos[1]] != j:
        return False

    n = 1
    for i in range(3):
        pos = fn(i + 1)
        if is_pos_valid(pos) and g[pos[0]][pos[1]] == j:
            n += 1
        else:
            break
        
    for i in range(3):
        pos = fn(-i - 1)
        if is_pos_valid(pos) and g[pos[0]][pos[1]] == j:
            n += 1
        else:
            break

    if n >= 4:
        return True
    else:
        return False

def horiz(g: Grille, j: int, l: int, c: int) -> bool:
    return win_check(g, j, lambda s : (c + s, l))

def vert(g: Grille, j: int, l: int, c: int) -> bool:
    return win_check(g, j, lambda s : (c, l + s))

def diag_haut(g: Grille, j: int, l: int, c: int) -> bool:
    return win_check(g, j, lambda s : (c + s, l + s))

def diag_bas(g: Grille, j: int, l: int, c: int) -> bool:
    return win_check(g, j, lambda s : (c + s, l - s))

def victoire(g: Grille, j: int) -> bool:
    for c in range(7):
        for l in range(6):
            if horiz(g, j, l, c) or vert(g, j, l, c) or \
            diag_haut(g, j, l, c) or diag_bas(g, j, l, c):
                return True
    return False

def match_nul(g: Grille) -> bool:
    for c in range(7):
        if g[c][5] == 0:
            return False
    return True

def coup_aleatoire(g: Grille, j: int):
    coups = []
    for c in range(7):
        if coup_possible(g, c):
            coups.append(c)
    
    jouer(g, j, choice(coups))

# Vide la console
def clear():
    # \033[ est un caractère special qui permet de controller un terminal
    # \033[H deplace le curseur au début du terminal
    # \033[J supprime tout le text entre le curseur et la fin
    print("\033[H\033[J", end="")

def is_int(n: any) -> bool:
    try:
        i = int(n)
        if i != float(n):
            return False
        return True
    except:
        return False
            
def coup(g: Grille) -> int:
    while(True):
        s = input("Joueur " + str(j) + ", entrez une colone. ")
        if is_int(s):
            i = int(s)
            if i < 1 or i > 7:
                print("Vous devez entrer un nombre entre 1 et 7.")
            elif not coup_possible(g, i - 1):
                print("Cette colone est pleine.")
            else:
                return i - 1

if __name__ == "__main__":
    clear()

    # 0 = 2 joueurs qui jouent aléatoirement
    # 1 = 1 vrai joueur contre un qui joue aléatoirement
    # 2 = 2 vrais joueurs
    mode = 2
    
    g = grille_vide()
    j = 1
    winner = None

    while(True):
        affiche(g)

        if mode == 0 or (mode == 1 and j == 2):
            coup_aleatoire(g, j)
        else:
            c = coup(g)
            jouer(g, j, c)
        
        if victoire(g, j):
            winner = j
            break
        elif match_nul(g):
            break

        if mode == 0 or (mode == 1 and j == 2):
            input("Appuyez sur entré pour continuer.")

        if j == 1:
            j = 2
        else:
            j = 1

    affiche(g)
    if winner == None:
        print("Match nul ! C'est nul !")
    else:
        print("Le joueur " + str(winner) + " a gagné !")