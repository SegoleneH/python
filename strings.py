# Notation pour sauter des lignes dans la chaîne de caractères
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

# Exo : permuter les 2 variables en utilisant l'opérateur d'affectation &
#       le nom des variables
a = 123
b = 42

print(a)
print(b)

#technique 1
a1 = (b)
print(a1)
b1 = (a)
print(b1)
a = a1
b = b1

c = b
b = a
a = c

#technique 2
a, b = b, a
print(a, b)

#technique 3
a2 = 42
b2 = 123

a2 = a2 + b2
print(a2,b2)
b2 = a2 - b2
print(a2,b2)
a2 = a2 - b2
print(a2,b2)



