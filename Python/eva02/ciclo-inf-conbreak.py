def menu():
    print("""Escoja una opción:
    1.- Continuar
    2.- Detener
    """)

menu()
a = 0
while True:
    opcion = int(input("Opción: "))

    if opcion == 2:
        break

    print(a)
    a += 1
