# Leslie Bacajol
# Date: 10/29/21
# This program asks the users to input number of sides, the length of the side,
# the color of the line, and the fill color
# of a regular polygon then it draws it and shows the users the drawing

import turtle
# ask requirements for the drawing
sides = int(input("How many sides?"))
length = int(input("What will the length of the sides be?"))
lines = (input("What color will the sides be?"))
shape_c = (input("What color should fill the shape?"))

wn = turtle.Screen()  # creates a window
alex = turtle.Turtle()

# the drawing starts

alex.begin_fill()

for i in range(sides):
    alex.fillcolor(shape_c)
    alex.pencolor(lines)
    alex.pensize(7)
    alex.forward(length)
    alex.left(360/sides)
alex.end_fill()

wn.exitonclick()
