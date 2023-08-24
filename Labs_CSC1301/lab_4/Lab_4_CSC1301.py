# Prolog
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: CSC1301
'''
  Purpose:
    Phone number breakdown

  Pre-conditions (input): 
       (Enter the 10-digit phone number)
  Post-conditions (output): 
      Breakdown of phone number (area code, prefix, line number)
      
'''
# 	Breakdown of phone number to area code, prefix, line number
#	Enter phone number? 8886504343
#	Phone number is converted to area code=888, prefix=650, line number=4343

def main():
#   Design and implementation

#   1.  Output a message to identify the program, and a blank line
    print("Breakdown of phone number to area code, prefix, line number")
    print()

#   2.  Input the 10-digit phone number
    p_num = (input("Enter phone number? "))
    
#   3.  Breakdown the phone number
    a_code = (p_num[0] + p_num[1] + p_num[2])
    prefix = (p_num[3] + p_num[4] + p_num[5])
    l_num = (p_num[6] + p_num[7] + p_num[8] + p_num[9])
#   4.  Output breakdown to area code, prefix, line number
    print()
    print("Phone number is converted to area code=", a_code, "prefix=", prefix, "line number=", l_num)
main()
# end of program file
