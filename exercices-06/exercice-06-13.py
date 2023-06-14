# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à 
# la place de la valeur originelle puis affichez le résultat
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
value=0    
# Line10 : creates a variable named value and sets it to 0. We use this variable 
# to keep track of the current position in the list.
for value in range(len(my_list)):       
# Line13 : This line starts a loop that goes through each position in [my_list]. 
# It means we will repeat the following instructions for each item in the list.
    my_list[value] *= 100
# Line16 : The item at the current position (my_list[value]) and multiply it by 100. 
# Then, we update the item in the list with this new multiplied value.
print("multiplied values list:", my_list)
# Line20 : After the loop finishes, we print the updated my_list array.
# It shows the values that have been multiplied by 100.
