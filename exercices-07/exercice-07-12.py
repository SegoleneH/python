# exo 7.12
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est compris entre 2 et 9 inclus
# affichez la variable `count` après la boucle

import random

# réponse 7.12

count=0

for i in range(100):
    r = random.randint(1, 10)
    print(r)
    if r<=2 and r>=9:
        count += 1
print(f'Nombre de chiffres compris entre 2 & 9 : {count}')