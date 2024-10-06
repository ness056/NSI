## Louis Vey
## Projet 1: Logiciel d'apprentissage des tables de multiplication

import sys
from random import randint

def is_int(n: any) -> bool:
    try:
        i = int(n)
        if i != float(n):
            return False
        return True
    except:
        return False

def custom_input(s: str) -> str:
    r = input(s)
    if r == "fin":
        sys.exit()
    return r

def ask_mul(n: int, m: int) -> bool:
    r = None
    while(True):
        r = custom_input("Combien font {} x {} ? ".format(n, m))
        if not is_int(r):
            print("Erreur : {} n'est pas un nombre entier".format(r))
            continue
        break
        
    if n * m != int(r):
        print("Erreur : la réponse était {}".format(n * m))
        return False
    else:
        return True
    

def ask_table(n: int):
    right = 0
    for m in range(1, 11):
        if ask_mul(n, m):
            right += 1
            
    print("\nVotre note est de {}/10".format(right))
    
def normal():
    while(True):
        n = custom_input("Quelle table de multiplication voulez vous-réviser ? (écrivez \"fin\" a n'importe quel moment pour finir le programme) ")
        if not is_int(n):
            print("Erreur : {} n'est pas un nombre entier".format(n))
            continue
        ask_table(int(n))
        print("\nEssayons à nouveau !")
        
def random():
    while(True):
        ask_mul(randint(1, 11), randint(1, 11))
    
    
if __name__ == "__main__":
    while(True):    
        r = custom_input("Voulez vous choisir la table (1) ou avoir des multiplication aléatoire (2) ? Rentrez 1 ou 2 pour choisir. ")
        if r == "1":
            normal()
        elif r == "2":
            random()
        else:
            continue
        break
    
    
