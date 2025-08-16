Carrito_de_Compras =  []

def agregar_producto():
    nombre = input("\nIngresa el nombre del producto que quieres agregar a la cesta:")
    precio = float(input(f"Ahora ingesa el precio para el producto {nombre}: "))
    Carrito_de_Compras.append({"producto": nombre, "precio": precio})
    print(f"\nEl producto {nombre} ha sido agregado a la cesta correctamente.\n")

def mostar_cesta():
     if len(Carrito_de_Compras) == 0:
        print("\nLa cesta de productos esta vacia ! que esperas para llenarla!.\n")
     else:
        print("\nContenido de la cesta de compras:")
        for item in Carrito_de_Compras:
            print(f"- {item["producto"]} - bs.{item["precio"]}")
        print("")

def eliminar_producto():
    mostar_cesta()
    producto = input("\nCual producto deseas eliminar? ")
    for item in Carrito_de_Compras:
        if item["producto"].lower() == producto.lower():
            Carrito_de_Compras.remove(item)
            print(f"{producto} Se ha eliminado de la cesta.\n")
            return
    print("\nNO SE ENCONTRO ESE PRODUCTO EN LA CESTA.\n") 

def calcular_total():
    total = sum(item["precio"] for item in Carrito_de_Compras)
    print(f"\nEl total de la compra es: Bs.{total}\n")

def mostar_menu():
    print("--- Cesta de Productos ---")
    print("1. Agregar nuevo producto")
    print("2. Mostrar cesta de compras")
    print("3. Eliminar un producto")
    print("4. Calcular el total de la compra hasta ahora")
    print("5. Finalizar la compra de productos")

while True:
    mostar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        mostar_cesta()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        calcular_total()
    elif opcion == '5':
        print("\nFue un placer ayudarte, nos vemos la proxima...\n")
        break 
    else:
        print("\nError: Eliga una de las opciones (1/5) \n")
