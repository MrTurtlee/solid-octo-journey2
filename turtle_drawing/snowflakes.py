from turtle import *
import random

color("white")
shape("turtle")
speed(100)
pensize(4)

# change the background colour of the window
Screen().bgcolor("turquoise")

# the v shape
def vshape():
    right(25)
    forward(50)
    back(50)
    left(50)
    forward(50)
    back(50)
    right(25)


def spike(v, length):
    # makea spike
    for i in range(0,v):
        forward(length)
        vshape()

    # to go back to the centre
    backward(length * v)
    
# our main loop
def main_snowflake():
    num_v = 5
    num_arms = 15
    length = 25

    for v in range(0,num_arms):
        left(360/num_arms) 
        spike(num_v, length)
    
main_snowflake()
done()