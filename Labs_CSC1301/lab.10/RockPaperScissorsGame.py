# Prolog: Lab 10        The Rock Paper Scissors Game
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
import random
def game(user_i):
    while user_i != -1:
        if user_i == 1:
            print("You chose rock")
        elif user_i == 2:
            print("You chose paper")
        elif user_i == 3:
            print("You chose scissors")
        else:
            print("Goodbye")
        cpu = random.randint(1,3)
        com = "The computer chose"
        if cpu == 1:
            rock = com, cpu
        if cpu == 2:
            paper = com, cpu
        if cpu == 3:
            scissors = com, cpu
    return rock, paper, scissors
    # else:
        # while user_i in range(1,3):
if __name__ == '__main__':
    print("The Rock Paper Scissors Game")
    user_i = int(input("""
Please enter 1 for rock, 2 for paper,\n
3 for scissors or -1 to quit: """))
    """if user_i == 1:
        print("You chose rock")
    elif user_i == 2:
        print("You chose paper")
    elif user_i == 3:
        print("You chose scissors")
    else:
        print("Goodbye")
    rock, paper, scissors = game(user_i)
    print(rock)
    """
    