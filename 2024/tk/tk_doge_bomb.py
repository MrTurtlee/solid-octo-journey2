import tkinter as tk
import random

game_over = False
score = 0
squares_to_clear = 0

bombfield = []

# Helper Functions
def print_bombfield(bombfield):
    for row_list in bombfield:
        print(row_list)


def on_click(event):        
    global score
    global game_over
    global squares_to_clear

    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    current_text = square.cget("text")

    # Checking Game Over
    if game_over == False:
        if bombfield[row][column] == 1:
            game_over = True
            square.config(bg = "red")
            print("Game Over! You clicked on a bomb")
            print("Your score was:", score)
        else:
            square.config(bg = "brown")
            total_bomb = 0
            if row < 9:
                # check bot row
                if bombfield[row + 1][column] == 1:
                    total_bomb = total_bomb + 1
            
            if row < 0:
                # check top row
                if bombfield[row - 1][column] == 1:
                    total_bomb = total_bomb + 1
            
            if column < 0:
                # check left column
                if bombfield[row][column - 1] == 1:
                    total_bomb = total_bomb + 1
            
            if column < 9:
                # check right column
                if bombfield[row][column + 1] == 1:
                    total_bomb = total_bomb + 1
            # if cell is not at the very top or at left
            
            if row > 0 and column > 0:
                # check top left corner
                if bombfield[row - 1][column - 1] == 1:
                    total_bomb = total_bomb + 1
            
            if row < 9 and column > 0:
                # check bottom left
                if bombfield[row +1][column - 1] == 1:
                    total_bomb = total_bomb + 1
            
            if row > 0 and column < 9:
                # check top right
                if bombfield[row - 1][column + 1] == 1:
                    total_bomb = total_bomb + 1
            
            if row > 9 and column < 9:
                # check bottom right
                if bombfield[row + 1][column + 1] == 1:
                    total_bomb = total_bomb + 1

           
            # display total amount of bombs to the cell
            square.config(text = " " + str(total_bomb) + " ")

            score = score + 1
            squares_to_clear = squares_to_clear - 1

            if squares_to_clear == 0:
                game_over = True
                print("Well done! Great job for completing the bombfield game!")
                print("Your score was:", score)


# Main Functions
def create_bombfield(bombfield):
    # whomp whomp
    global squares_to_clear

    for row in range(0,10):
        row_list = []
        for column in range(0,10):
            # probability of adding bomb is 20%
            if random.randint(1,100) < 20:
                row_list.append(1)
            else:
                row_list.append(0)
                squares_to_clear = squares_to_clear + 1
        bombfield.append(row_list)

def layout_window(window):
    for row_number, row_list in enumerate(bombfield):
        for column_number, coumn_value in enumerate(row_list):
            # here, we are using probability to create random green colours for each
            #square
            if random.randint(1,100) < 25:
                square = tk.Label(window, text = "    ", bg = "darkgreen")
            elif random.randint(1,100) < 75:
                square = tk.Label(window, text = "    ", bg = "seagreen")
            else:
                square = tk.Label(window, text = "    ", bg = "green")
            # this code places our squares into a grid with a specified
            # row number and column number based off our bombfield matrix
            square.grid(row = row_number, column = column_number)
            square.bind("<Button-1>", on_click)


# main function to run
def play_bombdoger():
    # function to create the bombfield
    create_bombfield(bombfield)
    
    # print_bombfield(bombfield)

    # create the tk window
    window = tk.Tk()

    # function to visually layout the game
    layout_window(window)
    
    # keeps the window on screen
    window.mainloop()

play_bombdoger()