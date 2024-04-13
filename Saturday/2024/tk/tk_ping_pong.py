import tkinter as tk
import time

window = tk.Tk()

# make a canvas and set its width, height and colour
canvas = tk.Canvas(window, width = 750, height = 500, bg = "white")
# initialise the canvas
canvas.pack()

# variable to make window stay open
windowOpen = True

pad = canvas.create_rectangle(0, 0, 70, 10, fill = "dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill = "blue")

# Pad variables
pad_speed = 6

# Ball variables
ball_x_speed = 4
ball_y_speed = -4
set_pad_top = 500 - 40
set_pad_bottom = 500 - 30

# Arrow key variables
left_pressed = 0
right_pressed = 0

# points variable
points = 0

# Variable f bounce count
bounce_count = 0

# if left and right_pressed variables are 1, the pad will move
def on_key_press(event):
    global left_pressed, right_pressed
    if event.keysym == "Left":
        left_pressed = 1
    elif event.keysym == "Right":
        right_pressed = 1

def on_key_release(event):
    global left_pressed, right_pressed
    if event.keysym == "Left":
        left_pressed = 0
    elif event.keysym == "Right":
        right_pressed = 0

def move_pad():
    pad_move = pad_speed * right_pressed - pad_speed * left_pressed
    (pad_left, pad_top, pad_right, pad_bottom) = canvas.coords(pad)
    if (pad_left < 750 or pad_move > 0):
        if (pad_right < 750 or pad_move < 0):
            canvas.move(pad, pad_move, 0)

def ball_move():
    global ball_x_speed, ball_y_speed, points, bounce_count, pad_speed
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
    
    if bounce_count == 4:
        if ball_x_speed > 0:
            ball_x_speed = ball_x_speed + 3
        elif ball_x_speed < 0:
            ball_x_speed = ball_x_speed - 3

        if ball_y_speed > 0:
            ball_y_speed = ball_y_speed + 3
        elif ball_y_speed < 0:
            ball_y_speed = ball_y_speed - 3
     
        # make pad go faster too
        pad_speed = pad_speed + 0.5
        bounce_count = 0

    # checks if we are going to the right and if we are touching the right side
    if ball_x_speed > 0 and ball_right > 750:
        ball_x_speed = -ball_x_speed
    # checks if we are going to the left and if we are touching the left side
    if ball_x_speed < 0 and ball_left < 0:
        ball_x_speed = -ball_x_speed
    
    # dealing with ball y speed
    if ball_y_speed < 0 and ball_top < 0:
        ball_y_speed = -ball_y_speed
    elif ball_y_speed > 0 and ball_bottom > set_pad_top and ball_bottom < set_pad_bottom:
        (pad_left, pad_top, pad_right, pad_bottom) = canvas.coords(pad)
        if (ball_x_speed > 0 and (ball_right + ball_x_speed > pad_left and ball_left < pad_right)
            or ball_x_speed < 0 and (ball_right > pad_left and pad_left + ball_x_speed < pad_right)
            ):
            ball_y_speed = -ball_y_speed
            points = points + 1
            bounce_count = bounce_count + 1

    # move our ball
    canvas.move(ball, ball_x_speed, ball_y_speed)

def close():
    global windowOpen 
    windowOpen = False
    window.destroy()

def reset():
    global left_pressed, right_pressed
    global ball_x_speed, ball_y_speed
    global points

    points = 0

    left_pressed = 0
    right_pressed = 0

    ball_x_speed = 4
    ball_y_speed = -4

    canvas.coords(pad, 10, set_pad_top, 50, set_pad_bottom)
    canvas.coords(ball, 20, set_pad_top - 10, 30, set_pad_top)

def check_game_over():
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
    if ball_top > 500:
        print("Final points:", points)
#        play_again = tk.Messagebox.askyesno(message = "Do you want to play again?")
#        if play_again == True:
#            reset()
#        else:
        close()

def main_loop():
    while windowOpen == True:
        move_pad()
        ball_move()
        window.update()
        time.sleep(0.02)
        if windowOpen == True:
            check_game_over()

window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

reset()
main_loop()