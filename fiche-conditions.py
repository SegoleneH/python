import random

if True:
#  ^^^^ = valeur/expression  
    print("Ce message s'affichera toujours")    # bloc conditionnel

if False:
    print("Ce message ne s'affichera jamais")
# ^ ne sera jamais exécuté car condition = False

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(f'{number1 = }')
print(f'{number2 = }')


if number1 < number2:
    print("number1 est plus petit que number2") 
#on a dit au dessus que si False,
# le code ne s'exécute pas: 
#si number1>number2 : rien ne s'affiche

else:
    print("La première condition n'est pas vérifiée")
# "catch all"--> recouvre tous les autres cas


# ELIF == ELSE IF

    if number1 < number2:
        print("number1 est plus petit que number2") 
    elif number1 > number2:
        print("La variable number1 est plus grande que number2")
    else:
        print("La variable number1 est égale à number2")


# OPERATEURS BOOLEENS  

    # négation 
    print(not True) # = False
    print(not False)# = True

    # "OU" logique
        #True s'il y a un True parmi les 2 valeurs

    # "OU" exclusif (Xor)
        #  A   |   B      | #  A xor B
    print(True ^ True)      # = False
    print(True ^ False)     # = True
    print(False ^ True)     # = True
    print(False ^ False)    # = False
        # True s'il y a 1x True (l'un ou l'autre mais pas les 2 en même temps)

    # "ET" logique
        # False dès qu'il y a un false parmi les 2 valeurs
