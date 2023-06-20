# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
import random
a = random.randint(0, 42)
b = random.randint(0, 42)

def is_greater(a:float, b:float) -> bool:
    print(a, b)
    if a > b:
        print(True)
    else:
        print(False)

is_greater(a, b)
