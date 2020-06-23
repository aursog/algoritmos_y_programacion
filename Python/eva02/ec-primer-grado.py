a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

if a != 0 and -b/a == abs(1):
    x = -b / a
    print(x)
else:
    if b == 0: 
        print("La ecuación tiene infinitas soluciones")
    else:
        print("La ecuación no tiene solución")