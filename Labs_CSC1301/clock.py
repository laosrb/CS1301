# Prolog
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: CSC1301
# Reference: Pavan Indukuri
""" 
Clock that wakes someone up 40 minutes early
maybe use conditionals
Prompt
Asks for 2 integers
"""
"""
print("The hour of the day that Road Runner needs to get out of bed is", hr, "hours.")
# print statement of hr
print("The minute of the day that Road Runner needs to get out of bed is", min, "minutes.")
"""
# set conditionals for time
# print(time)
# print(hr) 
def main():
    hr = int(input("Enter the hours: "))
# input variable hour
    min = int(input("Enter the minutes: "))
    if int(min) >= 40:
        new_hr = hr
        new_min = min - 40
        num = str(new_min).zfill(2)
        print(str(hr) + ":" + str(num))
    elif hr == 0:
        new_hr = 23
        new_min = min + 20
        print(str(new_hr) + ":" + str(new_min))
    else:
        new_hr = hr - 1
        new_min = min + 20
        num = str(new_hr).zfill(2)
        print(str(num) + ":" + str(new_min))
main()