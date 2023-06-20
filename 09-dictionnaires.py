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

print(type(fruits))
print(fruits)


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

# un dictionnaire n'est pas triable
# provoque l'erreur "AttributeError: 'dict' object has no attribute 'sort'"
# fruits.sort()

fruits['d'] = 'datte'
print(fruits)

# ATTENTION: appeler la méthode "has_key()" sur un dictionnaire provoque l'erreur "AttributeError: 'dict' object has no attribute 'has_key'"
# [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html)
# - Removed. dict.has_key() – use the in operator instead.

if 'b' in fruits:
    del fruits['b']
print(fruits)

print('a' in fruits)
print('c' in fruits.keys())
print('citron' in fruits.values())

# les joker ne fonctionnent pas car la recherche est littérale
print('ci*' in fruits.values())

## exemple

users = [
    {
        'id': 1,
        'email': 'foo@example.com'
    },
    {
        'id': 2,
        'email': 'bar@example.com'
    },
    {
        'id': 3,
        'email': 'baz@example.com'
    }
]

for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")

## exo 4.4 avec des dictionnaires
players = [
    {
        'name': 'Alice',
        'points': 0,
        'bet': {
            'symbol': 'coeur',
            'value': 3

        },
        'set': {
            'value': False,
            'symbols': 0
        }
    },
    {
        'name': 'Bob',
        'points': 0,
        'bet': {
            'symbol': 'pique',
            'value': 7

        },
        'set': {
            'value': False,
            'symbols': 0
        }
    },
]

print(players[0]['name'])
print(players[0]['bet']['symbol'])
players[0]['points'] += 1
players[0]['set']['value'] = True
