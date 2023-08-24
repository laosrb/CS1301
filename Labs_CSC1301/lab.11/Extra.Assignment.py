# Prolog: Extra Assignment 1
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301
import random
# int(input("How many numbers are needed to write to the file:"))
"""
test.txt """
"""
prime numbers found in this file

ALSO
maximum has a sum of digits """

# int(input(""))
"""
Code needs to print output"""

def prime(user_i):
    for i in range(2, user_i):
        if (user_i % i) == 0:
            return False
    else:
        return True

def sum(user_i):
    s_user_i = 0
    while user_i > 0:
        d_10 = user_i % 10
        user_i = user_i // 10
        s_user_i += d_10
    return s_user_i

def extra_1():
        
    f = open("test1.txt", "w")
    p = open("prime1.txt", "w")
    user_i = int(input("How many numbers are needed to write to the file: "))
    random.seed()
    maxsum = -1
    num = 0
    for i in range(user_i):
        ran = random.randint(1, 100)
        f.write(str(ran) + "\n")
        if prime(ran):
            p.write(str(ran) + "\n") 
        if sum(ran) > maxsum:
            maxsum = sum(ran)
            num = ran
    f.close()
    p.close()

    
    f = open("test1.txt", "r")
    p = open("prime1.txt", "r")
    print("All numbers in the file: ") 
    for i in f:
        print(i.strip(), end=" ")
    print("\n******************************")
    num_p = 0
    for i in p:
        num_p += 1
        print(i.strip(), end=" ")
    print()
    print(num_p, "prime numbers found in this file" )
    print("******************************")
    print(num, "has a maximum sum of digits =", maxsum)
    f.close()
    p.close()

extra_1()
