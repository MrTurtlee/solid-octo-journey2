# add the three lines of code to start our tk project
import tkinter as tk

# make the window
window = tk.Tk()

# here create the canvas
canvas = tk.Canvas(window, width=750, height=500, bg="white")
canvas.pack(padx=10, pady=10)

lastX, lastY = 0, 0
pen_colour = "black"

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
    canvas.create_line(lastX, lastY, event.x, event.y, fill=pen_colour, width=3)
    store_position(event)

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

# let the window stay on screen
window.mainloop()