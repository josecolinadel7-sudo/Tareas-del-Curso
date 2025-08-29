#1) Transformación de Matriz: 

def multiplicar_matriz(matriz, escalar):
    return [[elemento * escalar for elemento in fila] for fila in matriz]

mi_matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
resultado = multiplicar_matriz(mi_matriz, 3)

print("Matriz original:")
for fila in mi_matriz:
    print(fila)

print("\nMatriz multiplicada por 3:")
for fila in resultado:
    print(fila)


#2) Ordenamiento con Lambda:

puntuaciones = [("Ana", 10), ("Luis", 15), ("Juan", 10), ("David", 12), ("Javier", 18)]

puntuaciones_ordenadas = sorted(puntuaciones, key=lambda x: x[1], reverse=True)

print("Tuplas ordenadas por puntuación (descendente):")
for nombre, puntuacion in puntuaciones_ordenadas:
    print(f"{nombre}: {puntuacion}")


#3)Producto Recursivo:

def producto_recursivo(lista):
    if not lista:
        return 1
    return lista[0] * producto_recursivo(lista[1:])

numeros = [2, 3, 4, 5]
print("Producto recursivo:", producto_recursivo(numeros))


#4) Aplanadora de Arrays:

def aplanar_arrays(*args):
    return [elemento for lista in args for elemento in lista]

lista1 = [1, 2, 3]
lista2 = [4, 5]
lista3 = [6, 7, 8]

resultado_aplanado = aplanar_arrays(lista1, lista2, lista3)
print("Array aplanado:", resultado_aplanado)

#5) Filtrado por Longitud:

def filtrar_por_longitud(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]

palabras = ["gato", "elefante", "sol", "mariposa", "pez"]
resultado_filtrado = filtrar_por_longitud(palabras, 4)
print("Palabras con longitud mayor a 4:", resultado_filtrado)


