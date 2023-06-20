# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

import random
a = random.randint(0, 42)
b = random.randint(0, 42)

def compare(a:float, b:float) ->int:
    print(a, b)
    if a > b:
        print(1)
    elif a < b:
        print(-1)
    else:
        print(0)

compare(a, b)
