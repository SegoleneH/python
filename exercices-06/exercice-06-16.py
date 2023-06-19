# exo 6.16
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
for i in range(len(my_list)):                           #i=nombre d'itération de la boucle
    if i == 1:
        my_list[0], my_list[i] = my_list[i], my_list[0]
    if i == 2:
        my_list[2], my_list[3] = my_list[3], my_list[2]
    elif i == 3:
        my_list[4], my_list[5] = my_list[5], my_list[4]
print(my_list)