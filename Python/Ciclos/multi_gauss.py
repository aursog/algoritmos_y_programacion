def miMultiplicacion(multiplicando, multiplicador):
    secundario = 1
    segAcumulador = 0

    while secundario <= multiplicador:
        segAcumulador = segAcumulador + multiplicando
        secundario = secundario + 1

    return segAcumulador

indice = 1
acumulador = 1

while indice <= 10:
    acumulador = miMultiplicacion(acumulador, indice)
    indice = indice + 1

print(acumulador)