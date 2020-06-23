import math

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

discriminante = b ** 2 - 4 * a * c

if a == 0:
    print("La ecuacion no tiene solución")
else:
    if discriminante < 0:
        discriminante = -discriminante
        raiz = math.sqrt(discriminante)
        x_1 = complex(-b/(2*a), raiz/(2*a))
        x_2 = complex(-b/(2*a), -raiz/(2*a))
    else:
        raiz = math.sqrt(discriminante)
        x_1 = (-b + raiz) / (2*a)
        x_2 = (-b - raiz) / (2*a)
    
    print(f"El resultado de la ecuacion es x_1 = {x_1} y x_2 = {x_2}")