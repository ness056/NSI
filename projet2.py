## Louis Vey
## Projet 2 : Analyseur de mots de passe

def check_lenght(pwd: str):
    l = len(pwd)
    r = True
    s = None
    if l <= 4:
        r = False
        s = "est trop court"
    elif l > 20:
        r = False
        s = "est trop long"
    return r, s

def check_upper(pwd: str):
    r = any(str.isupper() for str in pwd)
    s = None
    if not r:
        s = "n'a pas de majuscule"
    return r, s


def check_lower(pwd: str):
    r = any(str.islower() for str in pwd)
    s = None
    if not r:
        s = "n'a pas de minuscule"
    return r, s


def check_number(pwd: str):
    r = any(str.isdigit() for str in pwd)
    s = None
    if not r:
        s = "n'a pas de chiffre"
    return r, s

def check_space(pwd: str):
    r = any(not str.isspace() for str in pwd)
    s = None
    if not r:
        s = "a un espace"
    return r, s

if __name__ == "__main__":
    checks = [check_lenght, check_upper, check_lower, check_number, check_space]
    while(True):
        pwd = input("Entrez un mot de passe : ")
        problems = []
        for check in checks:
            r, s = check(pwd)
            if not r:
                problems.insert(len(problems), s)
        
        if len(problems) == 0:
            print("Mot de passe valide !")
        else:
            print("Mot de passe invalide,\nil ", end = "")
            print(*problems, sep = ",\n")
            continue
        
        pwd2 = input("Entrez le mot de passe à nouveau : ")
        if pwd == pwd2:
            print("Mot de passe correct !")
            break
        else:
            print("Mauvais mot de passe, recommencer")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        