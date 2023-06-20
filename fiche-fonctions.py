# DEFINIR UNE FONCTION
def hello():
    print('Hello!')

# APPEL(1) OU EXECUTION(2)
    # /!\ il faut éviter de déclarer & d'appeler ou exécuter 1 fonction dans le même fichier
hello()


# FONCTIONS NATIVES = définies (print())    .vs.        FONCTIONS UTILISATEUR = celles que l'on crée


# DONNER DES PARAMÈTRES

#1
def helloyou(name):
    print(f"Hello {name} !")

helloyou("Jean-Mi") # = variable helloyou(name) précisée

#2
def addition(a, b):
    return a + b

resultat = addition(42, 123)
print(f"Le résultat est {resultat}")

# IMPORTER FONCTION D'UN AUTRE MODULE (FICHIER)
import library 

resultat = library.oui_non(False)
print(resultat)
print(library.oui_non(True))

# REVERSE LOOKUP

my_list = [42, 123, 3.14]

def reverse_lookup(my_list, value):
    """ Cette fonction prend en paramètres un liste & une valeur à rechercher. 
    Elle renvoie l'index de la valeur si cette dernière est trouvée. 
    Si la valeur n'est pas trouvée, la fonction renvoie None.

    my_list (list) = liste dans laquelle il faut chercher
    value (any) = la valeur à rechercher
    return (int si la valeur est trouvée ou None si valeur non trouvée 
    """
    for i in range(len(my_list)):
        print(i)
        if my_list[i] == value:
            # @dev
            # print(f'{i = }')
            return i

    return None         # une fois que la boucle est terminée & que la fonction n'a rien trouvé, 
                        # on s'assure que la fonction renvoie None
                        
# value=3.14 :soit ça,  soit ça
result = reverse_lookup(my_list, 3.14)
print(result)