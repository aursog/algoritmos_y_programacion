from math import sqrt

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("La ecuación tiene infinitas soluciones")
        else:
            print("La ecuación no tiene solución")
    else:
        x = -c / b
        print("El resultado es: ", x)
else:
    discriminante = b**2 - 4 * a * c

    if discriminante < 0:
        print("La ecuación no tiene soluciones reales")
    else:
        x_1 = (-b + sqrt(discriminante)) / 2 * a
        x_2 = (-b - sqrt(discriminante)) / 2 * a
        print("El resultado es: ", x_1, x_2)