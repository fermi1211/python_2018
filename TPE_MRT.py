import math
from turtle import *

loadWindow = Screen()
screensize(800,800)
pensize(10)

#move the position to the center
pu();forward(-50);pd()

#blue
pencolor("blue");forward(350);forward(-375);right(135);forward(135);left(45);forward(135)
pu();home();forward(-50);pd()

#red
pencolor("red");left(90);forward(270);left(45);forward(120);left(45);forward(80);right(90);forward(40);left(45);forward(60)
pu();home();forward(-50);pd()
right(90);forward(60);left(90);forward(210);
pu();home();forward(-50);left(90);forward(60);right(90);pd()

#green
pencolor("green");forward(255);forward(-280);right(90);forward(120);left(90);forward(25);right(45);forward(120);right(45);forward(150)
pu();home();forward(10);pd()

#orange
pencolor("orange");right(90);forward(60);right(45);forward(120);left(45);forward(45)
pu();home();forward(10);pd()
left(90);forward(120);left(90);forward(120);left(45);forward(270);forward(-270);right(90);forward(180)
pu();home();forward(70);pd()

#brown
pencolor('#CC6600');left(90);forward(180);right(90);forward(180);right(45);forward(75);right(45);forward(125)
pu();home();forward(70);pd()
right(90);forward(110);left(90);forward(65);right(90);forward(60);left(90);forward(105)
pu();home();forward(-50);left(90);forward(270);left(45);forward(120);right(90);pd()

#pink
pencolor("pink");forward(30)
pu();home();forward(-50);right(90);forward(60);left(45);forward(120);right(45);forward(90);right(90);pd()

#light green
pencolor('#CCFF99');forward(30)


exitonclick()
