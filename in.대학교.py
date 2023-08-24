"""with open("t.txt", 'w', encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file is Str8 Gucci \n\n")
    f.write("contains three lines... We G'eed up")"""
"""
a = input("Type y or n:")
y = "true"
def y():
    print("true")
y()
def main():
# function defined
	if a == "y":
		return(y)
	else:
		print("false")
main()
# function called
"""
# zybooks   Functions
"""def main():
    c1 = (f1 - 32.0) * (5.0 * 9.0 )
    c2 = (f2 - 32.0) * (5.0 * 9.0 )
    c3 = (f3 + 32.0) * (5.0 * 9.0 )"""
"""
verb_1 = input("Enter a verb of choice, and press enter:")
adj_1 = input("Enter an adjective of choice, and press enter:")
verb_2 = input("Enter second verb of choice, and press enter:")
body_part = input("Enter a body part name of choice, and press enter:")
adverb = input("Enter an adverb of choice, and press enter:")
body_part_2 = input("Enter any body name of your choice,and press enter:")
noun = input("Enter a noun of choice, and press enter:")
verb_3 = input("Enter the third verb of choice, and press enter:")
animal = input("Enter name of any animal of choice, and press enter:")
noun_2 = input("Enter an noun of choice , and press enter:")
verb_4 = input("Enter the fourth verb of choice, and press enter:")
adj_2 = input("Enter an adjective of chioce, and press enter:")
color = input("Enter any color name, and press enter:")



story = "Most doctors agree that bicycle of" + verb_1 
+ " is a/an " + adj_1 + " form of exercise." + verb_2 
+" a bicycle enables you to develop your " 
+ body_part + " muscles as well as " + adverb 
+ " increase the rate of a " + body_part_2
+" beat. More " + noun + " around the world "+ verb_3 
+" bicycles than drive "+ animal +". No matter what kind of "
+ noun_2 +"you "+ verb_4 +", always be sure to wear a/an "+ adj_2 
+" helmet.Make sure to have  " + color + " reflectors too! "



print(story)
import sys
from termcolor import colored, cprint
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
import colorama
from colorama import Fore

print(Fore.RED + 'This text is red in color')"""
"""a= input()
b= input()
print(
    "
    hello {}
    how are you {}
    ".format(a,b)
)
string="hello how are you"
uppercase_string=string.capitalize() 
print(string.capitalize())
one = input("type something:\n").lower()
print(one)"""
"""def f(n):
    if n>1:
        print("still")
    f(n/2)
f(32)"""
"""class C:
    def func1(self):
        self.var1 = "something"

    def func2(self):
        print(self.var1)

foo = C()
foo.func1()
foo.func2()
t = "hi"
t1 = "hello"
print("\033[36m"+ t +"\033[0m")
print("\033[34m"+ t1 +"\033[0m")
def color():
    "\033[34m"+ t +"\033[0m"
color()
class words:
    def madlib():
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


        zoo = (""
        Reporting live from {}
        "".format(place_1))

        school = (""SCHOOL
        Yesterday, I {} to school. Professor {} was {} and {}. I couldn't {} because of the 
{}.
        "".format("\033[34m"+ verb_1 +"\033[0m",noun_1,color_1,
        adj_1,verb_2, noun_2))
choice = input("Type Zoo, School, or Park:\n").lower()
def main():
    

    if choice == "zoo":
        return (words.madlib())

    if choice == "school":
        return madlib ()
        print(school)
    if choice == "park":
        return madlib ()
        park = (""PARK
        park {}, {}
        "".format(adj_1, adj_2))
        print(park)
        finish = 3
    print(madlib())
main()"""
"""list = []
t = str("hi")
r = str(("\033[34m"+ input("type:\n") +"\033[0m"))
a = str("bye")
list.append(r)

# print("\033[1;32m This text is Bright Green  \n")
tra = ("f""
hello I'm {}, nice to meet you. {} I'm actually a robot. What do you have planned robot?
My battery is actually low so I'm probably goin... 
.__.
{} robot
it was nice talking to you""f".format("\033[34m"+ r, t, a +"\033[0m"))
print(tra)"""
'''def st(miles_per_gallon, dollars_per_gallon, miles_driven):
# Define your function here
    choice = input("Type Zoo, School, or Park:\n").lower()
    if choice == "stop":
        finish = 0
        print(outro)
    if isChoice(choice) == True:
        adj_1 = str("\033[34m"+ input("Type adjective:\n")+"\033[0m")
        adj_2 = str("\033[34m"+ input("Type adjective:\n")+"\033[0m")
        verb_1 = str("\033[34m"+ input("Type verb:\n")+"\033[0m")
        verb_2 = str("\033[34m"+ input("Type verb:\n")+"\033[0m")
        verb_3 = str("\033[34m"+ input("Type verb:\n")+"\033[0m")
        noun_1 = str("\033[34m"+ input("Type noun:\n")+"\033[0m")
        noun_2 = str("\033[34m"+ input("Type noun:\n")+"\033[0m")
        noun_3 = str("\033[34m"+ input("Type noun:\n")+"\033[0m")
        color_1 = str("\033[34m"+ input("Type color:\n")+"\033[0m")
        name_1 = str("\033[34m"+ input("Type name:\n")+"\033[0m")
        place_1 = str("\033[34m"+ input("Type place:\n")+"\033[0m")

    gas_used = miles_driven / miles_per_gallon
    cost = gas_used * dollars_per_gallon
    cost = f'{cost:.2f}'
    return(cost)
if __name__ == '__main__':
    choice = choice = input("Type Zoo, School, or Park:\n").lower()
    print(st(
        adj_1
    # ))'''

i = 1
while i < 18:
    j = 4
    while j <= 8:
        print(f'{i}{j}')
        j = j + 3
        i = i + 15

letter1 = 'j'
while letter1 < 'k':
    letter2 = 'r'
    while letter2 <= 's':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

print('hi')