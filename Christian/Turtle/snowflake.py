from turtle import *

color("white")
shape("turtle")
speed(100)
pensize(4)
Screen().bgcolor("turquoise")

def vshape():
    right(25)
    forward(50)
    back(50)
    left(50)
    forward(50)
    back(50)
    right(25)

def flake():
    for i in range(1,5):
        forward(50)
        vshape()

def snowflake():
    for i in range(1,6):
        right(60)
        flake()

snowflake()

done()