// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

let my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'];

// réponse 6.15

// longueur =0;
// valeur="";
// index=0;
// 
// for i in range(0, len(my_list)):             // pour tous les éléments de la liste de 0 au max
//     if len(my_list) > longueur:             // si la longueur de la liste est sup à 0
//         longueur = len(my_list[i])         // my_list[i] = élément  |  len(my_list[i]) = longueur de cet élément
//         valeur= my_list[i]
//         index= i
// print(f"{index = }")
// print(f"{valeur = }")
// print(f"{longueur = }")

// my_list.length; ==> longueur de la liste
// console.log("foo".length); ==> longeur d'un mot

//my_list[0].length   ==> longueur du 1er mot

let index = null;
let valeur = "";
let longueur = 0;

for (let i=0; i < my_list.length; i++){
//   ^^^                        ^ si on ne met pas ça, i=0 à chaque boucle 
    // console.log(i);                 // affiche index
    // console.log(my_list[i]);        // affiche mot
    // console.log(my_list[i].length); // longueur mot
    // console.log();

    if (my_list[i].length > longueur) {
        longueur = my_list[i].length;   // mise à jour : stockage de la plus grande longueur rencontrée
        index = i;
        valeur = my_list[i];
    }
}
// console.log(index);
// console.log(valeur);
// console.log(longueur);
// console.log();


// BOUCLE FOR EACH QUI PERMET DE RÉCUPÉRER LES VALEURS (MAIS PAS L'INDEX)
let i = 0;

// reset des données (nécessaire car on a le même algo plus haut):
index = null;
valeur = "";
longueur = 0;

for (let word of my_list){

     // if peut aller ici
    console.log(i, word, word.length);

    if (my_list[i].length > longueur) {
        longueur = my_list[i].length;   // mise à jour : stockage de la plus grande longueur rencontrée
        index = i;
        valeur = my_list[i];
    }// if peut aller ici aussi, c'est même plus logique qu'il y ait les console.log avant
    
    i++;
// si on incrémente avant le console.log, l'index affiché sera de i+1, mais on veut i
// INCREMENT = DERNIERE CHOSE A FAIRE DANS LA BOUCLE
}
console.log(index);
console.log(valeur);
console.log(longueur);
console.log();          // equivalent des f strings ?