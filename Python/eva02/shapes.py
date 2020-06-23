def cuadrado(t):
    for i in range(4):
        t.fd(100)
        t.right(90)

def triangulo(t):
    for i in range(3):
        t.fd(100)
        t.right(120)

def rectangulo(t):
    for i in range(4):
        if i % 2 == 0:
            t.fd(50)
        else:
            t.fd(100)
        t.right(90)

def pentagono(t):
    for i in range(5):
        t.fd(100)
        t.right(72)

def hexagono(t):
    for i in range(6):
        t.fd(100)
        t.right(60)

def heptagono(t):
    for i in range(7):
        t.fd(100)
        t.right(52)