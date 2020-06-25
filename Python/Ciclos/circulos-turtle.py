import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(1000)

for i in range(6):
    for color in ["red", "green", "blue", "magenta", "cyan", "yellow"]:
        t.color(color)
        
        for i in range(4):
            t.fd(100)
            t.left(90)

        t.pensize(1)
        t.left(10)

input("")