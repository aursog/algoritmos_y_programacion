def menu():
    print("""Seleccione una alternativa: 
    \t 1.- Suma
    \t 2.- Resta
    \t 3.- Multiplicación
    \t 4.- División
    \t 5.- Salir""")

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        print("La division por 0 no existe")
        return 0

    return num1 / num2

def operaciones(opcion):
    num1 = int(input("Ingrese el número 1: "))
    num2 = int(input("Ingrese el número 2: "))

    if opcion == 1:
        resultado = suma(num1, num2)
    elif opcion == 2:
        resultado = resta(num1, num2)
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
    elif opcion == 4:
        resultado = division(num1, num2)

    return resultado

while True:
    menu()
    opcion = int(input("opcion: "))

    if opcion == 5:
        break
    else:
        print(operaciones(opcion))
