pokemon_base = {'Salamèche' :  {'espèce' : 'Salamèche',
                                'pv' : 39,
                                'attaque' : 53,
                                'defense' : 43,
                                'vitesse' : 65,
                                'évolution' : (16,'Reptincel'),
                                'type' : ('feu',),
                                'valeur_experience' : 65,
                                'attaques' : [{ 'Nom' : 'Charge',
                                                'Degats' : 60,
                                                'Precision' : 100,
                                                'Type' : 'normal'},
                                              { 'Nom' : 'Flamèche',
                                                'Degats' : 60,
                                                'Precision' : 100,
                                                'Type' : 'feu'} 
                                             ]
                                },
                'Reptincel' :  {'espèce' : 'Reptincel',
                                'pv' : 58,
                                'attaque' : 64,
                                'defense' : 58  ,
                                'vitesse' : 80  ,
                                'évolution' : (36,'Dracofeu'),
                                'type' : ('feu',),
                                'valeur_experience' : 40,
                                'attaques' : [{ 'Nom' : 'Coupe',
                                                'Degats' : 70,
                                                'Precision' : 100,
                                                'Type' : 'normal'},
                                              { 'Nom' : 'Lance-flamme',
                                                'Degats' : 80,
                                                'Precision' : 100,
                                                'Type' : 'Feu'},]
                                },
                'Dracofeu' :  {'espèce' : 'Dracofeu',
                                'pv' : 78,
                                'attaque' : 84,
                                'defense' : 78,
                                'vitesse' : 100,
                                'évolution' : (),
                                'type' : ('feu','vol'),
                                'valeur_experience' : 40,
                                'attaques' : [{ 'Nom' : 'Frappe Atlas',
                                                'Degats' : 90,
                                                'Precision' : 100,
                                                'Type' : 'normal'},
                                              { 'Nom' : 'Déflagration',
                                                'Degats' : 100,
                                                'Precision' : 100,
                                                'Type' : 'feu'},
                                              { 'Nom' : 'Tornade',
                                                'Degats' : 70,
                                                'Precision' : 100,
                                                'Type' : 'vol'},]
                                },
                                }

def CreerPokemon(espece, niveau):
    pokemon = {}
    pokemon["espece"] = espece
    pokemon["nom"] = espece
    pokemon["niveau"] = niveau
    pokemon["exp"] = 0

    for cle in pokemon_base[espece]:

        if cle == "attaque" or cle == "vitesse" or cle == "defense" :
            pokemon[cle] = (((pokemon_base[espece][cle] * 2) * niveau) // 100) + niveau + 10

        if cle == "pv" :
            pokemon["pv_max"]= (((pokemon_base[espece][cle] * 2) * niveau) // 100) + 5
            pokemon["pv"] = pokemon["pv_max"]

        if cle == "type" or cle == "évolution" or cle == "attaques" :
            pokemon[cle] = pokemon_base[espece][cle]

    return pokemon

def evolution(pokemon):
    nouvelle_espece = pokemon["évolution"][1]
    pokemon["espece"] = nouvelle_espece
    nv = pokemon["niveau"]

    for cle2 in pokemon_base :
        if cle2 == "attaque" or cle2 == "vitesse" or cle2 == "defense" :
            pokemon[cle2] = (((pokemon_base[nouvelle_espece][cle2] * 2) * nv ) // 100) + nv + 10

    if cle2 == "pv" :
        pokemon["pv_max"] = (((pokemon_base[nouvelle_espece][cle2] * 2 ) * nv) // 100) + 5
        pokemon["pv"] = pokemon["pv_max"]

    if cle2 == "type" or cle2 == "évolution" or cle2 == "attaques" :
        pokemon[cle2] = pokemon_base[nouvelle_espece][cle2]

def gain_niveau(pokemon):
    pokemon["niveau"] = pokemon["niveau"]+1
    nv = pokemon["niveau"]
    p_base = pokemon_base[pokemon["espece"]]

    for cle in p_base:

        if cle == "attaque" or cle == "vitesse" or cle == "defense" :
            pokemon[cle] = (((p_base[cle] * 2) * nv) // 100) + nv + 10

        if cle == "pv" :
            pokemon  ["pv_max"]= (((p_base[cle] * 2) * nv) // 100) + 5
            pokemon["pv"] = pokemon["pv_max"]

    if pokemon["niveau"] >= p_base["évolution"][0]:
        evolution(pokemon)

def gain_exp(pokemon, pokemon_vaincu, sauvage):

    if sauvage == True:
        a = 1
    else:
        a = 1.5

    b = pokemon_base[pokemon["espece"]]["valeur_experience"]

    N = pokemon_vaincu["niveau"] 

    exp_gagne = (a * b * N) // 7

    pokemon["exp"] = exp_gagne + pokemon["exp"]

    if pokemon["exp"] >= 10* pokemon["niveau"]:
        pokemon["exp"] -= 10 * pokemon["niveau"]
        gain_niveau(pokemon)