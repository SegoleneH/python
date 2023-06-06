# Nombre entier (=integer number). number1 : variable, = : opérateur d'affectation, 123 : valeur 
number1 = 123
number1 = 42
print(number1)

# Float = nombre à virgule flottante
number2 = 3.14
number2 = 2.71
# 2.71 : calculs exponentiels
print(number2)

# String values = Chaîne de caractères. text1 = "texte pour humains" text2 = 'texte pour machine'
text1 = "foo bar"
print(text1)

text2 = 'foo bar bis'
print(text2)

# Boolean value (on/off, true/false, open/closed)
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

# Null value
accepted_terms = None
print(accepted_terms)

# Type de données
type(number1)
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(accepted_terms))

# Vérification du type de données
print(type(number1) is int)
print(type(number2)is str)

# Todo : interroger le type des autres variables

# Transtypage = type casting  int--> str
print(type(str(number1)))
print(str(number1))

# transtypage int --> bool
print(type(bool(number1)))
print(bool(number1))

number3 = 0
print(bool(number3))

# transtypage str --> int 

text3 = "123456789"
print(type(int(text3)))
# print(type(int(text1)))--> erreur -> Fonctionne avec "nombres" seulement


    # Fonctions de transtypage : 

# str()=convertit vers string
# int()=convertit vers integer
# bool()=convertir vers boolean
# float()= convertit vers float


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
