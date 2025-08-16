agenda = {
    "Jose": "01234",
    "David": "56789"
}

print("\nContactos disponibles:")
for nombre, telefono in agenda.items():
    print(f"{nombre} = {telefono}")

nombre_buscar = input("Ingrese el nombre del contacto: ")
if nombre_buscar in agenda:
    print(f"\nTeléfono de {nombre_buscar}: {agenda[nombre_buscar]}")
else:
    print("\nContacto no encontrado")
