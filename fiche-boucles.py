# WHILE = "tant que"
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


# 1er tirage
dice = random.randint(1,6)

while dice != 6:
    print(f"je n'ai pas tiré un 6 mais un {dice}")
    print("je recommence un nouveau tirage")
    dice = random.randint(1,6)
else:    
    print("j'ai tiré un 6")

# idée exo : avec 2 dés & arrêter la boucle seulement si les 2 dés = 6

dice1 = random.randint(1,6)


