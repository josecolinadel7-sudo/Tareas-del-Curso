
//Primera actividad con JS: Informacion

let nombre = "Jose"; // es mutable
let curso = "Curso de Programacion"

var nombre_1 = 22 // es mutable


const nombre_2 = true // No es mutable

console.log("Mi nombre es",nombre,"Tengo",nombre_1,"de edad y estoy viendo",curso);






//Segunda actividad con JS: Calculadora con If & Else 

console.log(`--- Bienvenidos a la calcula de prueba --- `);
let dato =prompt (`Por favor ingrese un valor: `);
let dato2 =prompt (`Por favor ingrese un valor: `);
console.log(`1) Suma`);
console.log(`2) Resta`);
console.log(`3) Multiplicar`);
console.log(`4) Divisiòn`);
console.log(`5) Modulo`);
let dato3 =prompt (`Indica el numero de operacion a realizar`);

if (dato3 == 1){
    let suma = dato + dato2;
    console.log(`La suma de ${dato} + ${dato2} es:` ,suma);
} else if (dato3 == 2){
    let resta = dato - dato2;
    console.log(`La resta de ${dato} - ${dato2} es:` ,resta);
} else if (dato3 ==3){
    let multiplicacion = dato * dato2;
   console.log(`La multiplicacion de ${dato} * ${dato2} es:` ,multiplicacion);
} else if (dato3 == 3){
    let division = dato / dato2;
    console.log(`La divicion de ${dato} / ${dato2} es:` ,division);
} else if (dato3 == 4){
    let modulo = dato % dato2;
    console.log(`El modulo de ${dato} % ${dato2} es:` ,modulo);
} else if (dato3 == 5){
    let exponenciacion = dato ** dato2;
    console.log(`La exponenciacion de ${dato} ** ${dato2} es:` ,exponenciacion);
} else {
    console.log(`Por favor utilice valores enteros`)
}
console.log(`--- Gracias por utilizar la calculadora de prueba --- `)








//Segunda actividad con JS: Calculadora con Switch & Case

console.log(`--- Bienvenidos a la calcula de prueba --- `);
let dato =prompt (`Por favor ingrese un valor: `);
let dato2 =prompt (`Por favor ingrese un valor: `);
console.log(`1) Suma`);
console.log(`2) Resta`);
console.log(`3) Multiplicar`);
console.log(`4) Divisiòn`);
console.log(`5) Modulo`);
let dato3 =prompt (`Indica el numero de operacion a realizar`);

switch (dato3){
    case"1":
    let suma = dato + dato2;
    console.log(`La suma de ${dato} + ${dato2} es:` ,suma);
    break
    case "2":
    let resta = dato - dato2;
    console.log(`La resta de ${dato} - ${dato2} es:` ,resta);
    break
    case "3":
    let multiplicacion = dato * dato2;
   console.log(`La multiplicacion de ${dato} * ${dato2} es:` ,multiplicacion);
   break
   case "4":
    let modulo = dato % dato2;
    console.log(`El modulo de ${dato} % ${dato2} es:` ,modulo);
    break
    case "5":
    let exponenciacion = dato ** dato2;
    console.log(`La exponenciacion de ${dato} ** ${dato2} es:` ,exponenciacion);
    break
    default:
    console.log(`Por favor utilice valores enteros`)
    break
}
    console.log(`--- Gracias por utilizar la calculadora de prueba --- `)







//Segunda actividad con JS: Tv de 10 pulgadas con ¡¡¡ ENVIO GRATIIIIIIIS !!!


const producto1 = "Tv de 10 pulgadas"
let precio = 450.99
let stock =  25
const enviogratis = "Envio GRATIS !!!"

console.log (`Nombre del producto: ${producto1} \nTiene un precio de: ${precio}\n Disponibles en Stock: ${stock}\n Este producto cuenta con ${enviogratis}`)










//Segunda actividad con JS: Compra de TV de 10 pulgadas por cantidad

const producto1 = "Tv de 10 pulgadas";
let precio = 450.99;
let stock =  25;    

const enviogratis = "Envio GRATIS !!!";

console.log (`Nombre del producto: ${producto1} \nTiene un precio de: ${precio}\n Disponibles en Stock: ${stock}\n Este producto cuenta con ${enviogratis}`)
let dato5 = Number(prompt (`Indica la cantidad `));
Total = precio * dato5;
Impuestos = Total *0.07;
Pagar = Total + Impuestos
console.log (`\n Total precio de producto: ${Total}\nImpuestos a pagar: ${Impuestos}\nTotal a PAGAR: ${Pagar}`);

