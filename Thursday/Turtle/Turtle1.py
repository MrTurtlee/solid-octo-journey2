sides = input("How many sides do you want your shape to be?\n")
from turtle import *
color("blue")
shape("turtle")
speed(10)
pensize(4)

angle = 360 / sides 
for i in range(sides):
    forward(50)
    right(angle)

done()




