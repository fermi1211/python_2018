import math
import turtle

loadWindow = turtle.Screen()

turtle.speed(10)

turtle.pu()
turtle.forward(-200)
turtle.pd()

#blue block
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.forward(150);turtle.left(90);turtle.forward(100);turtle.left(90);turtle.forward(150);turtle.left(90);turtle.forward(100);turtle.end_fill()

#red block
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(100);turtle.left(90);turtle.forward(300);turtle.left(90);turtle.forward(200);turtle.left(90);turtle.forward(150);turtle.left(90);turtle.forward(100);turtle.right(90);turtle.forward(150);turtle.end_fill()

#move
turtle.pu()
turtle.forward(-75)
turtle.right(90)
turtle.forward(33)
turtle.right(90)
turtle.pd()

#white inside block
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(17.5);turtle.end_fill()

#move
turtle.pu()
turtle.right(90)
turtle.forward(3)
turtle.left(90)
turtle.pd()

#white outside block
turtle.circle(20.5)

turtle.right(90)
turtle.begin_fill()
turtle.forward(14.5);turtle.right(165);turtle.forward(15);turtle.right(105);turtle.forward(7.8);turtle.right(105);turtle.forward(15);turtle.end_fill()

#set in middle
for i in range(24):
    turtle.pu()
    turtle.left(15)
    turtle.right(180)
    turtle.forward(35)
    turtle.right(30)
    turtle.forward(20.5)
    turtle.pd()

    turtle.begin_fill()
    turtle.forward(14.5);turtle.right(165);turtle.forward(15);turtle.right(105);turtle.forward(7.8);turtle.right(105);turtle.forward(15);turtle.end_fill()

turtle.exitonclick()