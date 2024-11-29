def clear():
    # \033[3J supprime tout le text entre le curseur et la fin
    print("\033[H\033[J", end="")

# Renvoie un str si tous les params sont à False
# Vérifie le type et renvoie un float si number_expected est à True
# Vérifie le type et renvoie un int si int_expected est à True, en ignorant number_expected
def custom_input(msg: str = "", number_expected: bool = False, int_expected: bool = False):
    if msg != "":
        msg += "\n"

    result = None
    while result == None:
        s = input(msg + ">> ")

        if int_expected == True:
            try:
                result = int(s)
            except:
                pass
        
        elif number_expected == True:
            try:
                result = float(s)
            except:
                pass

        else:
            result = s
    
    return result

"""

"""
def show_dialog(texts: list):
    for text in texts:
        clear()

        print(text)
        print("\nAppuyer sur entré pour continuer.")
        custom_input()