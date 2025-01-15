# Program Name: Assignment1.py
# Course: IT3883/Section W02
# Student Name: Mateusz Rzepka
# Assignment Number: Assignment 1
# Due Date: 01/27/2025
# Purpose: The program prints out a text-based menu with options.
# Previous experience in CS1321/1322 & Python scripting experience & https://www.w3schools.com/python/python_syntax.asp to ensure my syntax is correct.

# Initialize an empty input buffer
input_buffer = ""

while True:  # This segment is responsible for printing out the menu
    print("Menu")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # This segment records user input
    user_input = input("Enter your selection: ")
#This segment sorts out user input and appends data, clears it or exits the program.
    if user_input == "1":
        user_in = input("Please enter the data to be added to the input buffer: ")
        input_buffer += user_in
        print("Data appended")

    elif user_input == "2":
        input_buffer = ""
        print("Buffer cleared")

    elif user_input == "3":
        if input_buffer:
            print("Current input buffer: ", input_buffer)
        else:
            print("The input buffer is empty")

    elif user_input == "4":
        print("Exiting" )
        break
    else:
        print("Choice not found, please try again")
