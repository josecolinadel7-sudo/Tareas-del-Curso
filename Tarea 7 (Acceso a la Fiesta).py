edad = int(input("Ingrese su edad: "))
lista = input("Estas en la lista de invitados?: ")

if edad >= 18 and lista:
    print("Acceso permitido.")
else:
    print("Acceso denegado. Debes ser mayor de edad.")