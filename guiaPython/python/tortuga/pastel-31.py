# Dibujo de línea para los aprobados
angulo = 360 * aprobados / 100
tortuga.lt(angulo)
tortuga.fd(radio)
tortuga.bk(radio)

# Escribir texto para los aprobados
tortuga.up()
tortuga.rt(angulo/2)
tortuga.fd(radio/2)
tortuga.write('Aprobados')
tortuga.bk(radio/2)
tortuga.lt(angulo/2)
tortuga.down()

# Dibujo de línea para los notables
angulo = 360 * notables  / 100
tortuga.lt(angulo)
tortuga.fd(radio)
tortuga.bk(radio)

# Textos para los notables
tortuga.up()
tortuga.rt(angulo/2)
tortuga.fd(radio/2)
tortuga.write('Notables')
tortuga.bk(radio/2)
tortuga.lt(angulo/2)
tortuga.down()

# Dibujo a los sobresalientes
angulo = 360 * sobresalientes / 100
tortuga.lt(angulo)
tortuga.fd(radio)
tortuga.bk(radio)

# Escribir el texto para los sobresalientes
tortuga.up()
tortuga.rt(angulo/2)
tortuga.fd(radio/2)
tortuga.write('Sobresalientes')
tortuga.bk(radio/2)
tortuga.lt(angulo/2)
tortuga.down()

# Salir cuando damos click sobre la ventana
pantalla.exitonclick()