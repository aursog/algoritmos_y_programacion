while True:
    edificio = input(">")

    if len(edificio) == 0:
        break
    
    for bloque in edificio:
        if bloque == "C":
            pass
            # dibujar cuadrado
        elif bloque == "V":
            pass
            #dibujar vidrio
        elif bloque == "T":
            pass
            # dibujar techo
        else:
            pass
            #mostrar error