"""alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points!')
else:
    print()
# fail
alien_color = 'red'
"""
"""
tages of Living

Write an if-elif-else cahin that determines a persons stage of life. Set a value for the variable age, and then:

•    If the person is less than 2 years old, print a message that the person is a baby.
•    If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
•    If the person is at least 4 years old but less than 13, print a message that the person is a Spoiled_Brat.
•    If the person is at least 13 years old but less than 20, print a message that the person is a Youngin.
•    If the person is at least 20 years old but less than 65, print a message that the person is a College .
•    If the person is age 65 or older, print a message that the person is an elder.
"""
"""
age = int(20)
if age <= 2:
    print("the person is a baby.")
elif age <= 3:
    print("the person is a toddler.")
elif 4 <= age <= 13:
    print("the person is a Spoiled_Brat.")
elif 14 <= age <= 20:
    print("the person is a Youngin.")
elif 21 <= age <= 65:
    print("the person is a College.")
else:
    print("the person is an elder.")
"""
# repeated task 
# use logic in game
"""
while True:
    number = int(input("Enter the numeric grade: "))
    # force true or true
    # establish true
    # creates infinitne loop
    if number >= 0 and number <= 100:
        break           # break infinite loop
    else:
        print("Error: grade must be between and 0")
print(number)
"""
""" Modify this program to distinguish a grade of A - A+, B - B+ , C - C+, D and F"""
"""
number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    if grades >=
    elif grades >= 80 and grades < 90:
        print("Grade: A+")
    # and both need to be true
    elif grades >= 70 and 
    if number > 89:
        letter = 'A'
    if number > 96:
        letter = 'A+'
    elif 89 <= number <= 86:
        letter = 'B+'
    elif number == 79:
        letter = 'B'
    if number > 69:
        letter = 'C'
    else:
        print("Grade: F")
else:
    print("Error: grade must be between and 0")
print("The letter grade is", letter)"""
"""
Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral triangle.

Program: equilateral.py
Determine whether or not three input sides compose an
equilateral triangle.
"""
               
# Request the inputs
'''
# Determine the result and display it
side_1 = int(input("Type side 1: "))
side_2 = int(input("Type side 2: "))
side_3 = int(input("Type side 3: "))
if side_1 == side_2 == side_3:
    print("EQUILATERAL TRIANGLE")
else:
    print("NOT AN EQUILATERAL TRIANGLE")
'''
"""
Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle.
Recall from the Pythagorean theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides.
Program: right.py

Determine whether or not three input sides compose a
right triangle.
"""
"""               
# Request the inputs
import math
side_1 = int(input("Type side 1: "))
side_2 = int(input("Type side 2: "))
side_3 = int(input("Type side 3: "))
c = max([side_1, side_2, side_3])       # hypotenuse
# print(c, "is the hypotenuse")
a_b = side_1 **2 + side_2**2
if c**2 == a_b:
    print("The triangle is a right triangle")
# Compute the squares
else: 
    print("The triangle is not a right triangle")


# Determine the result and display it"""