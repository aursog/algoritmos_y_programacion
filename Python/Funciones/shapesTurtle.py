import turtle
import shapes

def menu():
    print("""\n Seleccion una figura:
    \t 1.- Circulo
    \t 2.- Cuadrado
    \t 3.- Triangulo
    \t 4.- Rectangulo
    \t 5.- Pentagono
    \t 6.- Sextagono
    \t 7.- Heptagono
    \t 8.- Salir \n\n""")

def opciones(opc):
    if opc == 1:
        t.circle(100)
    elif opc == 2:
        shapes.cuadrado(t)
    elif opc == 3:
        shapes.triangulo(t)
    elif opc == 4:
        shapes.rectangulo(t)
    elif opc == 5:
        shapes.pentagono(t)
    elif opc == 6:
        shapes.hexagono(t)
    elif opc == 7:
        shapes.heptagono(t)
        
t = turtle.Turtle()

while True:
    menu()
    opc = int(input("Opcion: "))

    if opc == 8:
        break
    else:
        opciones(opc)

    input("")
    t.clear()

input("Presione enter para continuar")