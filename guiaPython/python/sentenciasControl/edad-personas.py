edad_1 = int(input("Ingrese la edad de la persona 1: "))
edad_2 = int(input("Ingrese la edad de la persona 2: "))

if edad_1 > edad_2:
    print("La persona 1 es mayor")
else:
    if edad_1 < edad_2:
        print("La persona 2 es mayor")
    else:
        print("Las personas tienen la misma edad")