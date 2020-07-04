while True:
    edificio = input("> ")

    if len(edificio) == 0:
        break

    for bloque in edificio:
        if bloque == "C":
            pass
        elif bloque == "V":
            pass
        elif bloque == "T":
            pass
        else:
            print("Error")