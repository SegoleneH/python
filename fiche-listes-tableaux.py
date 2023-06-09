                                        # LISTES
                                        
# DECLARATION D'UNE LISTE   (peut contenir expression, bool, int ,float ou [liste])
liste1 = [element, element1]

liste2 = list(element, element1)

liste3 = [
    element,
    element1
]

# AJOUTER ELEMENTS A LA FIN DE LA LISTE
    # ajouter 1 valeur 
liste1.append(123)

    # ajouter 1 variable
nombre1 = 42
liste1.append(nombre1)

# AJOUTER ELEMENTS N'IMPORTE OÙ DANS LISTE/TABLEAU
liste1.insert(1, "foo") # ajout en index 1 = 2ème position

# SUPPRESSION DU DERNIER ELEMENT
last_user = users.pop()         # variable qui contient expression supprimée 
print(last_user)
print(users)

# SUPPRESSION PAR INDEX
first_user = users.pop(0)        # variable qui contient expression supprimée    
print(first_user)

# SUPPRESSION PAR VALEUR
users.remove('bar')
print(users)

# CONCATENATION DE LISTES
liste8 = liste5 + liste6

# FUSION DE LISTES
liste5.extend(liste6)


# UTILISATION D'UN INDEX POUR AFFICHER 1 VALEUR PARTICULIERE
    # affichage de la première valeur
print(liste5[0])
# /!\ si on veut afficher Xème valeur, l'index = X-1


# UTILISATION D'UN INDEX POUR SUPPRIMER 1 VALEUR
del liste5[0]

# LISTE 2D
players = [ 
    [42000, 46400, 32103],
    [16700, 44667, 57987]
]
line = 0
col = 0
print(players[line][col])

for line in range(0, len(players)):         # compte le nombre de fois qu'il y a des éléments dans le tableau
    line = players[line]                    # récupérer les 2 lignes

    for col in range(0, len(line)):         # len(line) = longueur de la ligne = nombre de colonnes
        score = line[col]

        print(score)


# VARIABLE SCALAIRE : variable qui contient valeurs qui ne changent pas

                                        #TABLEAUX


# OBTENIR LA LONGUEUR D'UN TABLEAU (LE NOMBRE D'ELEMENTS) = len ()
taille_tableau5 = len(liste5)


# REMPLACER (REAFFECTER) 1 VALEUR DU TABLEAU AVEC UN INDEX
    # c'est comme si on écrasait la valeur avec une nouvelle valeur
liste5[0] = 123

# TRIER TABLEAU/LISTE
    # la fonction sorted() permet d'obtenir une copie d'un tableau triée par ordre alphabétique
    # le tableau original n'est pas modifié
numbers = ['g', 'd', 'a', 'c', 'b', 'Z']
ordered_list = sorted(numbers)      # ['Z', 'a', 'b', 'c', 'd','g'] = Maj apparaissent en 1er dans tableau ASCII

    # la méthode sort() permet de trier un tableau
    # ATTENTION : le tri s'effectue directement sur les données, l'ordre original est donc perdu !
liste6.sort()

# SUPPRIMER ELEMENT D'UN TABLEAU
    # la méthode pop() permet de supprimer la dernière valeur d'un tableau et d'affecter la valeur supprimée à une variable
    # ici, la valeur supprimée est récupérée dans la variable derniere_valeur
derniere_valeur = liste6.pop()

    # là par contre, la valeur supprimée n'est récupérée dans aucune variable (du coup elle est perdue)
liste6.pop()

# INSERER ELEMENTS AU MILIEU D'UN TABLEAU
liste5.insert(1, "foo")
