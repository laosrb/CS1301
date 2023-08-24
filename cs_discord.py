import random
"""

def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    else:
        return True


def sumDigit(n):
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        s += d
    return s

def extraassignment1():
    
    f = open("test1.txt", "w")
    prime = open("prime1.txt", "w")
    n = int(input("How many numbers are needed to write to the file: "))
    random.seed()
    maxSumOfDigit = -1
    num = 0
    for i in range(n):
        # random number between 1 and 100
        r = random.randint(1, 100)
        f.write(str(r) + "\n")
        if isPrime(r):
            prime.write(str(r) + "\n")
        
        if sumDigit(r) > maxSumOfDigit:
            maxSumOfDigit = sumDigit(r)
            num = r
    f.close()
    prime.close()
    


    # read/show file 
    f = open("test1.txt", "r")
    prime = open("prime1.txt", "r")

    print("All numbers in the file: ") 
    for i in f:
        print(i.strip(), end=" ")
    print("\nThe list of prime numbers: ") 
    countPrime = 0
    for i in prime:
        countPrime += 1
        print(i.strip(), end=" ")
    print("\n%d prime numbers found in this file" % countPrime)
    print("%d has a maximum sum of digits = %d" % (num, maxSumOfDigit))
    f.close()
    prime.close()


extraassignment1()
"""


"""
f = open("test.txt", "w")
p = open("prime.txt", "w")
ran = random.sample(range(1,101), user_i)
num = ' '.join(str(item) for item in ran)
if (user_i % num) == 0:
    p.write(str(ran))"""
"""
f = open("test.txt", "w")
p = open("prime.txt", "w")
#user_p = int(input("Type number of numbers to be written to a file:\n"))
for i in range(2, user_i):
    # r = random.randint(1, 100)
    # f = open("test.txt", "w")
    f.write(str(ran) + "\n")
    if (user_i % i) == 0:
        p.write(str(ran) + "\n")
f.close()
p.close()
f = open("test.txt", "r")
p = open("prime.txt", "r")
print("All numbers in the file: ") 
for i in f:
    print(i.strip(), end=" ")
print("\nThe list of prime numbers: ") 

num_prime = 0
for i in p:
    num_prime += 1
    print(i.strip(), end=" ")
print("\n%d prime numbers found in this file" % num_prime)
f.close()
p.close()
"""
"""
get input of number of random numbers being created
create new text file
close text file
print 
find prime"""
"""
Create random numbers and store in text files
Find prime numbers and sore in prime files"""
# a = int(input("Type number of numbers to be written to a file:\n"))

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
    
    
python = Snake("python")
anaconda = Snake("anaconda")

# print the names of the two variables
print(python.name)
# python
print(anaconda.name)
# anaconda
# choice = input("Type Zoo, School, or Park:\n").lower()
class words:
    def madlib(choice):
        adj_1 = str(input("Type adjective:\n"))
        adj_2 = str(input("Type adjective:\n"))
        verb_1 = str(input("Type verb:\n"))
        verb_2 = str(input("Type verb:\n"))
        verb_3 = str(input("Type verb:\n"))
        noun_1 = str(input("Type noun:\n"))
        noun_2 = str(input("Type noun:\n"))
        noun_3 = str(input("Type noun:\n"))
        color_1 = str(input("Type color:\n"))
        name_1 = str(input("Type name:\n"))
        place_1 = str(input("Type place:\n"))

        if z == 1:
            zoo = words("""
            Reporting live from {}
            """.format(place_1))
            print(zoo)
# problem with printing the adj-place user input
# with the main function 
# I am trying to print zoo in class words to 
# in the main function
def main():
    choice = input("Type Zoo, School, or Park:\n").lower()
    z=0
    if choice == 'zoo':
        return words.madlib(choice)
        
main()
