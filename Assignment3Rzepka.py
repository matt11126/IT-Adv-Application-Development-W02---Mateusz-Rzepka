	# Program Name: Assignment3Rzepka.py (use the name the program is saved as)
	# Course: IT3883
	# Student Name: Mateusz Rzepka
	# Assignment Number: 3
	# Due Date: 02/23/ 2025
	# Purpose: What does the program do (in a few sentences)?
	# https://docs.python.org/3/library/tkinter.html
    # https://www.geeksforgeeks.org/python-tkinter-label/
    # https://www.w3schools.com/python/python_functions.asp
    # https://realpython.com/pysimplegui-python/

import tkinter as tk

# 1mpg = 0.425143707 km/l
CONVERSION_FACTOR = 0.425143707


# function where all the data is converted into km/l
def convert():
    try:
        # user input for the # of MPG's
        mpg = entry.get()

        # convert to float in order to round decimals
        mpg = float(mpg)

        # convert mpg to km/l
        kmpl = mpg * CONVERSION_FACTOR

        # round results to 3 decimal places
        label_result.config(text="Kilometers per Liter: {:.3f}".format(kmpl))

    except ValueError:
        # show "--" if user input is invalid
        label_result.config(text="Kilometers per Liter: --")


# creates the gui main window
window = tk.Tk()
window.title("MPG to KM/L Converter")

# input field instructions
label_instructions = tk.Label(window, text="Enter MPG:")
label_instructions.pack(pady=5)


# input field entry
entry = tk.Entry(window)
entry.pack(pady=5)

# creation of result label
label_result = tk.Label(window, text="", font=("Arial", 14))
label_result.pack(pady=10)


#looks at the input and instantly runs the convert command based on user input
entry.bind("<KeyRelease>", lambda event: convert())

# Run the GUI event loop
window.mainloop()
