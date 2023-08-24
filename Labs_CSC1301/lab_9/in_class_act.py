# Prolog: In class activity
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
"""
# Function 
def laps_to_miles(user_laps):                                       # This function converts the laps into miles
    miles = user_laps * 0.25
    return(miles)
# return for miles 
# like define main function
# one key word to define the main function
# you don't have to call
# if __name__ == '__main__': This will always execute
if __name__ == '__main__':                                          # just like def main()
    user_laps = int(input("Enter user laps: "))                     # sends user input to laps functions 
    print(laps_to_miles(user_laps))                                 # This line calls the laps function and you need to put the parameters for it
# print(f'{your_value:.2f}')
"""
# Price
"""
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
# Define your function here
    gas_used = miles_driven / miles_per_gallon
    cost = gas_used * dollars_per_gallon
    cost = f'{cost:.2f}'
    return(cost)
if __name__ == '__main__':
    miles_per_gallon = float(input("Type car's miles per gallon: "))
    dollars_per_gallon = float(input("Type price per gallon : $"))
    miles_driven = int(input("Enter miles driven: "))
    print(driving_cost(
        miles_per_gallon,
        dollars_per_gallon,
        miles_driven
    ))"""
name= input("""Hello 😊 , 
what's your name? """)
s_1 = "zoo"
s_2 = "school"
s_3 = "park"
# PROMPT
prompt = ("""
Greetings, {}
Thanks for joining us and Welcome to ZAIN's & RYAN's madlib Project. 

    (〃￣︶￣)人(￣︶￣〃)

____________________

Hi, I'm your helpful robot buddy Chip here to guide you through your 
EPIC MADLIB STORY. I was told that madlibs might make any sense but 
are a great deal of fun. Tell me "stop" and I'll stop the story. 
If your ready to begin...


Please enter a storyline to begin. 
    STORYLINE:
        > ZOO
        > SCHOOL
        > PARK
(If you want to exit type "stop")
____________________
    """.format(name))
outro = ("""
Thank you for playing I hope you enjoyed playing. Visit me soon.

    (  ￣y▽￣)╭ Ohohoho.....
    
    bye {}, 
    p.s. 
    
    <3 u
        """.format(name))    
print(prompt)
def isChoice(choice):
    if choice == "":
        print("""sorry my dumb dumb robot brain doesn't understand, please try again
    
    (*/ω＼*)
____________________

    type "stop"
    to end game
        """)
        return st()   
    else:
        return True 
def st(zoo):
# Define your function here
    choice = input("Type Zoo, School, or Park:\n").lower()
    if choice == "stop":
        finish = 0
        print(outro)
    #if isChoice(choice) == True:
    while isChoice(choice) is True:
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
        break

    zoo = ("""
        Reporting live from the {}, it's {} at the Zoo, with dozens of {} animals out of their enclosures! 
        {} and {} are rushing to the gates, the {}s are trying to climb the walls, it's complete chaos. My good buddy, Bill, he's {}, he says he's been stuck for so long,
        that he just wants to {} right outta here. Oh, god, I think the lions see me. They look hungry. They're growling. They see {}. Why am I still standing here?
        I better get to my feet and {} out of here!
        """.format(place_1, name_1, adj_1, noun_1, noun_2, noun_3, adj_2, verb_1, color_1, verb_2))
    
    return(st(zoo))
if __name__ == '__main__':
    choice = choice = input("Type Zoo, School, or Park:\n").lower()
    zoo = 0
    if choice == "zoo":
        print(st(
            zoo
    ))
"""
e = input("enter color code\n")
one = e[0]
two = e[1]
print(e[0:2])
code = str(e[0])
x = int(code, 16)
# x = hex(255)
print(x)
# Type your code here. Your code must call the function
""
# print("\033[1;32m This text is Bright Green  \n")
def grammar():
    def vowel():
        # find if it starts with vowel 
        # if True then use a instead of an
        def cap():
        # find if you need a punctuation
        # for names, places make them Capital
            return
""
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
    name_2 = str(input("Type name:\n"))
    place_1 = str(input("Type place:\n"))
"/""
def isChoice(choice):
    if choice == "":
        print("bye")
        return False
    else:
        return True
def story():
    while choice is True:
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
        name_2 = str(input("Type name:\n"))
        place_1 = str(input("Type place:\n"))
        break
        
    if choice == "zoo":
        zoo = (""f"
        "Reporting live from" + verb_1 + "school." + "Professor" 
        + noun_1 + "was" + color_1 + "and" + adj_1 + "." + 
        "I couldn't" + verb_2 + "because"
        "f"".format())
        print(zoo)
    elif choice == "school":
        school = ("f""
        "Yesterday I" + verb_1 + "school." + "Professor" 
        + noun_1 + "was" + color_1 + "and" + adj_1 + "." + 
        "I couldn't" + verb_2 + "because"
        ""f".format())
        print(school)
    elif choice == "park":
        park = (""f"Park Madlib
        park {}, {}
        "f"".format(adj_1, adj_2))
        print(park)
    else:                           # re-iterates madlib function
        print("Try agin")
        return story()
if __name__ == '__main__':
    choice = input("Type zoo, school, park:").lower
    if isChoice(choice):
        print(
            
        )

t = "hi"
t1 = "hello"
print("\033[36m"+ t +"\033[0m")
print("\033[34m"+ t1 +"\033[0m")
def color():
    "\033[34m"+ t +"\033[0m"
color()
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

    zoo = (""f"
        Reporting live from {}
        ""f".format(place_1))

    school = ("f"SCHOOL
        Yesterday, I {} to school. Professor {} was {} and {}. I couldn't {} because of the 
{}.
        "".format("\033[34m"+ verb_1 +"\033[0m",noun_1,color_1,
        adj_1,verb_2, noun_2))

def main():
    choice = input("Type Zoo, School, or Park:\n").lower()
    if choice == "zoo":
        return madlib()
    print(zoo)

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