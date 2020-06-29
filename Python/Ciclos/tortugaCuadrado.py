from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()

for _ in range(4):
    turtle.fd(20)
    turtle.right(90)

screen.exitonclick()
