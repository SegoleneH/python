# Notation pour écrire une chaîne de caractères sur plusieurs lignes
text4 = """ <div>
                <h1></h1>
            <div>
        """

text5 = "<div>\n\t<h1>Titre de 1er niveau</h1>\n<div>\n"
print(text4)
print(text5)
# \n : retour à la ligne \t = tabulation
# alt + Z : retour à la ligne auto

# text6 = "Foo "Bar" Baz" --> erreur de syntaxe
text6 = 'Foo Bar Baz'
text6 = "Foo \"Bar\" Baz" # --> \= caractère d'échappement \\ = \ 

# documentation d'une fonction

def addition(a: float, b: float) -> float:
    """Renvoie la somme des nombres a et b

    a float le nombre a
    b float le nombre b
    return float
    """
#    ^ documentation
    return a + b


#INTERPOLATION 

# interpolation : intégrer directement des variables dans une chaîne de caractères

    #Interpolation avec f-strings

    mails=52

    text1=f"Vous avez reçu {mails} mails"
    #                       ^^^^^ INTERPOLATION


                                # CONCATENATION 


text1="lorem"
text2="ipsum"

text3=f"{text1} {text2}"        # toujours privilégier f strings pour la lisibilité
print(text3)


text3= text1 + text2        # resultat: loremipsum
print(text3)

text3= text1 + " " + text2        # resultat: lorem ipsum
print(text3)

# /!\ la concaténation ne fonctionne qu'avec des strings
# solution = convertir les autres types en str
mails=52


#text7= "Vous avez" + mails + "non lus"      # pas le même type de données = message d'erreur
text7= "Vous avez" + str(mails) + "non lus" # même type = OK


# répétition de texte

text8= "foo" * 3
print(text8)


# affichage de valeurs arrondies
number1= 10/3
text9 = f"10/3 est à peu près {number1:.2f}"    # on veut afficher arrondi à 2 chiffres
                                                # derrière virgule, sans perdre valeur 
print(text9)



                        # FONCTIONS ASSOCIÉES AUX STRINGS


text10= "foo bar baz foo"
print(len(text10))      # affiche la taille de la string (marche aussi pour listes)


print(text10.count('foo')) 
# affiche le nombre de fois où "foo" apparaît dans la string


# retrouver l'emplacement d'un mot/caractère
print(text10.find('foo'))       # resultat = 0

text10= "foo bar baz foo"
        #0  --> listes/strings commencent toujours à 0

position = text10.find('foo')
print(position)
print(text10.find('foo', position + 1))     # affiche 12: 2ème 'foo' commence 
                                            # au caractère 12


# remplacement de mots
print(text10.replace('foo', 'lorem'))
print(text10) # <-- affiche texte initial
text10=text10.replace('foo', 'lorem') # <-- changement appliqué sur la variable

# split & join
text10= "foo bar baz foo"
list1=text10.split(' ')   # = je veux split les éléments de la string
print(list1)              # résultat = ['foo', 'bar', 'baz', 'foo']

text11=" ".join(list1)    # = je veux réassembler les ["str","str"] en 1 "str"
print(text11)             # résultat = foo bar baz foo


# documenter une fonction
def ouiNon(value):
    """Cette fonction renvoie :
    -"oui" si le paramètre passé est True
    -"non" si le paramètre passé est False
    - "" dans les autres cas"""

    if value == True:
        return "oui"
    elif value == False:
        return "non"
    
        return ""     # on a enlevé le "else"
    
print(ouiNon.__doc__)

# Pour cette variable, dans d'autres langages on aurait mis des coms
    # -"oui" si le paramètre passé est True
    # -"non" si le paramètre passé est False
    # - "" dans les autres cas

# Mais en Python, on documente la variable comme ci-dessus
    

# Programmation orientée Objet

# foo = Button () <-- classe = majuscule
#^variable=minuscule

# foo.text()
#variable.fonction()
# fonction définie dans une classe = méthode
