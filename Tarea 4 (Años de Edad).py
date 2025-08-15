# Tarea 4 Años de edad
año = float(input("Ingresa tu año de nacimiento: "))

hoy = 2025
edad = hoy - año

mayor = edad >= 18
if mayor:
    print(f"Tienes {edad} años Eres mayor de edad")
else:
    print(f"Tienes {edad} años Eres menor de edad")
