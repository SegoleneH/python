import random

# DEFINITIONS

    #EXPRESSION  
    #--> élément qui peut être réduit à 1 seule valeur/ remplacé par 1 valeur

    # (100 + 2)*3 -> 102*3 -> 306 --> expression
    # 1+1 > (100+2)*3 -> 2>306 -> False --> expression
    #random.randint(0, 100) -> 100 --> expression

    # print(100) -> pas une expression


# PRECEDENCE DES OPERATEURS : https://docs.python.org/3/reference/expressions.html#operator-precedence

# OPERATEURS SIMPLES 
    # additions & soustractions
    result = 1 + 2
    result = 3 - 4


    #multiplications
    result = 5 * 6


    #division
    result = 5 / 6


    #division entière
    result = 5 // 6


# OPERATEURS COMPOSES

    # ajouter 5 à i et affecter le résultat à la variable i
    i += 5
    # c'est la même chose que
    i = i + 5

    # soustraire 2 à i et affecter le résultat à la variable i
    i += 2
    # c'est la même chose que
    i = i + 2

    # on peut aussi composer des multiplications ou des divisions
    c *= 2
    # c'est la même chose que
    c = c * 2

    c = 3
    c = c * 2
    c *= 2

    c /= 2
    # c'est la même chose que
    c = c / 2


# INCREMENTATION

    # incrémenter de 1 (=ajouter 1)
    c = 0

    c = c + 1
    c += 1
    # si je remets la même ligne, c=2 < incrémentation stockée dans la variable
    # (c = c + 1) = (c += 1) 

    c += 1 

    # décrémenter de 1
    c = c - 1

    # l'opérateur -- n'existe pas en python mais il est valide dans d'autres langages
    # c--
    # c'est la même chose que
    c -= 1

    # on peut aussi composer des multiplications ou des divisions
    c *= 2
    # c'est la même chose que
    c = c * 2

    c = 3
    c = c * 2
    c *= 2

    c /= 2
    # c'est la même chose que
    c = c / 2



# OPERATEUR D'INCLUSION

        # dans une string de caractères
text1 = "Lorem ipsum"

result = "e" in text1
print(result)       #true
print("Lorem" in text1) #true
print("lorem" in text1) #false = cherche le mot exact, ici pas de majuscule

        # dans une liste
list1 = ['Lorem', 'ipsum']  # simple ou double quote = pareil
print("e" in list1) # false
print("ipsum" in list1) # true


# OPERATEUR DE COMPARAISON (< , > , <= , >= , == (égalité), != (différence))
    # COMPARAISON AVEC DES NOMBRES ALEATOIRES   

e = random.randint(0, 100)  # génère chiffre random entre 0 & 100 inclus
f = random.randint(0, 100)
print(f'{e = }')
print(f'{f = }')    # syntaxe = print(f'{variable = }')

result = e == f
print(result)

result = e > f
print(result)