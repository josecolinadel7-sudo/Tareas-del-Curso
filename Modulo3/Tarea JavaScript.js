// 1) Calculadora Básica

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



// 2) Filtro de Objetos Genérico

function filtrarPorPropiedad(arr, propiedad, valor) {
    return arr.filter(obj => obj[propiedad] === valor);
}
const personas = [
    { nombre: "Ana", edad: 25 },
    { nombre: "Luis", edad: 30 },
    { nombre: "Ana", edad: 40 }
];

const resultado = filtrarPorPropiedad(personas, "nombre", "Ana");
console.log("Filtrado por nombre 'Ana':", resultado);


// 3) Encontrar el Máximo

function encontrarMaximo(arr) {
    if (arr.length === 0) return undefined;
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

const numeros = [3, 7, 2, 9, 5];
console.log("El número más alto es:", encontrarMaximo(numeros));


// 4) Reduce al Máximo

const transacciones = [100, -20, 50,];
const balanceFinal = transacciones.reduce((acum, transaccion) => acum + transaccion, 0);

console.log("Balance final:", balanceFinal);



// 5) Concatenar Arrays

function concatenarArrays(arr1, arr2) {
    return [...arr1, ...arr2];
}

const a = [1, 2, 3];
const b = [4, 5, 6];
const resultadoConcatenado = concatenarArrays(a, b);
console.log("Arrays concatenados:", resultadoConcatenado);
