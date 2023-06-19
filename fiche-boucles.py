# UTILISATION DES BOUCLES:
# for : n(=nombre d'itérations de la boucle) est connu
# for each : liste finie mais n est inconnu
# while : n est inconnu, ou liste non-finie, ou on veut traiter seulement certains éléments d'une liste 


# 1- BOUCLE WHILE = "tant que"
    # for, if = une fois que la boucle est effectuée, on sort de la boucle
    # avec while, la boucle s'effectue à l'infini tant que la condition requise est remplie
        # --> pour ça qu'on s'en sert très peu en dev web. Surtout utilisé pour les jeux vidéos 

import random

# while False:
#     print("ce message ne s'affiche pas")

# while True:
#     continue     --> permet de reprendre au début de la boucle suivante : ici le print ne s'affichera
#                       jamais = Code mort
#     print("ce message s'affiche en boucle")     # --> ctrl + C pour arrêter le programme
#     break        --> permet de sortir d'une boucle à tout moment



# Cas où la boucle while est utile:
    # tant qu'il reste des éléments à traiter dans une liste
    # je veux m'arrêter dès qu'un résultat qui me convient est trouvé


# Exemple avec tirage de dé
dice = random.randint(1,6)

# while dice != 6:
#     print(f"je n'ai pas tiré un 6 mais un {dice}")
#     print("je recommence un nouveau tirage")
#     dice = random.randint(1,6)
# else:    
#     print("j'ai tiré un 6")


# exo : avec 2 dés & arrêter la boucle seulement si les 2 dés = 6
dice1 = random.randint(1,6)

while (dice !=6 and dice1 !=6):
    print(f"j'ai tiré un {dice} et un {dice1}")
    print("je recommence un nouveau tir")
    dice1 = random.randint(1,6)

else:
    print("j'ai tiré deux 6")


# re-création de la boucle for classique avec une boucle while

i=0
while i < 10:               # condition de continuation
    print(f'{i = }')        
    i += 1                  # partie incrément
# ^^^^^^^^^^^^^^^^^ = not very pythonic

# 2- BOUCLE FOR CLASSIQUE EN PYTHON :
for i in range(0, 10):        # 0 inclus, 10 exclu
        print(f'{i = }')      # même boucle qu'au dessus, il n'y a que la notation qui change  
# for index in range(0, 10):
#        print(f'{index = }')  Fonctionne aussi


# 3- BOUCLE A REBOURS
for i in range(10, 0, -1):  # (10, 0 , -1): compter de 10 à 1, avec décrémentation de -1 à chaque itération
        print(f'{i = }') 

# 4- BOUCLE FOREACH
users = ['foo','bar','baz']

for user in users:
#   ^^^^: variable temporaire
      print(user)


for i, user in enumerate(users):        # Permet de retrouver l'index de chaque élément
      print(f"{i= }, {user}")           # print : i= 0, foo | i= 1, bar | i= 2, baz

# 5- BOUCLE FOR syntaxe spéciale
for i, user in range(0, len(users)):        # 0= départ len(users)= nombre d'éléments dans la liste
      print(f"{i= }, {user}")               # range(0, len(users)) = range(0, 3)

