
import turtle


screen = turtle.Screen()
screen.bgcolor("lightblue")


my_turtle = turtle.Turtle()
my_turtle.color("darkblue")
my_turtle.pensize(5)


for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)


turtle.done()
