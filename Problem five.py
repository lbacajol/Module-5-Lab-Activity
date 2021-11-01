# Leslie Bacajol
# 10/29/21
# This program draws some kind of picture/shape
import turtle
wn = turtle.Screen()  # create a window

# set the background color
# of the turtle screen
turtle.Screen().bgcolor("pink")

# Draw a shape
alex = turtle.Turtle()

alex.begin_fill()
for i in range(7):  # repeat
    alex.pensize(2)
    alex.fillcolor()
    alex.right(100)
    alex.forward(45)
    alex.left(45)
    alex.backward(100)
    alex.right(70)
    alex.forward(45)
    alex.left(45)
    alex.backward(45)
    alex.right(100)
    alex.forward(45)
    alex.left(45)
    alex.backward(100)
    alex.right(70)
    alex.forward(45)
alex.end_fill()

wn.exitonclick()
