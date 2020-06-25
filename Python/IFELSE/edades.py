# programa de edades

edad_p1 = int(input("Ingrese la edad de la persona 1: "))
edad_p2 = int(input("Ingrese la edad de la persona 2: "))

if edad_p1 < edad_p2:
    print("La persona 1 es menor que la persona 2")

if edad_p2 < edad_p1:
    print("La persona 2 es menor")
    
if edad_p2 == edad_p1:
    print("las personas tienen la misma edad")