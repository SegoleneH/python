# exo 7.17
# en utilisant une boucle for, affichez la puissance 3 des nombres de 1 à 100 inclus

# réponse 7.17

import random

for i in range(100):
    r = random.randint(0, 101)
    print(f'Nombre: {r}  \n  Puissance 2 : {r**3}')