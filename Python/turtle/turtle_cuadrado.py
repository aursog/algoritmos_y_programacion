from turtle import Turtle, Screen

s = Screen()
turtle = Turtle()
numero = int(input("Ingrese numero de cuadrados: "))

for i in range(numero):
    x = 20 * i
    turtle.up()
    turtle.goto(0, x)
    turtle.down()

    turtle.fd(20)
    turtle.left(90)
    turtle.fd(20)
    turtle.left(90)
    turtle.fd(20)
    turtle.left(90)
    turtle.fd(20)
    turtle.left(90)

s.exitonclick()