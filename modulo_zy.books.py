'''
x = float(input("Enter a non-negative number which is between -10 to 10: "))
exp_1 =  x % -10
exp_2 = (x % 21) - 10
exp_3 = (x % 20) - 10
exp_4 = (x % 6) + 5
print("\n")
print("\nx % -10=", exp_1, "\nx % 21=", exp_2, "\nx % 20=", exp_3) #"\n(x % 6) + 5=", exp_4)

x = 693
y = (x // 10) % 10
print(y)
'''
# credit card last 4 digits
'''
x_16 = 1234567891011125
# x_16 is the 16 digits in a credit card number
four_digit = x_16 % 10 ** 4
# use modulus to get four digits
print(four_digit)
'''

"""
amount_to_change = int(input())

num_fives = amount_to_change // 5

''' Your solution goes here '''
num_ones =  (amount_to_change % num_fives) + num_fives
# idk how to do this lol i did it the right way and idek that it was right

print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')
"""

# The pet_names.py module I don't understand this
"""
print ('Initializing pet variables...')
pet_name1 = 'Ryder'
pet_name2 = 'Jess'
pet_weight1 = 5.1
pet_weight2 = 8.5

# Executes only if file run as a script (e.g., python pet_names.py)
if __name__ == '__main__':
    print('Pet 1:', pet_name1, 'was born', pet_weight1, 'lbs')
    print('Pet 2:', pet_name2, 'was born', pet_weight2, 'lbs')
 
# A script favorite_pet.py that imports and uses the pet_names module.

import pet_names  # Importing the module executes the module contents  

print('My favorite pet is', pet_names.pet_name1, '-')
print('I remember when he weighed only', pet_names.pet_weight1, 'pounds.')
print('I love', pet_names.pet_name2, 'too, of course.')
"""
# Importing modules and executing scripts
# Gravitational constants for various planets
"""
earth_g = 9.81  # m/s^2
mars_g = 3.71

if __name__ == '__main__':
    print('Earth constant:', earth_g)
    print('Mars constant:', mars_g)

# Find seconds to drop from a height on some planets.
import constants
import math

height = int(input('Height in meters: '))  # Meters from planet

if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / constants.earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / constants.mars_g), 'seconds')
"""
"""
import math

x = float(input())
y = float(input())

''' Your code goes here '''
z = (y - x)
z = math.sqrt(z)

print(round(z, 2)) # This will output only 2 decimal places.
"""
"""
import math

x = float(input())
y = float(input())

''' Your code goes here '''
z = math.sqrt(x)
z = math.fabs(z - y)

print(round(z, 2)) # This will output only 2 decimal places.
"""
"""
import math

x = float(input())
y = float(input())

''' Your code goes here '''
z = math.pow((math.sqrt(math.fabs(x + y))), 3)

print(round(z, 2)) # This will output only 2 decimal places.
"""

"""
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

''' Your solution goes here '''
a = x2 - x1
b = y2 - y1
point_dist = math.sqrt((math.pow(a, 2) + (math.pow(b, 2))))

print('Points distance:', point_dist)
"""

"""
# raw strings and converting between an encoding and text
my_string = 'This is a \n \'normal\' string\n'
my_raw_string = r'This is a \n \'raw\' string'

print(my_string)
print(my_raw_string)


# print('The name of the game is "Fortnite".')

# print("The dog's name is \"Colby\".")	

# print('Arya\\nDrew\nBeth\\\nRudy')

# print(r'The escape sequence for single quote is \'')
address = '900 University Ave'
address[0] = '6'
address[1] = '2'
print(address)
# doesn't work
address = '900 University Ave'
address = '620 University Ave'
print(address)

street_num = '500'
street = 'Floral Avenue'
address = street_num + ' ' + street
print(address)"""
