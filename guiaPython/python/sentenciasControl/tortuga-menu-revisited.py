from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

turtle = Turtle()

print("""Escoja una opción:
        \t 1.- Cuadrado
        \t 2.- Triángulo
        \t 3.- Círculo""")

opcion = int(input("Ingrese opcion: "))

if opcion == 1:
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
elif opcion == 2:
    turtle.fd(100)
    turtle.lt(120)
    turtle.fd(100)
    turtle.lt(120)
    turtle.fd(100)
    turtle.lt(120)
elif opcion == 3:
    turtle.circle(40)
else:
    print("Opción ingresada es incorrecta")

pantalla.exitonclick()