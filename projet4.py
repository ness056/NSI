def transform_char(char: str, key: int) -> str:
    n = ord(char)
    shift = None
    if n >= 65 and n <= 90:
        shift = 65
        n -= 65
    elif n >= 97 and n <= 122:
        shift = 97
        n -= 97
    else:
        return char
    
    n = (n + key) % 26 + shift
    return chr(n)

if __name__ == "__main__":
    print("Bonjour, voulez vous chiffrer (1) ou déchiffrer (2) un message")

    mode = None
    mode_str = None
    while(mode == None):
        s = input("> ")
        if s == "1":
            mode = 1
            mode_str = "chiffrer"
        elif s == "2":
            mode = 2
            mode_str = "déchiffrer"
        else:
            print("Vous devez entrer soit 1 soit 2")

    print("Entrez le message à {}.".format(mode_str))
    message = input("> ")

    print("Entrez la clée de {}.".format(mode_str[:-1] + "ment")) # (dé)chiffrer -> (dé)chiffrement
    key = None
    while(key == None):
        s = input("> ")
        try:
            i = int(s)
            if i == float(s):
                key = i
        except:
            None

    if mode == 2:
        key *= -1

    new_message = ""
    for char in message:
        new_message += transform_char(char, key)

    if mode == 1:
        print("Voici votre message chiffrer: \"{}\"".format(new_message))
    else:
        print("Voici le message originel: \"{}\"".format(new_message))