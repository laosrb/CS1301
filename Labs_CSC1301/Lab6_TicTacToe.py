# Prolog
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: CSC1301
# Reference: Lena Eschenbach


def main():
    ROW0 = input("ROW0: ")
    ROW1 = input("ROW1: ")
    ROW2 = input("ROW2: ")
    d = False
    v= False
    h = False
    # inputs
    # checking for diagnol, tie, and horizontal
    # diagnol
    if ROW1[1] == ROW0[0] == ROW2[2]:
        print(ROW1[1], "IS GOOD IN DIAGONAL")                #\ this direction
        d = True
    elif ROW1[1] == ROW0[2] == ROW2[0]:
        print(ROW1[1], "IS GOOD IN DIAGONAL")              #/ this direction
        d = True
    # horizontal
    if ROW0[0] == ROW0[1] == ROW0[2]:
        print(ROW0[0], "IS GOOD IN HORIZONTAL1")
        h = True
    elif ROW1[0] == ROW1[1] == ROW1[2]:
        print(ROW1[0], "IS GOOD IN HORIZONTAL")
        h = True
    elif ROW2[0] == ROW2[1] == ROW2[2]:
        print(ROW2[0], "IS GOOD IN HORIZONTAL")
        h = True
    # vertical
    if ROW0[0] == ROW1[0] == ROW2[0]:
        print(ROW0[0], "IS GOOD IN VERTICAL")
        v = True
    if ROW0[1] == ROW1[1] == ROW2[1]:
        print(ROW0[0], "IS GOOD IN VERTICAL")
        v = True
    if ROW0[2] == ROW1[2] == ROW2[2]:
        print(ROW0[0], "IS GOOD IN VERTICAL")
        v = True
    # tie
    if d == False and v == False and h == False:
        print("THIS IS TIE")
main()