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

# Dibujo linea de suspensos
angulo = 360 * suspensos / 100
tortuga.lt(angulo)
tortuga.fd(radio)
tortuga.bk(radio)

# Escribir texto para los suspensos
tortuga.up()
tortuga.rt(angulo/2)
tortuga.fd(radio/2)
tortuga.write('Suspensos')
tortuga.bk(radio/2)
tortuga.lt(angulo / 2)
tortuga.down()