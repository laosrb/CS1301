# Prolog Homework 2 
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: CSC1301
"""
*** findingFactors ***
Please provide an integer: 42
The factors of integer 42 are: [1, 2, 3, 6, 7, 14, 21, 42].
Give 3 P's  Purpose, pre, and post condition
    main function
    Display introductory message 
    Your design here
"""
# Purpose:          Given user input of an integer and return a list of factors in the following string.
# Pre-Condiiton:    Give inputs of integers, If integer is negative than return facor has no factors
# Post-Condiiton:   Return list of integer 
# Write an introductory message
""" 
This program uses input; you will have to prompt the user for the inputs. The inputs can be assumed to be integers.
● You must download helper.py from icollege (to the folder that has your solution) and import helper.py (do not copy the code from the helper.py file, you must only import) 
● You must use at least two functions and use helper.findingFactors() from helper.py to find if the number is prime. 
● Find a prime number should be its own function and should be called foundFactors that prints the desired output message
● You should have a main function and you should call foundFactors to find out if the number is prime or not.
● Make sure you format the lines of the output as described. The line breaks and the punctuation should be as shown. The output messages should be exactly as given
"""
# import helper.py file   
# define main function
# define foundFactors method that prints desired output message find prime number
def main():
    print("     *** findingFactors ***")                    # introductory message
    # print introductory message
    user_int = int(input("Please provde and integer: "))    # user input integer statement
    # print input statement
    '''Type code that returns list of factors for the user's integer input'''
    # create conditonal that determines if user input is negative, positve, or zero
    # conditional that returns the list of integers for factors
    # If the integer is negative or zero, you will need to say the integer has no factors.
    # create a code that solves the factors of given user input of an integer
    # create code that solves the factors of the users integer
    print("The factors of integer", user_int, "are: ")
    # create conditional statement for negative or zero user_int
    if user_int <= 0:
        print("The integer", user_int, "has no factors.")
    # output statement
main()