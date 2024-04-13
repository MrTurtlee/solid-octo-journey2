import tkinter as tk
import random

# this is how you intialise a window
window = tk.Tk()

# this is how you make the button
button = tk.Button(window, text="Do not press this button", width = 40)
button.pack(padx=40, pady=40)

# clicking function
click_count = 0
random_quote = [
    "Seriously? Do not press it.",
    "Wow! Next time, no more button",
    "Really? Thats quite immature of you",
    "...",
    "Just don't",
    "no more after this",
    ":(",
    "Womp womp",
]

random.choice(random_quote)
# using the code above, change the below if statements so that it generates
# a random quote as long as the clicks are below 10
# if clicks are above 10, delete the button

def on_click(event):
    global click_count
    click_count = click_count + 1
    # when we first click the button:
    if click_count < 10:
        button.configure(text=random.choice(random_quote))
    else:
        button.pack_forget()

# bind the function above to the button
button.bind("<ButtonRelease-1>", on_click)


# this is to allow the window to stay on screen
window.mainloop()

