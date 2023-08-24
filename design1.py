# Prolog
# Author: Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 1301 Computer Science
# Date(finished): 9/14/22 
# Purpose: Find area of wafer (mm^2) and calculate number of dies cut from wafer given integer (dies)
# Pre condition give inputs of diameter of wafer and area of die
# Post condition make outputs in for diameter (mm), area of single die and area of wafer (mm^2), and dies not produced properly
# main function
# display introductory message
# input variable for diameter of wafer (mm)
# input variable for area of die (mm**2) or import math.* for math.pow
# calculate area for wafer
# calculate number of dies per wafer (integer)
# expected outputs wafer area (mm**2), number of dies per wafer integer ("dies")

#Implementation
# add main f(x)
# add constant from math library math.pi

# errors
# x solved - solution
#x indentation for main() - you have to indent to reuse a variable
#x not round to decimal points wafer area - use f'{var:.0f}' to control decimal point
# problem with numbers of dies cut tries to round by 0.1
import math

def main():
# use main(f(x)) and one constant from math library
# create input variables for wafer diameter and die area
# create line to calculate wafer are (mm**2)
    waf_diameter = float(input("Enter the diameter of the wafer (mm): "))
    die_area = float(input("Enter area of single die (mm^2): "))

# calculate wafer area (mm^2)= diameter / 2 * (pi) 
# calculate number of dies per wafer (int)
    waf_area = (waf_diameter / 2) ** 2 * (math.pi)
    die_num1 = (waf_area / die_area) 
    die_num2 = float((waf_diameter * math.pi) / math.sqrt(2 * die_area))
    die_waf = die_num1 - die_num2
    die_num = math.floor(die_waf)
# output results
# diameter of wafer(mm)
# die area (mm^2)
# wafer area (mm^2)
# number of dies that can be cut (int)
    print("A silicon wafer with the area of ", f'{waf_area:.2f}', "square millimeters you can cut ", die_num, "dies.")
main()
# end of main function