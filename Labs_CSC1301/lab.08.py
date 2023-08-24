# Prolog: Lab 08
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 

# Step 1 - Make a List
def func_1():
    alist = list()
    makelist = int(input("Enter a number: "))
    for i in range(makelist):
        alist.append(i)
    print(f'makelist({makelist})', "# returns", alist)
func_1()
print("\n")
# Step 2 - Lift Off!
def func_2():
    empty = list()
    rocketcountdown = int(input("Type countdown number: "))
    for i in range(rocketcountdown, 0, -1):
        empty.append(i)
    empty.append('We have lift off!')
    print(f'rocketcountdown({rocketcountdown})', "# returns",empty)
func_2()
print("\n")
# Step 3 - Double Loop
def func_3():
    another = list()
    doubleloop_1 = int(input("Type a number for loop one: "))
    doubleloop_2 = int(input("Type a number for loop two: "))
    for x in range(doubleloop_1):                   # nested for loop
        for y in range(doubleloop_2):
            another.append("{}:{}".format(x,y))
    print(f'doubleloop{doubleloop_1, doubleloop_2}', "# returns", another)
func_3()