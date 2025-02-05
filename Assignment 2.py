o	# Program Name: Assignment2.py
o	# Course: IT3883/
o	# Student Name: Mateusz Rzepka
o	# Assignment Number: Assignment 2
o	# Due Date: 02/07/2025
o	# Purpose: The program calculates a students average and sorts all students by grade average.
o	# https://www.dataquest.io/blog/read-file-python/   https://www.datacamp.com/tutorial/python-split-list





#Open text file to read data
f = open("input.txt", "r")


# Store contents from the file in a list called lines
line = f.read().splitlines()
f.close()
# List to store student data
students = []
i = 0


while i < len(line):
    #Distinguishes between empty and non empty lines
    if line[i] != "":
        # splitting the line to distinguish name from grade
        parts = line[i].split()
        # Grabbing the student name
        name = parts[0]
        total = 0.0
        count = 0
        # Processing the data for each student
        j = 1


        while j < len(parts):
            grade = float(parts[j])
            # Add the grade to the total.
            total = total + grade
            count = count + 1
            # Next grade
            j = j + 1


        #Calculating average grade
        average = total / count


        #Add name and average to the student list
        students.append([name, average])


    # Next student to be processed
    i = i + 1


#Sort the students by grade average
students.sort(key=lambda student: student[1], reverse=True)


# Print the sorted results from the students list
k = 0
while k < len(students):
    name = students[k][0]
    avg = students[k][1]
    print(name, format(avg, ".2f"))
    k = k + 1
