# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
# Note : faites une boucle et n'utilisez pas la méthode `index()`
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11
i=0
search=3.14  # pour récupérer valeur & pouvoir la réutiliser; 
             # search=int(input()) ==> reverse lookup recherche avec le terminal

for i, number in enumerate(my_list):            #pour chaque boucle effectuée & pour chaque item de my_list
    if number == search:                        # si l'item est égal à 3.14
        print(f'Index de 3.14 : {i}ème place')  # affiche le nombre de boucles effectuées jusqu'à l'item 3.14


# for number in my_list:       # affiche toute la liste
#     # @dev
#     print(number)


# if number == 3.14:
#     print("Le nombre est égal à 3.14")
# else:
#     print("Le nombre n'est pas égal à 3.14")
