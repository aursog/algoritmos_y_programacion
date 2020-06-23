from math import sqrt

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

if a != 0:
    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        x_1 = (-b + sqrt(discriminante)) / 2 * a
        x_2 = (-b - sqrt(discriminante)) / 2 * a
        print(f"El resultado es: x_1={x_1}, x_2={x_2}")
    else:
        print("La ecuación no tiene soluciones reales")
elif b != 0:
    x = -c / b
    print(f"El valor de x es {x}")
elif c != 0:
    print("La ecuación no tiene solución")
else:
    print("La ecuación tiene infinitas soluciones")