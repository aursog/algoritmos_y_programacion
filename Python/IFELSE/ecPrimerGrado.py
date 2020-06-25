# ax + b = 0
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

if a == 0:
    if b == 0: 
        print("El sistema tiene infinitas soluciones")
    if b != 0:
        print("el sistema no tiene solucion")

if a != 0:
    x = -b / a
    print("El resultado de la ecuacion es:", x)
