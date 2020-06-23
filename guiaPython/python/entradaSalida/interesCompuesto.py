cantidad = int(input("Ingrese cantidad: "))
tasa = float(input("Ingrese tasa de interés: "))
periodo = int(input("Ingrese periodo (años): "))

valor = cantidad * (1 + tasa/100)**periodo
print(f"El valor final en {periodo} años es de: {valor}")