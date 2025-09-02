# Tarea Clase 2
from abc import ABC, abstractmethod

class Vehiculo(ABC):
	def __init__(self, marca, modelo, costo_base):
		self.marca = marca
		self.modelo = modelo
		self._costo_base = costo_base

	@abstractmethod
	def calcular_costo_mantenimiento(self):
		pass

	def mostrar_info(self):
		print(f"Vehículo: {self.marca} {self.modelo}")
		print(f"Costo de mantenimiento: ${self.calcular_costo_mantenimiento()}\n")

class Automovil(Vehiculo):
	def __init__(self, marca, modelo, costo_base, numero_puertas):
		super().__init__(marca, modelo, costo_base)
		self.numero_puertas = numero_puertas

	def calcular_costo_mantenimiento(self):
		return self._costo_base * self.numero_puertas

class Motocicleta(Vehiculo):
	def __init__(self, marca, modelo, costo_base, cilindrada_cc):
		super().__init__(marca, modelo, costo_base)
		self.cilindrada_cc = cilindrada_cc

	def calcular_costo_mantenimiento(self):
		return self._costo_base + (self.cilindrada_cc * 0.5)

# --- Uso de la clase ---

auto = Automovil("Chevrolet", "Optra", 400, 4)
moto = Motocicleta("Bera", "KAVAK", 100, 150)

auto.mostrar_info()
print("Siempre el Optra dañandose jajajajjajaj\n")
moto.mostrar_info()
print("La KAVAK es muy buena, no se rompe con nada jajajaja\n")




