import turtle

t = turtle.Turtle()

lados = int(input("Ingrese cantidad de lados: "))
angulo = 360 // lados
veces = 0

#mientras condicion hacer
#tiempo total = 40 seg
while veces < 10:
    i = 0
    # 4 seg
    while i < lados:
        t.fd(100)
        t.right(angulo)
        i = i + 1
    
    veces = veces + 1

input()