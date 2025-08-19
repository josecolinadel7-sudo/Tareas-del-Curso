calificacion = float(input("Cual es tu calificaion final: "))

if calificacion >= 90 and calificacion <=100:
    print("Tienes A")
elif calificacion >= 80 and calificacion <= 89:
    print("Tienes B")
elif calificacion >= 70 and calificacion <= 79:
    print("Tienes C")
elif calificacion >= 60 and calificacion <= 69:
    print("Tienes D")
elif calificacion >= 0 and calificacion <= 59:
    print("Tienes F")
else:
    print("Coloca una calificaion de 0 a 100 por favor")