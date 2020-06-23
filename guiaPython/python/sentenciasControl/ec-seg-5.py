from math import sqrt

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

if a != 0:
    discriminante = b**2 - 4 * a * c
    det = 2 * a

    if discriminante > 0:
        x_1 = (-b + sqrt(discriminante)) / det
        x_2 = (-b - sqrt(discriminante)) / det
    else:
        discriminante = -discriminante
        raiz = sqrt(discriminante)
        x_1 = complex(-b/(det), raiz/(det))
        x_2 = complex(-b/(det), -raiz/(det))

    print(f"El resultado es: x_1={x_1}, x_2={x_2}")
elif b != 0:
    x = -c / b
    print(f"El valor de x es {x}")
elif c != 0:
    print("La ecuación no tiene solución")
else:
    print("La ecuación tiene infinitas soluciones")