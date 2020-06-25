def es_primo(numero):
    isPrimo = False

    for elemento in range(2, numero):
        if numero % elemento == 0:
            break
    else:
        isPrimo = True

    return isPrimo