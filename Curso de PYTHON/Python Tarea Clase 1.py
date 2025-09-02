# Clase Alumno con tres métodos y atributos básicos
class Alumno:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.en_salon = True

    def salir_del_salon(self):
        if self.en_salon:
            self.en_salon = False
            print(f"{self.nombre} ha salido del salón.")
        else:
            print(f"{self.nombre} ya está fuera del salón.")

    def hacer_examen(self):
        if self.en_salon:
            print(f"{self.nombre} está haciendo el examen.")
        else:
            print(f"{self.nombre} no puede hacer el examen porque no está en el salón.")

    def saludar(self):
        print(f"Hola, soy {self.nombre} y mi matrícula es {self.matricula}.")

    # Tarea 1.2
    def __responder_preguntas_examen(self):
        print(f"{self.nombre} está respondiendo preguntas del examen.")

    def __entregar_tarea(self):
        print(f"{self.nombre} ha entregado la tarea.")

    def __recibir_calificaciones(self, calificacion):
        print(f"{self.nombre} ha recibido la calificación: {calificacion}.")

# --- Uso de la clase ---

alumno1 = Alumno("Jose", "A1")
alumno2 = Alumno("David", "A2")
alumno3 = Alumno("Eliezer", "A3")

alumno1.saludar()
alumno2.saludar()
alumno3.saludar()

alumno1.hacer_examen()

# Tarea 1.2
print("\n--- Métodos privados ---")
alumno1._Alumno__responder_preguntas_examen()
alumno2._Alumno__entregar_tarea()
alumno3._Alumno__recibir_calificaciones(9.5)
alumno2.hacer_examen()
alumno3.hacer_examen()

alumno1.salir_del_salon()
alumno1.salir_del_salon()

alumno1.hacer_examen()



# Tarea 2 ( Pizzeria )

# Ingredientes
class Ingrediente:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"

# Pizza
class Pizza:
    def __init__(self, nombre, tamano, precio_base):
        self.nombre = nombre
        self.tamano = tamano
        self.precio_base = precio_base
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def calcular_precio_total(self):
        total = self.precio_base + sum(ing.precio for ing in self.ingredientes)
        return total

    def __str__(self):
        ingredientes_str = ', '.join(str(ing) for ing in self.ingredientes)
        return f"Pizza: {self.nombre} ({self.tamano})\n  Ingredientes: {ingredientes_str}\n  Precio: ${self.calcular_precio_total():}"

# Pedido
class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.pizzas = []

    def agregar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calcular_total_pedido(self):
        return sum(pizza.calcular_precio_total() for pizza in self.pizzas)

    def mostrar_resumen_pedido(self):
        print(f"\n--- Resumen del Pedido #{self.numero_pedido} ---")
        for pizza in self.pizzas:
            print(pizza)
        print(f"Total a pagar: ${self.calcular_total_pedido():}\n")

# --- Uso de la clase ---

queso = Ingrediente("Queso", 15)
jamon = Ingrediente("Jamón", 18)
piña = Ingrediente("Piña", 10)

hawaiiana = Pizza("Hawaiana", "Grande", 80)
hawaiiana.agregar_ingrediente(queso)
hawaiiana.agregar_ingrediente(jamon)
hawaiiana.agregar_ingrediente(piña)

pedido1 = Pedido(1)
pedido1.agregar_pizza(hawaiiana)

pedido1.mostrar_resumen_pedido()






