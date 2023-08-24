# Prolog: Lab 11
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
import random
"""
f = open("test.txt", "w")
user_i = int(input("Type number of numbers to be written to a file:\n"))
ran = random.sample(range(1,101), user_i)
num = ' '.join(str(item) for item in ran)
f.write(num)
f.close()
f = open("test.txt", "r")
print(f.readline())
"""
def prime(user_i):
    for i in range(2, user_i):
        if (user_i % i) == 0:
            return False
    else:
        return True
def main():
    f = open("test.txt", "w")
    p = open("prime.txt", "w")
    user_i = int(input("How many numbers are needed to write to the file: "))
    random.seed()
    num = 0
    for i in range(user_i):
        ran = random.randint(1, 100)
        f.write(str(ran) + "\n")
        if prime(ran):
            p.write(str(ran) + "\n") 
    f.close()
    p.close()

    
    f = open("test.txt", "r")
    p = open("prime.txt", "r")
    print("All numbers in the file(test.txt): ") 
    for i in f:
        
        print(i.strip(), end=" ")
    print("\n******************************")
    num_p = 0
    for i in p:
        num_p += 1
        print(i.strip(), end=" ")
    print()
    print(num_p, "prime numbers found in this file(prime.txt)" )
    f.close()
    p.close()


main()
