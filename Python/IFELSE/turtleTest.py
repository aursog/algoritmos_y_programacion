import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
izq = input("Quiere ir a la izquierda (s/n): ")

t.fd(100)
if izq == "s":
    t.left(90)
    pasos = int(input("Ingrese la cantidad de pasos a dar: "))

    if pasos > 500:
        pasos = int(input("Ingrese menos pasos: "))
    
    t.fd(pasos)
else:
    if izq == "n":
        t.right(45)
        t.fd(100)
    else:
        print("Dije s/n")

input()