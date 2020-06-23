a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

x = -b / a

if a != 0:
    print(f"El valor de x es {x}")
else:
    if b == 0:
        print("La ecuación tiene infinitas soluciones")
    else:
        print("La ecuación no tiene solución")