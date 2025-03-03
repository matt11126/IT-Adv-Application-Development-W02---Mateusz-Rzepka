import time
from tkinter import *
from random import randint


class ButtonWrapper:
    def __init__(self, id="", row=-1, col=-1, c=""):
        self.ID = id
        self.ROW = row
        self.COL = col
        self.COLOR = c
        self.BUTTON_OBJ = None


""" Check if two buttons have been clicked and if they are a match"""


def check_match():
    global buttons
    clicked = []
    for b in buttons.values():
        if b.BUTTON_OBJ['relief'] == "sunken":
            clicked.append(b)
    if len(clicked) >= 2:
        if clicked[0].BUTTON_OBJ['bg'] == clicked[1].BUTTON_OBJ['bg']:
            # It's a match
            clicked[0].BUTTON_OBJ.configure(fg='black', bg='black', relief='raised', state='disabled')
            clicked[1].BUTTON_OBJ.configure(fg='black', bg='black', relief='raised', state='disabled')
            # black
        else:
            clicked[0].BUTTON_OBJ.configure(fg='SystemButtonFace', bg='SystemButtonFace', relief='raised')
            clicked[1].BUTTON_OBJ.configure(fg='SystemButtonFace', bg='SystemButtonFace', relief='raised')


""" If a button is pushed, draw the correct colors"""


def button_pushed(pushed_id):
    global buttons
    # Check if we already have two buttons flipped
    clicked_count = sum(1 for b in buttons.values() if b.BUTTON_OBJ['relief'] == "sunken")
    if clicked_count >= 2:
        return  # Don't allow more than 2 buttons to be flipped simultaneously

    buttons[pushed_id].BUTTON_OBJ.configure(bg=buttons[pushed_id].COLOR, relief="sunken")
    # Because time.sleep blocks execution, the color change for the second button clicked does not take effect until
    # the function returns. So we need to use the 'after()' method
    # Parameters:
    # parent: is the object of the widget or main window whichever is using this function.
    # ms: is the time in milliseconds.
    # function: which shall be called.
    # *args: other options.
    buttons[pushed_id].BUTTON_OBJ.after(1500, check_match)


def close_options(top):
    top.destroy()


""" Save the new Row and Col values to the global game variables"""


def save_options(r, c):
    global rows, cols
    rows = r
    cols = c
    reset_game()


""" Draw and handle the options menu"""


def options():
    # Create a Toplevel window
    top = Toplevel(root)
    top.geometry("250x250")

    row_val = StringVar()
    col_val = StringVar()

    # Create an Entry Widget in the Toplevel window
    row = Entry(top, width=25, textvariable=row_val)
    row.pack()

    col = Entry(top, width=25, textvariable=col_val)
    col.pack()

    # Create a Button to print something in the Entry widget
    save = Button(top, text="Save", command=lambda: save_options(int(row_val.get()), int(col_val.get())))
    # Create a Button Widget in the Toplevel Window
    close = Button(top, text="Close", command=lambda: close_options(top))
    save.pack(pady=5, side=TOP)
    close.pack(pady=5, side=TOP)


"""
Resets the game. Will clear, reshuffle and redraw the board
Parameters: buttons - the global list of buttons
***This function requires an even number of cells on the board.***
"""


def reset_game():
    global buttons
    # Delete all buttons if any
    for b in buttons.values():
        b.BUTTON_OBJ.destroy()

    buttons = {}  # Clear the button dictionary

    # Create all new buttons and add them to the button dictionary
    for i in range(rows):
        for j in range(cols):
            id = (i * cols) + j  # Calculate the button id
            b = ButtonWrapper(id=str(id), row=i, col=j)  # Create the button meta data object
            # Create the button widget
            b.BUTTON_OBJ = Button(root, text="     ", command=lambda bid=str(id): button_pushed(bid), height=3, width=7)
            buttons[b.ID] = b  # Save the button meta data object in the dictionary

    #  Randomly assign colors to buttons, making sure there are always matching pairs
    ids = list(range(rows * cols))  # Make a list of all button IDs
    while len(ids) > 0:  # While there are still IDs in the list
        a = ids[randint(0, len(ids) - 1)]  # Pick a random button ID
        ids.remove(a)  # Remove it from the list
        b = ids[randint(0, len(ids) - 1)]  # Pick a second random button ID
        ids.remove(b)  # Remove it from the list as well
        color = colors[randint(0, len(colors) - 1)]  # Pick a random color
        buttons[str(a)].COLOR = color  # Set both buttons to the same color
        buttons[str(b)].COLOR = color

    # Set all buttons to default state
    for b in buttons.values():
        b.BUTTON_OBJ.configure(fg='SystemButtonFace', bg='SystemButtonFace', relief='raised')

    # Add all buttons to the screen
    for b in buttons.values():
        b.BUTTON_OBJ.grid(row=b.ROW, column=b.COL)


"""
Main Method
"""
rows = 5
cols = 6

buttons = {}
root = Tk()
menubar = Menu(root)  # Creating Menubar

colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New Game', command=reset_game)
file.add_command(label='Options', command=options)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

reset_game()

root.grid_rowconfigure(0, minsize=40)
root.config(menu=menubar)

root.mainloop()