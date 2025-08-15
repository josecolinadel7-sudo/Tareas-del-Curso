monto = float(input("Ingrese el monto de la compra: "))

if monto >= 100:
    descuento = 0.20
elif monto >= 50:
    descuento = 0.10
else:
    descuento = 0

precio_final = monto * (1 - descuento)
print(f"Precio original: {monto}€")
print(f"Descuento aplicado: {descuento*100}%")
print(f"Precio final: {precio_final}€")