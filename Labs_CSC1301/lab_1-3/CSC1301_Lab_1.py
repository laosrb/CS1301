# Prolog 9_1_2022
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 040
'''
  Purpose: 
      convert miles to kilometers, using fact that we multiply 1.6 to each mile.
  Pre-conditions (input): 
      mile (floating point)
  Post-conditions (output): 
      kilometers, floating point with 2 decimals rounded
'''

def main():
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Conversion of miles into kilometers")
    print()

#  2.  Input miles from user
    miles = float(input("Enter miles: "))
    # syntax error b/c of missing ) of miles variable
    
#  3.  Conversion of miles into kilometers
    # 1 kilometer = 1 mile * 1.6
    km = miles * 1.6
    # two ** which processed as exponent which should be multiplying 1.6
    
#  4. Output resulting given miles converted into kilometers
    print()
    print(miles, "miles is {:.2f}".format(km), "kilometers")

main()
# end of program file
