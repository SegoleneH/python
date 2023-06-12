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
    print(not True)
    print(not False)

    # "OU" logique
    print(True or True)
        #True s'il y a un True parmi les 2 valeurs

    # "ET" logique
        # False dès qu'il y a un false parmi les 2 valeurs
