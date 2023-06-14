# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers
# de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
new_list = []
# réponse 6.14
for item in (my_list):          # for every item in my_list
    if type(item) == int:       # if item type is "int"
        new_list.append(item)   # add item to the end of new_list 
print(new_list)
