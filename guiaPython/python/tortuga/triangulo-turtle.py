from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

t = Turtle()

# Dibujamos el triangulo
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)

pantalla.exitonclick()