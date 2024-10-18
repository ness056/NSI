from random import randint

## Functions
## III.1

def volume_cube(c):
    return c ** 3

print(volume_cube(3))
print(volume_cube(3.5))

## III.2

def B_nb(nb):
    return "B" + str(nb)

print(B_nb(7) == "B7")
print(B_nb(B_nb(52)))

## V.2
## 1)

def sqrt(n: float) -> float:
    return n ** 0.5

print(sqrt(15129))

## 2)

def pythagore(a: float, b: float) -> float:
    return sqrt(a ** 2 + b ** 2)

print(pythagore(3, 4))

## 3)

def six_faces() -> int:
    return randint(1, 6)

print(six_faces())

## VI.1

def aire_rect(larg: float, long: float) -> float:
    return larg * long

def aire_boite(a: float, b: float, c: float) -> float:
    return aire_rect(a, b) * 2 + aire_rect(b, c) * 2 + aire_rect(a, c) * 2

print(aire_boite(3, 4, 5))

## VI.3

def IMC(masse: float, taille: float) -> float:
    """
    Renvoie l'IMC en fonction de la masse et de la taille.
    Paramètres:
        masse: float positif en kg
        taille: float positif en mètre
    Valeur renvoyé:
        float positif
    """
    return masse / taille ** 2

print(IMC(53, 1.65))


## Les structures conditionnelles
## I.3
## 1)

def entre_8_12(n: float) -> bool:
    if n >= 8 and n <= 12:
        return True
    return False

def entre_8_12_no_if(n: float) -> bool:
    return n >= 8 and n <= 12

## 2)

def est_neveu_donald(name: str) -> bool:
    if name == "Riri" or name == "Fifi" or name == "Loulou":
        return True
    return False

def un_bon_nombre(n: float) -> bool:
    if n % 2 == 0 and (n < 51 or n > 81):
        return "Bravo"
    return "Non!"


## IV.1
## App 2

def is_7_multiple(n: int) -> bool:
    return n % 7 == 0

print(is_7_multiple(0))
print(is_7_multiple(6))
print(is_7_multiple(7))
print(is_7_multiple(8))

## App 3

def gagne(point: int) -> str:
    if point >= 10:
        return "Gagné!"
    else:
        return "Perdu..."

print(gagne(4))
print(gagne(10))
print(gagne(15))


## App 4

def analyse_temperature(t: float) -> str:
    if t <= 14:
        return "Il fait froid !"
    elif t >= 26:
        return "Il fait chaud !"
    else:
        return "Il fait bon !"

## App 5

def max_3(a: float, b: float, c: float):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_3(10, 12, 4))

## V Exercices
## V.1

def positif_ou_nul(n: float) -> bool:
    return n >= 0

## V.2

def terrain_valid(long: float, larg: float) -> bool:
    return long > 90 and long < 120 and larg > 45 and larg < 90

## V.3

