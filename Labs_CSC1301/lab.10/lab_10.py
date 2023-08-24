# Prolog: Lab 10        The Rock Paper Scissors Game
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
"""
The Rock Paper Scissors Game
Please enter 1 for rock, 2 for paper,
3 for scissors or -1 to quit: 1
"""
import random
def game():
    print("The Rock Paper Scissors Game")               # prompt
    user_i = int(input("""
Please enter 1 for rock, 2 for paper,\n
3 for scissors or -1 to quit: """))
    cpu = random.randint(1,3)                           # computer's random number generator 1 - 3
    while user_i != -1:
        # User choice
        R = ''
        P = ''
        S = ''
        r = ''
        p = ''
        s = ''
        if user_i == 1: #== 0:                             # if statement from user input
            R = 0
            print("You chose rock")
        if user_i == 2: #== 0:
            P = 0
            print("You chose paper")
        if user_i == 3: #== 0:
            S = 0
            print("You chose scissors")
        # Computer choice
        if cpu == 1: # == 0:                                # computer's if statement for random choice
            r = 1
            print("The computer chose rock")
        if cpu == 2: # == 0:
            p = 1
            print("The computer chose paper")
        if cpu == 3: # == 0:
            s = 1
            print("The computer chose scissors")
        if (R == 0 and s == 1) or (P == 0 and r == 1) or (S == 0 and p == 1):
            print("Congratulations you win!")
        elif(R == 0 and p == 1) or (P == 0 and s == 1) or (S == 0 and r == 1):
            print("Sorry you lose!")
        elif user_i == cpu:
            print("The match was a tie!")
        user_i = int(input("""
Please enter 1 for rock, 2 for paper,\n
3 for scissors or -1 to quit: """))
    print("Goodbye")
game()
