import math

def calculo_discriminante(a,b,c):
    discriminante = b**2 - 4*a*c

    if (discriminante < 0):
        discriminante = -discriminante

    x_1 = (-b + math.sqrt(discriminante)) / 2*a
    x_2 = (-b - math.sqrt(discriminante)) / 2*a

    return (x_1, x_2)

def mostrar_resultado(x1, x2):
    print("El resultado es x1 = {:.2f} y x2 = {:.2f}".format(x1, x2))

resultado = calculo_discriminante(3,4,5)
mostrar_resultado(resultado[0], resultado[1])