Carrito_de_Compras =  []

def mostrar_lista():
    "Menu para la compra"
    print("Lista de Compra")
    print("1. Agrega un producto")
    print("2. Mostrar Carrito de Compra")
    print("3. Eliminar producto")
    print("4. Total de la compra")
    print("5. Finalizar\n")

def agregar_producto(cesta):
    producto = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input(f"Ingrese el precio de {producto}: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un numero valido para el precio.")
    cesta.append({"producto": producto, "precio": precio})
    print(f"{producto} Se agrego con el precio de {precio:}")

def mostrar_carrito(cesta):
    if not cesta:
        print(" Tu cesta esta vacia")
    print("CONTENIDO DE LA CESTA")
    for i, item in enumerate(cesta, 1):
        print(f"{i}. {item['producto']} ${item['precio']}")

def eliminar_producto(cesta):
     mostrar_carrito(cesta)
     if not cesta:
        return
    
     while True:
        try:
            seleccion = int(input("Ingrese el numero del producto a eliminar (0 para cancelar): "))
            if seleccion == 0:
                print("Operacion cancelada.")
                return
            if 1 <= seleccion <= len(cesta):
                producto_eliminado = cesta.pop(seleccion - 1)
                print(f"{producto_eliminado['producto']} Se elimino de la cesta.")
                break
            else:
                print(f"Por favor ingrese un numero entre 1 y {len(cesta)} o 0 para cancelar.")
        except ValueError:
            print("Por favor ingrese un numero valido.")

def calcular_total(cesta):
      if not cesta:
        print("No hay productos en la cesta para calcular el total.")
        return 
      total = sum(item['precio'] for item in cesta)
      print("TOTAL DE LA COMPRA")
      mostrar_carrito(cesta)
      print(f"TOTAL A PAGAR: ${total}")
 
def main():
   cesta = []
   print("Bienvenido, realicemos una compra")
    
   while True:
        mostrar_lista()
        opcion = input("Seleccione una opcion (1-5): ")
        if opcion == "1":
            agregar_producto(cesta)
        elif opcion == "2":
            mostrar_carrito(cesta)
        elif opcion == "3":
            eliminar_producto(cesta)
        elif opcion == "4":
            calcular_total(cesta)
        elif opcion == "5":
            print("Gracias por usar el simulador de cesta de compra")
            print("Hasta la proxima")
            break
        else:
            print("Opción no valida. Por favor ingrese un numero del 1 al 5.\n")
        
        input("Presione Enter para continuar.")

if __name__ == "__main__":
    main()