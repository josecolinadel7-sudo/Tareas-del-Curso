print("Calculadora Basica")
num1 = float(input ("Ingrese el primer numero: "))
num2 = float(input ("Ingrese el segundo numero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else"No se puede dividir por 0"
print(f"La suma de {num1} + {num2} es: {suma}")
print(f"La resta de {num1} - {num2} es: {resta}")
print(f"La multiplicación de {num1} * {num2} es: {multiplicacion}")
print(f"La división de {num1} / {num2} es: {division}")