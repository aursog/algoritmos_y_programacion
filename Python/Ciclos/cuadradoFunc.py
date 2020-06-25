import turtle
import shapes

t = turtle.Turtle()

t.speed(0)
for i in range(72):
    t.left(5)
    shapes.hexagono(t)

input("Presione enter para finalizar")