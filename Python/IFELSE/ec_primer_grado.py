a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones")
    else:
        print("La ecuación no tiene solución")
else:
    x = -b / a
    print("La solucion es: ", x)