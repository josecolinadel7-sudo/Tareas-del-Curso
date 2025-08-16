
lista_de_compras = []

lista_de_compras.append(input("Ingresa el primer producto: "))
lista_de_compras.append(input("Ingresa el segundo producto: "))
lista_de_compras.append(input("Ingresa el tercer producto: "))

print("Lista de compra:")
for articulo in lista_de_compras:
    print(f"{articulo}")

print(f"Total de produtos en la lista:{len(lista_de_compras)}")