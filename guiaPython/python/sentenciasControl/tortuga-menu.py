from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

turtle = Turtle()

print("Escoja una opción:")
print("\t 1.- Cuadrado")
print("\t 2.- Triángulo")
print("\t 3.- Círculo")

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
else:
    if opcion == 2:
        turtle.fd(100)
        turtle.lt(120)
        turtle.fd(100)
        turtle.lt(120)
        turtle.fd(100)
        turtle.lt(120)
    else:
        turtle.circle(40)

pantalla.exitonclick()