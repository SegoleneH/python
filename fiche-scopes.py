# SCOPE = PORTÉE DES VARIABLES

# Si variable définie à l'extérieur d'une fonction : 
#       La fonction traite les variables soit avant, soit après
my_var = 123

def my_func1():
    print(my_var)
    print(my_var2)

my_var2 = 42


# Si variable définie à l'intérieur d'une fonction: 
#       On ne peut pas y accéder autrement que dans la fonction
#   ==> principe du verre teinté (comme une limousine)
# NameError: name 'my_var3' is not defined. Did you mean: 'my_var'?


def my_funct1():
    my_var3 = 3.14

# print(my_var3)


my_var4 = 'foo'

def my_func3(my_var4):
    # le paramètre my_var4 masque la variable définie à l'extérieur de la fonction ???
    print(my_var4)

# cet appel affiche 'bar'
my_func3('bar')


my_var4 = 'foo'

def my_func4():
    # la variable de my_var4 fait de l'ombre à la variable définie à l'extérieur de la fonction ???
    #      = function est lue en priorité ???
    my_var4 = 'baz'
    print(my_var4)

my_func4()
# la variable de my_var4 définie à l'extérieur de la fonction reste inchangée
print(my_var4)



def my_func5(my_var5):
    my_var5 = 'foo'
    print(my_var5)
my_var6 = 123


# Le passage de paramètre se fait par valeur.
# ==> cad que python copie la valeur dans une autre variable ( qui est le paramètre de la fonction)

# Types int, float, bool, str sont passés par valeur.
# cad que la fonction ne pourra accéder qu'à une copie de la variable originale définie à l'extérieur.
my_func5(my_var6)
print(my_var6)

def my_func6(my_var7: list):   #": list" est un type hinting.
    my_var7.append('foo')

my_var8 = [123, 42, 3.14]

# Types list, dict, tuple ou objet sont passés par référence.
# ==> cad que la fonction pourra accéder à la variable originale définie à l'extérieur.
my_func6(my_var8)
print(my_var8)