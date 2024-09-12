# add the three lines of code to start our tk project
import tkinter as tk

# make the window
window = tk.Tk()

# here create the canvas
canvas = tk.Canvas(window, width=750, height=500, bg="white")
canvas.pack(padx=10, pady=10)

lastX, lastY = 0, 0
pen_colour = "black"
pen_width = 3

# this function updates lastX and lastY coordinates depending on where my mouse is at the moment
def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

# this function calls the store_posistion function when you click on the screen
def on_click(event):
    store_position(event)

# this function will draw a line by connection where my mouse is at the moment with my 
# lastX and lastY coordinates
def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=pen_colour, width=pen_width)
    store_position(event)

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

# this is to create a red rectangle
red_id = canvas.create_rectangle(10,10,30,30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = canvas.create_rectangle(10, 85, 30, 105, fill="white")


# function to change colour if clicked
def change_red(event):
    global pen_colour, pen_width
    pen_colour = "red"
    pen_width = "3"
def change_blue(event):
    global pen_colour, pen_width
    pen_colour = "blue"
    pen_width = "3"
def change_black(event):
    global pen_colour, pen_width
    pen_colour = "black"
    pen_width = "3"
def change_white(event):
    global pen_colour, pen_width
    pen_colour = "white"
    pen_width = "30"

# bind the funtion to the rectangle
canvas.tag_bind(red_id, "<Button-1>", change_red)
canvas.tag_bind(blue_id, "<Button-1>", change_blue)
canvas.tag_bind(black_id, "<Button-1>", change_black)
canvas.tag_bind(white_id, "<Button-1>", change_white)


# let the window stay on screen
window.mainloop()