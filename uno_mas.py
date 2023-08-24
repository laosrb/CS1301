# Prolog: Project
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
print("***")
print("\033[32m This text is Bright Green  \n", "\032[1m")
print("\032")

print("***")

print("\033[32m This text is Bright Green  \n", "\032[1m")
print("\033[33m This text is blue  \n", "\033[1m")
def grammar():
    def vowel():
        # find if it starts with vowel 
        # if True then use a instead of an
        def cap():
        # find if you need a punctuation
        # for names, places make them Capital
            return


name= input("""
    Hello 😊 , 
    What's your name? """)
s_1 = "zoo"
s_2 = "school"
s_3 = "park"
# PROMPT
prompt = ("""
____________________

Greetings, {}!
Thanks for joining us and Welcome to ZAIN's & RYAN's madlib Project. 

(〃￣︶￣)人(￣︶￣〃)

____________________

Hi, I'm your helpful robot buddy Chip here to guide you through your 
EPIC MADLIB STORY. I was told that madlibs might make any sense but 
are a great deal of fun. Tell me "stop" and I'll stop the story. 
If your ready to begin...


Please enter a storyline to begin. 
    STORYLINE:
        \032 ZOO
        \032 SCHOOL
        \032 PARK
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
    if choice == "" or choice != "zoo" and choice != "school" and choice !="park":
        print("""sorry my dumb dumb robot brain doesn't understand, please try again
    
    (*/ω＼*)
____________________

    type "stop"
    to end game
        """)
        return story()   
    else:
        return True
def newgame(choice):               # reiterates game
    choice = input("Type Zoo, School, or Park:\n").lower()
    if choice == "stop":
        print(outro)
    elif isChoice(choice) == True:
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
    if choice == "zoo":
        zoo = ("""\032 ZOO
        Reporting live from the {}, it's {} at the Zoo, with dozens of {} animals out of their enclosures! 
        {} and {} are rushing to the gates, the {}s are trying to climb the walls, it's complete chaos. 
        My good buddy, Bill, he's {}, he says he's been stuck for so long, that he just wants to 
        {} right outta here. Oh, god, I think the lions see me. They look hungry. They're growling. 
        They see {}. Why am I still standing here? I better get to my feet and {} out of here!
        """.format(place_1, name_1, adj_1, noun_1, noun_2, noun_3, adj_2, verb_1, color_1, verb_2))
        print(zoo)
        return newgame(choice)
        
    if choice == "school":
        school = ("""\032 SCHOOL
        Yesterday, I {} to school. Professor {} was {} and {}. I couldn't {} because of the 
        {}. But all of a sudden, a {} cloud came into the classroom, and none other than {} appeared! 
        He had ran through the {}, looking for a {}. He looked like he was {} for a long time. 
        He must not know it was in the {}.
        """.format(verb_1,noun_1,color_1, adj_1,verb_2, noun_2, adj_2, name_1, place_1, noun_3, place_1))
        print(school)
        return newgame(choice)

    if choice == "park":
        park = ("""\032 PARK
        The park is such a great place for {} and {} people to be at. I love seeing all the {} and {}, 
        they always so fun to play with, it's so much better than the {}. Wait... is that... Oh my god, 
        it's {}! What's {} doing here! They're here with his {}..., why the heck is it {}?! It's actually kinda {}. Huh.
        """.format(adj_1, adj_2, noun_1, noun_2, place_1, name_1, name_1, noun_3, color_1, verb_1))
        print(park)
        return newgame(choice)
def story():
    choice = input("Type Zoo, School, or Park:\n").lower()

    if choice == "stop":
        print(outro)

    elif isChoice(choice) == True:
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
    if choice == "zoo":
        zoo = ("""\032 ZOO
        Reporting live from the {}, it's {} at the Zoo, with dozens of {} animals out of their enclosures! 
        {} and {} are rushing to the gates, the {}s are trying to climb the walls, it's complete chaos. 
        My good buddy, Bill, he's {}, he says he's been stuck for so long, that he just wants to 
        {} right outta here. Oh, god, I think the lions see me. They look hungry. They're growling. 
        They see {}. Why am I still standing here? I better get to my feet and {} out of here!
        """.format(place_1, name_1, adj_1, noun_1, noun_2, noun_3, adj_2, verb_1, color_1, verb_2))
        print(zoo)
        return newgame(choice)
        
    if choice == "school":
        school = ("""\032 SCHOOL
        Yesterday, I {} to school. Professor {} was {} and {}. I couldn't {} because of the 
        {}. But all of a sudden, a {} cloud came into the classroom, and none other than {} appeared! 
        He had ran through the {}, looking for a {}. He looked like he was {} for a long time. 
        He must not know it was in the {}.
        """.format(verb_1,noun_1,color_1, adj_1,verb_2, noun_2, adj_2, name_1, place_1, noun_3, place_1))
        print(school)
        return newgame(choice)

    if choice == "park":
        park = ("""\032 PARK
        The park is such a great place for {} and {} people to be at. I love seeing all the {} and {}, 
        they always so fun to play with, it's so much better than the {}. Wait... is that... Oh my god, 
        it's {}! What's {} doing here! They're here with his {}..., why the heck is it {}?! It's actually kinda {}. Huh.
        """.format(adj_1, adj_2, noun_1, noun_2, place_1, name_1, name_1, noun_3, color_1, verb_1))
        print(park)
        return newgame(choice)
    

story()