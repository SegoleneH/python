# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

longueur =0
valeur=""
index=0

for i in range(0, len(my_list)):            # pour tous les éléments de la liste de 0 au max
    if len(my_list) > longueur:             # si la longueur de la liste est sup à 0
        longueur = len(my_list[i])          # my_list[i] = élément  |  len(my_list[i]) = longueur de cet élément
        valeur= my_list[i]
        index= i
print(f"{index = }")
print(f"{valeur = }")
print(f"{longueur = }")
