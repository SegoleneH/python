# DOC : https://docs.python.org/3/library/stdtypes.html#dict

# déclaration d'un dictionnaire vide
fruits = {}

# déclaration d'un dictionnaire avec du contenu
fruits = {
    'an': 'ananas',
    'ba': 'banane',
    'ci': 'citron'
  #  ^^clé  ^^valeur + do NOT forget the ','
}

# déclaration d'un dictionnaire vide
# pas la méthode recommandée
fruits = dict()

# déclaration d'un dictionnaire avec du contenu
# pas la méthode recommandée
fruits = dict(
    ci = 'citron',
    an = 'ananas',
    ba = 'banane',
)


# APPEND FOR DICTIONARY
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

my_dict['ipsum']='2.71'
print(my_dict)


# SUPPRIMER VALEUR

my_dict1 = my_dict.pop('foo')               # avec copie
my_dict.pop('foo')                          # sans copie

del my_dict['baz']                          # sans copie


# RECHERCHER VALEUR PAR LA CLE

print(my_dict['lorem'])

# exo 9.8
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

for key in my_dict:
    print(f"Key = {my_dict[key]}")      # renvoie valeurs des key au lieu de renvoyer index (tableau)


# BOUCLE FOR EACH pour obtenir les clés
for key in fruits:
    print(key)

for key in fruits.keys():
    print(key)

for fruit in fruits.values():
    print(fruit)


# BOUCLE FOR EACH pour obtenir les clés & les valeurs

for key, fruit in fruits.items():
    print(key, fruit)
