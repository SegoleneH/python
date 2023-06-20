# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#       meters = miles * 1609.344
#
# 1- Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# 2- Ensuite convertissez les valeurs :
# - 1 Km en miles
# - 10 miles en mètres
#
# 3-Appelez les fonctions et affichez les résultats

# réponse 10.6

def meters_to_miles(meters):
    miles = (meters / 1609.344)
    return(miles)

def miles_to_meters(miles):
    meters = (miles * 1609.344)
    return(meters)

km=1
miles=meters_to_miles(km*1000)      # (km*1000) = (meters)

print(miles)

miles=10
meters=miles_to_meters(miles)
print(meters)