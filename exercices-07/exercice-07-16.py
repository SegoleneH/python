# exo 7.16
# en utilisant une boucle for, affichez la puissance 2 des nombres de 0 à 99 inclus

# réponse 7.16

import random

for i in range(100):
    r = random.randint(0, 100)
    print(f'Nombre: {r}  \n  Puissance 2 : {r**2}')