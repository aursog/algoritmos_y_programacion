from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(450, 450)
pantalla.screensize(425, 425)

t = Turtle()

# Primer cuadrado
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)

# levantamos el pincel y movemos la tortuga al interior
t.up()
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(90)
t.down()

# segundo cuadrado
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

pantalla.exitonclick()