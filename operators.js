//  comparaison égalité 
// renvoie true  
console.log("hello JS !"); 
let number1 = 123; 
let text1 = "123";  
// comparaison égalité 
// renvoie true 
console.log (number1 == text1); 
console.log (text1 == number1);  
// comparaison d 
// renvoie false 
console.log (number1 === text1); 
console.log (text1 === number1);

// opérateur incrémentation
console.log(number1)        // 123

// number1 += 1
number1++;
console.log(number1);       // 124

// incrémentation se fait après l'affichage
console.log(number1++);     // 124
console.log(number1);       // 125

// incrémentation se fait avant l'affichage
console.log(++number1);     // 126
