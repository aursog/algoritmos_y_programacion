import turtle

lab = turtle.Turtle()
lab.color('blue')
lab.penup()
lab.pendown()
lab.speed(1000)

for i in range(361):
    lab.forward(100)
    lab.right(90)
    
    if i != 0 and i % 4 == 0:
        lab.left(5)

input("wait")