def est_bissextile(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

## Les chaines de caractères
## I Généralités
## I.3

def longest_str(a: str, b: str) -> str:
    if len(a) > len(b):
        return a
    else:
        return b
    
a = "Hello world!"
b = "Bonjour le monde !"


print(longest_str(a, b))

## II.2
## App 2

def immatriculation(c1: str, nb: int, c2: str) -> str:
    return c1 + "-" + str(nb) + "-" + c2

print(immatriculation("LC", 546, "GB"))

## App 4

def lettre(i: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[i - 1]

print(lettre(1), lettre(26))

## App 5

def rand_consonne() -> str:
    consonnes = "bcdfghjklmnpqrstvwxz"
    return consonnes[randint(0, len(consonnes) - 1)]

print(rand_consonne())

## App 6

def contient_a(prenom: str) -> bool:
    return "a" in prenom.lower()

## App 7

text = """
Anton Voyl n'arrivait pas à dormir. Il alluma. Son Jaz marquait minuit vingt. Il poussa un profond soupir, s'assit dans son lit, s'appuyant sur son polochon. Il prit un roman, il l'ouvrit, il lut; mais il n'y saisissait qu'un imbroglio confus, il butait à tout instant sur un mot dont il ignorait la signification.  
Il abandonna son roman sur son lit. Il alla à son lavabo ; il mouilla un gant qu'il passa sur son front, sur son cou.    
Son pouls battait trop fort. Il avait chaud. Il ouvrit son vasistas, scruta la nuit. Il faisait doux. Un bruit indistinct montait du faubourg. Un carillon, plus lourd qu'un glas, plus sourd qu'un tocsin, plus profond qu'un bourdon, non loin, sonna trois coups. Du canal Saint-Martin, un clapotis plaintif signalait un chaland qui passait.  
Sur l'abattant du vasistas, un animal au thorax indigo, à l'aiguillon safran, ni un cafard, ni un charançon, mais plutôt un artison, s'avançait, traînant un brin d'alfa. Il s'approcha, voulant l'aplatir d'un coup vif, mais l'animal prit son vol, disparaissant dans la nuit avant qu'il ait pu l'assaillir.
"""
print(text.count("e"))

## App 8

def number_voyelle(s: str) -> int:
    t = 0
    lower = s.lower()
    voyelle = "aeiuy"
    for v in voyelle:
        t += lower.count(v)
        
## VI.2
## App 8

p1 = "Patrick Balkany"
p2 = "Nicolas Sarkozy"
p3 = "Mister MV"

print(p1)
print(p2)
print(p3)

print(p1, p2, p3)

print(p1, end = " ")
print(p2, end = " ")
print(p3)

print(p1, p2, p3, sep = "\n")


## App 9

def est_paire(n: int):
    return n % 2 == 0

print("Le nombre 8 est " + "pair." if est_paire(8) else "impair.")

## App 10

def premiere_lettre(mot: str):
    return mot[0]

print("La première lettre du mot artichaut est " + premiere_lettre("artichaut") + " !")

## App 11

def etat_eau(t: int) -> str:
    if t < 0:
        return "SOLIDE"
    elif t > 100:
        return "GAZEUX"
    else:
        return "LIQUIDE"
    
temp = input("Donnez une temperature:")
print("A " + str(temp) + " eau est " + etat_eau(int(temp)))

## Exercice 1

def rand_voyelle() -> str:
    voyelles = "aeuiy"
    return voyelles[randint(0, len(voyelles) - 1)]
    
def rand_consonne() -> str:
    consonnes = "bcdfghjklmnpqrstvwxz"
    return consonnes[randint(0, len(consonnes) - 1)]

def rand_prenom() -> str:
    return rand_consonne() + \
        rand_voyelle() + \
        rand_consonne() + \
        rand_voyelle() + \
        rand_consonne()
        
print(rand_prenom())
print(rand_prenom())
print(rand_prenom())

##IV - applications

## Application 1
def char_iso(char: str) -> str:
    return hex(ord(char))

print(char_iso("t"))

## Application 2
name = input("Entrez votre nom: ")
if name.lower().startswith("b"):
    print("Votre prenom commence effectivement par b.")
else:
    print("Votre prenom ne commence pas par b.")


## Listes
## II

## Application 1
jours_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
premier_jour = jours_semaine[0]
print(premier_jour)
jours_semaine.append("dimanche")
jours_semaine[1] = "Tuesday"
print(len(jours_semaine))

## Application 2
nombres_entiers = []
nombres_entiers.append(1)
nombres_entiers.append(4)
nombres_entiers.append(9)
nombres_entiers = []
for i in range(20):
    nombres_entiers.append((i + 1) ** 2)
carre_15 = nombres_entiers[14]

## Application 3
## Il affiche le carré des 5 premiers nombres entiers

## Application 4
## 1) Il affiche chaque char de la liste avec son index
## 2) On ne pourrait pas afficher l'index des valeurs

## Application 5
liste_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print(*liste_jours, sep = "\n")

for s in liste_jours:
    print(s[0])

## Application II.1
"""
Les lignes 3 et 4 sont des créations de listes, la première contient
6 mots en français, la deuxième contient les même mots en anglais

La ligne 10 donne un nombre aléatoire entre 0 et 5, 
"""