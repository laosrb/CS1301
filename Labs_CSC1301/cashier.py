# Prolog
# Author: Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: YOUR SECTION
# Date(finished): 9/9/22 8:12
'''
  Purpose: 
      calculate the change you are due when you buy an item in a store
  Pre-conditions (input): 
      money given to the cashier(cost of item)
  Post-conditions (output): 
      change user get back from the cashier(dollars, quarters, dimes, nickels and    pennies)
'''

from unittest import result
from xml.sax.saxutils import quoteattr

def main():
#  1.  Output a message to identify the program, and a blank line
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    print()

#  2.  Input the cost and the amount of change from user
    cost = float(input("Cost of an item? "))
    amt = float(input("Amount of money given to the cashier? "))
    print()	

#  3.  Calculate the change
    change = float(amt - cost)
    remain = change % 1
    dollar = int(change - remain)
    qrt = remain / .25
    remain = remain % .25
    qrt = int(qrt - remain)
    dme = remain / .1
    remain = remain % .1
    dme = int(dme - remain)
    nkl = remain / .05
    remain = remain % .05
    nkl = int(nkl - remain)
    pny = remain / .01
    remain = remain % .01
    pny = float(pny - remain)
    Pny = round(pny)
# round pny.var b/c of .001 value off
# int data type b/c dollar, qrt, dme, and nkl use as a numerical value in math operator subtraction
#-ok-test case 1 input 0.99 _ output Pennies= 1
# error 1 change output was wrong giving more change than what should be given
# error 2 failed to give me any dimes
# error 3 did not define qrt before using it on the right side of the 2nd qrt.var
#-fail-test case 2 input 1.57 _ output $=1, qrt= 1, dme=4, nkl=8, pny=43
#-ok-add remain variable = change.var mod 1, and remain.var is used for each change type
# wow this was hard
# i will take a break watching the hr long video of pythons for beginners wish me luck future ryan
# wow the solution was easier than i thought
#  4.  Output resulting change 
    print("Change is converted to dollars=", dollar,"Quarters=", qrt,"Dimes=", dme,"Nickels=", nkl,"Pennies=", Pny)
main()
# end of program file