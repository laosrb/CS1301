# Prolog: Lab 09
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
# Step 1: Look Through Lab
"""
example = 'ABCDEF'
color = ""                              # color code is the six digit code the user enters
"""
# Step 2: Writing get_red
def get_red(color):                     # I made a for loop to allow the user to skip testing functions
    for frst in color:
        frst = color[0:2]
        convert = int(frst, 16)
        return(convert)
        continue
# Step 3: Writing get_green
def get_green(color1):                   # green's color code is '--62--'  should output 98
    for mid in color1:
        mid = color1[2:4]
        convert = int(mid, 16)
        return(convert)
        continue
# Step 4: Writing get_blue
def get_blue(color2):                    # blue's color code is '----85'  should output 133
    for last in color2:
        last = color2[4:6]
        convert = int(last, 16)
        return(convert)
        continue
# Step 5: Writing id_protanopia
def id_protanopia(color_id):
    for red in color_id:
        red = (get_red(color_id))
        if red < 64:                            # if less than 64 return(True)
            return(True)
        else:
            return(False)
        continue
# Step 6: Writing id_deuteranopia
def id_deuteranopia(color_id1):
    for green in color_id1:
        green = (get_green(color_id1))
        if green < 64:                            # if less than 64 return(True)
            return(True)
        else:
            return(False)
        continue
# Step 7: Writing id_tritanopia
def id_tritanopia(color_id2):
    for red in color_id2:
        red = get_red(color_id2)
        green = get_green(color_id2)
        blue = get_blue(color_id2)
        if blue > 0 and red > 230 and green > 220:                            # if blue is less than 0, red is greater than 230, and green is greater than 220 return(False)
            return(False)
        else:
            return(True)
        continue
if __name__ == '__main__':                  # prints each function
    print("Enter a six digit color code in hexidecimal form:\n- - - - - -")
    color = input("Type color code for red:\n")
    print(get_red(color))
    color1 = input("Type color code for green:\n")
    print(get_green(color1))
    color2 = input("Type color code for blue:\n")
    print(get_blue(color2))
    color_id = input("Type color code for protanopia:\n")
    print(id_protanopia(color_id))
    color_id1 = input("Type color code for deuteranopia:\n")
    print(id_deuteranopia(color_id1))
    color_id2 = input("Type color code for tritanopia:\n")
    print(id_tritanopia(color_id2))