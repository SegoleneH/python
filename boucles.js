// 1- BOUCLE FOR CLASSIQUE

for(let i = 0; i < 10; i++) {   // à partir de 0, si i < 10, y ajouter 1
    console.log("i=" + i)  
    // console.log : i=0, i=1, i=2, i=3, i=4, i=5, i=6, i=7, i=8, i=9
}
// let i = 0 : declaration de valeur dans une variable (peut être un boolean)
// i < 10 : condition de continuation : si i < 10, on continue la boucle
// i++ : incrément
//  console.log("i=" + i) : corps de la boucle

// Sens de lecture : for(1; 2; 4)
//                       3


//  BOUCLE A REBOURS
for(let i = 10; i > 0; i--) {
    console.log("i=" + i)
    // console.log : i=10, i=9, i=8, i=7, i=6, i=5, i=4, i=3, i=2, i=1
}

// 2- BOUCLE FOR EACH
let users = ['foo', 'bar', 'baz']

for (let user of users){        // "Of" permet de récupérer l'élément
    console.log(user);
}


for (let user in users){        // "In" permet de récupérer l'index de l'élément
    console.log(user);
}

for (let i in users){           
    let user = users[i];        // permet de récupérer les 2
    console.log(`i= ${i}, user = ${user}`);     // ` != ' | `=Alt Gr + 7
}

// 3- METHODE FOR EACH ASYNCHRONE

users.forEach(
    function(user, i, list) {
        console.log(`i = ${i}, user = ${user}`);
    }
);

// mode synchrone:  je fais 1 truc, quand j'ai fini je passe à un autre truc
// mode asynchrone: je fais 1 truc, je vérifie s'il n'y a pas d'autre truc à faire, puis je passe à un autre truc
// AJAX = Asynchronous JavaScript request & XML

// Syntaxe alternative : fonctions fléchées = syntaxe à utiliser 
users.forEach(
    (user, i, list) => {
        console.log(`i = ${i}, user = ${user}`);
    }
);
