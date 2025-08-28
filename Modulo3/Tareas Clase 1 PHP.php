
// Ejercicio #1.

<?php
$pares = 0;
$impares = 0;

for ($impares = 1; $i <= 50; $i++) {
    ($pares % 2 == 0) ? $pares++ : $impares++;
}

echo "Pares: $pares, Impares: $impares";
?>

// Ejercicio #2.

<?php
echo "## 1. Tabla del 8 ##\n";

for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
echo "\n";
?>

// Ejercicio #3.

<?php
$secreto = "14";
$intentos = 0;
$numero = readline ("Escoje un numero del 1 al 100: ");

while (true) {  
    if ($numero == $secreto) {
        echo "¡Correcto! en $intentos intentos\n";
        break;
    }elseif ($numero != $secreto) {
        echo "Numero incorrecto\n";
        break;
    }
}
?>

//Ejercicio #4.

<?php
$suma = 0;

for ($i = 1; $i <= 100; $i += 2) {
    $suma += $i;
}

echo "Suma de impares (1-100): $suma";
?>

//Ejercicio #5.
<?php
    $edad = readline ("Indique su edad: ");
while(true){
    if ($edad >= 18 && $edad <= 65) {
        echo "Licencia permitido.";
        break;
    } else {
        echo "Licencia denegada. Debes ser mayor de edad.";
        break;
    };
}
?>

// Ejercicio de Calculadora
<?php
function mostrarSaludo() {
    echo "¡Hola! Bienvenido a la Calculadora numero ya perdi la cuenta.\n";
    $suma = 5 + 5;
    echo "La suma de 5 + 5 es: $suma\n";
    $resta = 5 - 5;
    echo "La resta de 5 - 5 es: $resta\n";
    $multiplicacion = 5 * 5;
    echo "La multiplicacion de 5 * 5 es: $multiplicacion\n";
    $division = 5 / 5;
    echo "La division de 5 / 5 es: $division\n";
}
mostrarSaludo();
?>

//Ejercicio 6.
<?php
for ($A = 0; $A < 5; $A++) {
    for ($B = 0; $B < 5; $B++) {
        echo "#";
    }
    echo "\n";
}

?>


//Ejercicio 7.
<?php
$numero = 7;

if ($numero > 0) {
    echo "El número " . $numero . " es positivo.";
} else if ($numero < 0) {
    echo "El número " . $numero . " es negativo.";
} else {
    echo "El número " . $numero . " es cero.";
}

?>

//Ejercicio 8.
<?php
for ($numero = 1; $numero <= 30; $numero++) {
    if ($numero % 3 == 0 && $numero % 5 == 0) {
        echo "MarTierra\n";
    }
    else if ($numero % 3 == 0) {
        echo "Mar\n";
    }
    else if ($numero % 5 == 0) {
        echo "Tierra\n";
    }
    else {
        echo $numero . "\n";
    }
}

?>

//Ejercicio 9.
<?php
$temperatura_celsius = 20;
if ($temperatura_celsius < 10) {
    echo "Fría";
} else if ($temperatura_celsius >= 10 && $temperatura_celsius <= 25) {
    echo "Templada";
} else {
    echo "Calurosa";
}

?>

//Ejercicio 10.
<?php
for ($A = 10; $A >= 1; $A--) {
    echo $A."\n";
}
echo "¡Feliz Año Nuevo!\n";

?>


// Ejercicio de Calculadora #2
<?php
function mostrarSaludo() {
    echo "¡Hola! Bienvenido a la Calculadora numero ya perdi la cuenta.\n";
    $valor1 = readline ("Indique primer valor: ");
    $valor2 = readline ("Indique segundo valor: ");
    echo "--- MENU DE OPERACIONES ---\n";
    echo "1. Suma (+)\n";
    echo "2. Resta (-)\n";
    echo "3. Multiplicacion (*)\n";
    echo "4. Division (/)\n";

$respuesta = readline ("Indique el numero de Operacion a realizar: ");

while (true) {

    if ($respuesta == 1) {
        $suma = $valor1 + $valor2;
        echo "La suma es: $suma\n";
        break;
    } elseif ($respuesta == 2) {
        $resta = $valor1 - $valor2;
        echo "La resta es: $resta\n";
        break;
    } elseif ($respuesta == 3) {
        $multiplicacion = $valor1 * $valor2;
        echo "La multiplicacion es: $multiplicacion\n";
        break;
    } elseif ($respuesta == 4) {
        $division = $valor1 / $valor2;
        echo "La division es: $division\n";
        break;
    } else {
        echo "Opcion no valida, intente de nuevo.\n";
        $respuesta = readline ("Indique el numero de Operacion a realizar: ");
    }
}

}
mostrarSaludo();
?>