from turtle import*


# forward(num)   - this one moves the turtle forward by a certain num of steps
# right(num)     - turns the turtle to the right by a certain num of degrees
# left(num)      - turns the turtle to the right by a certain num of degrees
# backward(num)  - this one moves the turtle backward by a certain num of steps


def v_shape(v_length, num_v):    
    right(25)
    forward(v_length)
    backward(v_length)
    left(50)
    forward(v_length)
    backward(v_length)
    right(25)

def arm(arm_length, v_length, num_v):
    for i in range(0, num_v):
        forward(arm_length)
        v_shape(v_length, num_v)
    backward(arm_length * num_v)

# for entire snowflake
def snowflake(num_arms, arm_length, v_length, num_v):
    for i in range(0,num_arms):
        arm(arm_length, v_length, num_v)
        left(360 / num_arms)


def main():
    shape("turtle")
    speed(500)
    pencolor("white")
    pensize(4)
    Screen().bgcolor("turquoise")
    arm_length = 30
    v_length = 50
    num_arms = 10
    num_v = 4

    snowflake(num_arms, arm_length, v_length, num_v)

main()

done()
