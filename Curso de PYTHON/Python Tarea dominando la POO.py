print("Profe no ponga tanta tarea para la proxima por favor 😭😭")

# --- Ejercicio 1: Sistema de Figuras Geométricas 📐 ---
print("\nTarea 1: Sistema de Figuras Geométricas 📐\n")
from abc import ABC, abstractmethod
import datetime

def registrar_calculo(func):
	def wrapper(self, *args, **kwargs):
		resultado = func(self, *args, **kwargs)
		print(f"Se realizó el cálculo: {func.__name__} para {self.__class__.__name__}")
		return resultado
	return wrapper

class FiguraGeometrica(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimetro(self):
		pass

class Circulo(FiguraGeometrica):
	def __init__(self, radio):
		self._radio = radio

	@property
	def radio(self):
		return self._radio

	@radio.setter
	def radio(self, valor):
		if valor > 0:
			self._radio = valor
		else:
			raise ValueError("El radio debe ser positivo.")

	@registrar_calculo
	def area(self):
		from math import pi
		return pi * self._radio ** 2

	@registrar_calculo
	def perimetro(self):
		from math import pi
		return 2 * pi * self._radio

class Rectangulo(FiguraGeometrica):
	def __init__(self, base, altura):
		self._base = base
		self._altura = altura

	@property
	def base(self):
		return self._base

	@base.setter
	def base(self, valor):
		if valor > 0:
			self._base = valor
		else:
			raise ValueError("La base debe ser positiva.")

	@property
	def altura(self):
		return self._altura

	@altura.setter
	def altura(self, valor):
		if valor > 0:
			self._altura = valor
		else:
			raise ValueError("La altura debe ser positiva.")

	@registrar_calculo
	def area(self):
		return self._base * self._altura

	@registrar_calculo
	def perimetro(self):
		return 2 * (self._base + self._altura)

def mostrar_calculos(figura):
	print(f"Área: {figura.area()}")
	print(f"Perímetro: {figura.perimetro()}\n")

# --- Uso de la clase ---
circulo = Circulo(4)
rectangulo = Rectangulo(4, 6)

mostrar_calculos(circulo)
mostrar_calculos(rectangulo)

print("--" * 50)
# --- Ejercicio 2: Sistema de Personajes de Videojuego 🎮⚔ ---
print("\nTarea 2: Sistema de Personajes de Videojuego 🎮⚔\n")
from abc import ABC, abstractmethod

def requiere_mana(cantidad):
	def decorador(func):
		def wrapper(self, *args, **kwargs):
			if self._mana >= cantidad:
				resultado = func(self, *args, **kwargs)
				self._mana -= cantidad
				print(f"Mana restante: {self._mana}")
				return resultado
			else:
				print(f"No tienes suficiente mana para lanzar el hechizo. Mana actual: {self._mana}")
		return wrapper
	return decorador

class Personaje(ABC):
	def __init__(self, nombre, vida, mana):
		self.nombre = nombre
		self._vida = vida
		self._mana = mana

	@abstractmethod
	def atacar(self, objetivo):
		pass

# Guerrero
class Guerrero(Personaje):
	def atacar(self, objetivo):
		dano = 15
		print(f"{self.nombre} ataca a {objetivo.nombre} y causa {dano} de daño.")
		objetivo._vida -= dano
		print(f"Vida de {objetivo.nombre}: {objetivo._vida}")

# Mago
class Mago(Personaje):
	@requiere_mana(20)
	def atacar(self, objetivo):
		dano = 25
		print(f"{self.nombre} lanza un hechizo a {objetivo.nombre} y causa {dano} de daño.")
		objetivo._vida -= dano
		print(f"Vida de {objetivo.nombre}: {objetivo._vida}")

# --- Uso de la clase ---
guerrero = Guerrero("Daniel", 100, 10)
mago = Mago("Jose", 120, 80)

print("Estado Inicial:")
print(f"Guerrero = Daniel")
print(f"Mago = Jose (Me gustan los magos en los videojuegos xd)")

print("\n-- Guerrero Ataca:\n")
guerrero.atacar(mago)
print("\n-- Mago Ataca:\n")
mago.atacar(guerrero)
print("\n-- Guerrero Ataca:\n")
guerrero.atacar(mago)
print("\n-- Mago Ataca:\n")
mago.atacar(guerrero)

print("--" * 50)
# --- Ejercicio 3: Sistema de Gestión de Animales 🐾🐶🐱 ---
print("\nTarea 3: Sistema de Gestión de Animales 🐾🐶🐱\n")
class Animal:
	def __init__(self, nombre, edad):
		self.__nombre = nombre
		self.__edad = edad

	@property
	def nombre(self):
		return self.__nombre

	@property
	def edad(self):
		return self.__edad

	def hacer_sonido(self):
		raise NotImplementedError()

# Perro
class Perro(Animal):
	def __init__(self, nombre, edad, raza):
		super().__init__(nombre, edad)
		self.raza = raza

	def hacer_sonido(self):
		print(f"{self.nombre} (raza: {self.raza}) dice: ¡Guau guau!")

# Gato
class Gato(Animal):
	def __init__(self, nombre, edad, color):
		super().__init__(nombre, edad)
		self.color = color

	def hacer_sonido(self):
		print(f"{self.nombre} (color: {self.color}) dice: ¡Quiero Lazaña jajajajajaj!")

# --- Uso de la clase ---
perro = Perro("Betobe", 5, "Pastor Aleman")
gato = Gato("Garfield", 3, "Naranja Atigrado")

perro.hacer_sonido()
gato.hacer_sonido()

print("--" * 50)
# --- Ejercicio 4: Menú de Restaurante 🍕🍝 ---
print("\nTarea 4: Menú de Restaurante 🍕🍝\n")

class Ensalada:
	def __init__(self, nombre, precio):
		self._nombre = nombre
		self._precio = precio

	def mostrar_descripcion(self):
		print(f"Plato: {self._nombre} = Precio: ${self._precio}")

class Pizza(Ensalada):
	def __init__(self, nombre, precio, ingredientes, tamano):
		super().__init__(nombre, precio)
		self._ingredientes = ingredientes
		self._tamaño = tamano

	def mostrar_descripcion(self):
		print(f"Pizza: {self._nombre} ({self._tamaño})")
		print(f"  Ingredientes: {', '.join(self._ingredientes)} = Precio: ${self._precio}")

# --- Uso de la clase ---
plato1 = Ensalada("Ensalada Cesar", 5)
pizza1 = Pizza("Pepperoni", 25, ["queso", "chorizo", "salsa de tomate"], "Grande")

plato1.mostrar_descripcion()
pizza1.mostrar_descripcion()

print("--" * 50)
# --- Ejercicio 5: Productos de Tienda Online 🛒💻👕 ---
print("\nTarea 5: Productos de Tienda Online 🛒💻👕\n")

class Producto:
	def __init__(self, sku, nombre, precio):
		self.__sku = sku
		self.nombre = nombre
		self.precio = precio

	@property
	def sku(self):
		return self.__sku

	def mostrar_info(self):
		print(f"SKU: {self.__sku} - Producto: {self.nombre} - Precio: ${self.precio}")

class Electronico(Producto):
	def __init__(self, sku, nombre, precio, marca):
		super().__init__(sku, nombre, precio)
		self.marca = marca

	def mostrar_info(self):
		super().mostrar_info()
		print(f"Marca: {self.marca}")

class Ropa(Producto):
	def __init__(self, sku, nombre, precio, talla):
		super().__init__(sku, nombre, precio)
		self.talla = talla

	def mostrar_info(self):
		super().mostrar_info()
		print(f"  Talla: {self.talla}")
		
# --- Uso de la clase ---
prod1 = Electronico("A123", "Laptop DELL", 300, "DELL")
prod2 = Ropa("B456", "Franela Polo", 30, "L")

prod1.mostrar_info()
prod2.mostrar_info()
