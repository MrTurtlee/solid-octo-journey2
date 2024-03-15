import tkinter as tk

window = tk.Tk()

# make a canvas and set its width, height and colour
canvas = tk.Canvas(window, width = 750, height = 500, bg = "white")
# initialise the canvas
canvas.pack()

pad = canvas.create_rectangle(0, 0, 70, 10, fill = "dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill = "black")

windowOpen = True

def main_loop():
    while windowOpen == True:
        move_pad()
        move_ball()
        window.update()

        if windowOpen == True:
            check_game_over()