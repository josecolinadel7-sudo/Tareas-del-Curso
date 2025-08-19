
calificaciones = [5, 10, 15, 18, 20]
suma = 0

for nota in calificaciones:
    suma += nota
    promedio = suma / len(calificaciones)

nota_maxima = max(calificaciones)
nota_minima = min(calificaciones)

print("(-: *Tarea de Calificaciones :-)")
print(f"Calificaciones:{calificaciones}")
print(f"Promedio:{promedio:.2f}")
print(f"Nota más alta:{nota_maxima}")
print(f"Nota más baja:{nota_minima}")