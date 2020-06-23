def es_primo(numero):
    isPrimo = False

    for elemento in range(2, numero):
        if numero % elemento == 0:
            break
    else:
        isPrimo = True

    return isPrimo


numero = int(input("Ingrese un rango para buscar primos: "))
for i in range(2, numero):
    if es_primo(i):
        print(f"El número {i} es primo")
