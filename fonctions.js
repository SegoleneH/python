// DONNER DES PARAMÈTRES À UNE FONCTION

function nameFunction(nameOfTargetedValue){
                    //     ^ paramètre
    if (nameOfTargetedValue >= 42){     // <== condition
        nameOfTargetedValue*=0.25;      // <== contenu 
    }
    console.log(nameOfTargetedValue);   // <== ALWAYS PUT AFTER END OF LOOP
}
nameFunction() // <== appeler la fonction


// On peut définir le contenu des paramètres après la fonction
function discount(purchase){
    if (purchase>=1500){
        purchase*=0.85;
    }
    console.log(purchase);
}

discount(1900);//discount
discount(1200);//no discount

// On peut aussi définir plusieurs paramètres séparés par une virgule : (param1, param2)