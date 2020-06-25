import turtle

# Crea el espacio de dibujo donde comenzara a trabajar la tortuga
turtle.shape('turtle')

# Set del color de la tortuga
turtle.color('orange')
turtle.pensize(3)
turtle.speed(0)

# lectura desde el teclado
line = input('> ')

# ciclo que verifica si ya se termino de dibujar el mapa
while line:
    data = 0;
    
    # permite dibujar las lineas ingresadas segun descripcion de tarea
    for data in range(0,len(line),1):
        if (line[data] == 'X'):
            # dibuja los cuadraditos y posiciona a la tortuga para el proximo cuadrado
            for i in range(4):
                turtle.forward(20)
                turtle.left(90)

            turtle.up()
            turtle.setpos(turtle.pos() + (20,0))
            turtle.down()
        else:
            turtle.up()
            turtle.setpos(turtle.pos() + (20,0))
            turtle.down()

    # deja a la tortula lista para recibir instruccion en la siguiente linea
    turtle.up()
    turtle.setx(0)
    turtle.setpos(turtle.pos() + (0,-20))
    turtle.down()
    line = input('> ')

#Deja la tortuga lista para el recorrido del laberinto
turtle.up()
turtle.setpos(-20,20)
turtle.color('blue')
turtle.down()

pasos = input('Ruta: ')

input('Presione Enter para terminar ......');
