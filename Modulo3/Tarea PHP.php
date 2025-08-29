
//Tarea 1: Crear un array asociativo y convertirlo a JSON

<?php
$datos = [
    "nombre" => "Ana García",
    "edad" => 28,
    "ciudad" => "Madrid",
    "activo" => true
];

$json = json_encode($datos);

echo $json; 
?>

//Tarea 2: Contar palabras en un texto

<?php
function contadorPalabras($texto) {
    $texto = mb_strtolower($texto, 'UTF-8');
    $texto = preg_replace('/[^\p{L}\p{N}\s]/u', '', $texto);

    $palabras = preg_split('/\s+/', $texto, -1, PREG_SPLIT_NO_EMPTY);

    $frecuencia = array_count_values($palabras);
    
    arsort($frecuencia);
    
    return $frecuencia;
}

$texto = "¡Hola mundo! El mundo es grande, el mundo es diverso.";
$resultado = contadorPalabras($texto);

print_r($resultado);
?>

//Tarea 3: Determinar si un número es primo

<?php
function esPrimo($numero) {
    if ($numero < 2) {
        return false;
    }
    if ($numero == 2) {
        return true;
    }
    if ($numero % 2 == 0) {
        return false;
    }
    
    for ($i = 3; $i <= sqrt($numero); $i += 2) {
        if ($numero % $i == 0) {
            return false;
        }
    }
    
    return true;
}

$numeros = [0, 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17];

foreach ($numeros as $num) {
    echo "$num: " . (esPrimo($num) ? "Sí" : "No") . " es primo\n";
}
?>

//Tarea 4: Invertir un string

<?php
function invertirString($texto) {
    return strrev($texto);
}

// Ejemplos de uso
echo invertirString("Hola mundo") . "\n";
echo invertirString("PHP") . "\n";
echo invertirString("12345") . "\n";
?>

//Tarea 5: Generar una contraseña aleatoria

<?php
function generarPassword($longitud = 12, $especiales = true) {
    $letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $numeros = '0123456789';
    $caracteresEspeciales = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    
    $caracteres = $letras . $numeros;
    if ($especiales) {
        $caracteres .= $caracteresEspeciales;
    }

    $password = '';
    $max = strlen($caracteres) - 1;
    
    for ($i = 0; $i < $longitud; $i++) {
        $password .= $caracteres[random_int(0, $max)];
    }
    
    return $password;
}

echo "Password básica: " . generarPassword() . "\n";
echo "Password corta: " . generarPassword(8) . "\n";
echo "Password sin especiales: " . generarPassword(10, false) . "\n";
echo "Password larga con especiales: " . generarPassword(16, true) . "\n";
?>