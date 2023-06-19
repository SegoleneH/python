# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus

# réponse 7.14
import random

for i in range(100):
    r = random.randint(0, 101)
    if (r % 2) == 0:
        print(f'Nombres pairs : {r}')
