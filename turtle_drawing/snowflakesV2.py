from turtle import*

shape("turtle")
speed(10)
pencolor("white")
pensize(4)
Screen().bgcolor("turquoise")

# forward(num)   - this one moves the turtle forward by a certain num of steps
# right(num)     - turns the turtle to the right by a certain num of degrees
# left(num)      - turns the turtle to the right by a certain num of degrees
# backward(num)  - this one moves the turtle backward by a certain num of steps

# 1st arm
arm_length = 30
def v_shape():    
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def arm():
    for i in range(0,4):
        forward(arm_length)
        v_shape()
    backward(arm_length * 4)

# for entire snowflake
for i in range(0,6):
    arm()
    left(60)


done()
