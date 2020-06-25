import turtle
from math import sin, pi

pantalla = turtle.Screen()
pantalla.setup(825,425)
pantalla.screensize(800,400)
pantalla.setworldcoordinates(-2*pi, -1, 2*pi, 1)

turtle = turtle.Turtle()

x = -2*pi
dx = 4*pi / 800
turtle.penup()
turtle.goto(x, sin(x))
turtle.pendown()

while x <= 2*pi:
    turtle.goto(x, sin(x))
    x += dx

pantalla.exitonclick()
