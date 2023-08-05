# imports the turtle file, but have to use turtle.function_name
# mport turtle

# imports every function in the turtle file
from turtle import *

# defining the colour of the turtle that's going to draw
color("blue")

# define the shape of the drawer
shape("turtle")

# define the speed of the drawing
speed(10)

# define the thickness of the line that will be drawn
pensize(4)

# drawing a square:
# define how long the forward line is and draw it
forward(50)

# to turn to the left by a certain degree:
# left(90)

# to turn to the left by a certain degree:
# right(90)

# Class work: draw a square, by coding it manually or with a loop

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
# to stop the window from closing automatically:
done()