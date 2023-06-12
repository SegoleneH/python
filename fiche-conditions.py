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
