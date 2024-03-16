import tkinter as tk
import time

window = tk.Tk()

# make a canvas and set its width, height and colour
canvas = tk.Canvas(window, width = 750, height = 500, bg = "white")
# initialise the canvas
canvas.pack()

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

# if left and right_pressed variables are 1, the pad will move
def on_key_press(event):
    global left_pressed, right_pressed
    if event.keysym == "Left":
        left_pressed = 1
    elif event.yeysym == "Right":
        right_pressed = 1

def on_key_release(event):
    global left_pressed, right_pressed
    if event.keysym == "Left":
        left_pressed = 0
    elif event.yeysym == "Right":
        right_pressed = 0

def move_pad():
    pad_move = pad_speed * right_pressed - pad_speed * left_pressed
    (pad_left, pad_top, pad_right, pad_bottom) = canvas.coords(pad)
    if (pad_left < 750 or pad_move > 0):
        if (pad_right < canvas_width or pad_move < 0):
            canvas.move(pad, pad_move, 0)

def ball_move():
    global ball_x_speed, ball_y_speed
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
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
        if (ball_left < pad_right and ball_right > pad_left):
            ball_y_speed = -ball_y_speed

    # move our ball
    canvas.move(ball, ball_x_speed, ball_y_speed)

def chaeck_game_over():
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
    if ball_top > 500:
        play_again = tk.Messagebox.askyesno(message = "Do you want to play again?")

windowOpen = True
def main_loop():
    while windowOpen == True:
        move_pad()
        move_ball()
        window.update()
        time.sleep(0.02)
        if windowOpen == True:
            check_game_over()

