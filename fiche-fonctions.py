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



# TYPE HINTING

def mult(a:int, b:int)->int:   
#       =  Signature de la fonction (nom fonction + ses paramètres + son type de retour)


# copie d'une fonction comme si c'était une variable
# mult_copy = mult
# mult_copy(2,5)


    # fonction de degré supérieur = fonction qui accepte une fonction en paramètre
    # ou qui renvoie une fonction
    def operateur_binaire(a,b,fonction):
        return fonction(a,b)

    # appel de la fonction de degré supérieur
    resultat = operateur_binaire(2, 5, mult)

    operations = []
    operations.append(mult)

    a = 2
    b = 5
    resultat = None

    for operation in operations:
        resultat = operation(a,b)

    # Remplacer fonction len par fonction personnalisée
        def my_len(value):
            return 42

        len_backup = len

        len = my_len    # ==> renvoie toujours 42
        # Problème : on a cassé la fonction len. Si on veut la garder, il faut la stocker dans une
        # variable temporaire (L97)