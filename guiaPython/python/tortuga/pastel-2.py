from turtle import Screen, Turtle

# Calificaciones
suspensos = 10
aprobados = 20
notables = 40
sobresalientes = 30

# Radio de circunferencia
radio = 300

# Inicialización 
pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

# Dibujo de circulo exterior
tortuga.up()
tortuga.goto(0, -radio)
tortuga.down()
tortuga.circle(radio)
tortuga.up()
tortuga.home()
tortuga.down()

# Salir cuando damos click sobre la ventana
pantalla.exitonclick()