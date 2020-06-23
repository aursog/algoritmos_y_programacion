from turtle import Screen, Turtle

radio = 300

pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

tortuga.up()
tortuga.goto(0, -radio)
tortuga.down()
tortuga.circle(radio)
tortuga.up()
tortuga.home()
tortuga.down()

pantalla.exitonclick()