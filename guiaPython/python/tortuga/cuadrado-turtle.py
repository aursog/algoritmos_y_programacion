from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

tortuga = Turtle()

# dibujamos el cuadrado
tortuga.fd(100)
tortuga.rt(90)
tortuga.fd(100)
tortuga.rt(90)
tortuga.fd(100)
tortuga.rt(90)
tortuga.fd(100)
tortuga.rt(90)

pantalla.exitonclick()