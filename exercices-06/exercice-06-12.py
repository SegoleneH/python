# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12
i=0
for i, item in enumerate(my_list):  # pour chaque itération, relève dans my_list
    if item <= 10:                  # tous les chiffres <= 10
        print(i, item)



