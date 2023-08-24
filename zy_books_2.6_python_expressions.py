# code_1 expressions
"""""
avg_sales = 0

num_sales1 = int(input())
num_sales2 = int(input())
num_sales3 = int(input())

# (''' Your solution goes here ''')
avg_sales = (num_sales1 + num_sales2 + num_sales3) / 3

print(f'Average sales: {avg_sales:.2f}')
"""""
# code_2 procedure rules
"""""
pi = 3.14159
sphere_volume = 0.0

sphere_radius = float(input())

# (''' Your solution goes here ''')
import math
sphere_volume = (4.0 / 3.0) * pi * math.pow(sphere_radius, 3)

print(f'Sphere volume: {sphere_volume:.2f}')
"""""

# code 3 scientific numbers 
"""
G = 6.673e-11
M = 5.98e24
accel_gravity = 0.0

dist_center = float(input())

''' Your solution goes here '''
accel_gravity = (G * M) / dist_center ** 2

print(f'Acceleration of gravity: {accel_gravity:.2f}')
"""

# code 4 modulus example 
"""
minutes = int(input('Enter minutes:\n'))
# \n new line
hours = minutes // 60
# floor division to get integer hours
minutes_remaining = minutes % 60
# modulus to convert minutes remaining
# ^ex: minutes = 75 so 75 % 60 is 75/60, 1 and 15 from 75-60 so 75 % 60 is 15

print(minutes, 'minutes is', end=' ')
print(hours, 'hours and', end=' ')
print(minutes_remaining, 'minutes.\n', end=' ')
"""

# code from modulo examples 
"""
user_val = int(input("Type number value: "))
phone_num = int(input("Enter phone number: "))
ones_digit     = user_val % 10    # Ex: 927 % 10 is 7. 
tmp_val        = user_val // 10

tens_digit     = tmp_val % 10     # Ex: tmp_val = 927 // 10 is 92. Then 92 % 10 is 2.
tmp_val        = tmp_val // 10

hundreds_digit = tmp_val % 10     # Ex: tmp_val = 92 // 10 = 9. Then 9 % 10 is 9.
# phone number prefix

tmp_val = phone_num // 10000  # // 10000 shifts right by 4, so 936555. 
prefix_num = tmp_val % 1000 # % 1000 gets the right 3 digits, so 555.
area_code = phone_num // (10 ** 7)  # // (10 ** 7) gets first 3 digits, so 936
line_num = phone_num % 10 ** 4    # phone_num % 10 ** 4 gets last 4 digits, so 1212

print(area_code, prefix_num, line_num)
"""
#"""
# code attempt to seperate phone number
p_num = int(input("Enter phone number: "))

area_code = p_num // (10 ** 7)
pre_num = p_num // (10 ** 4)
prefix = pre_num % (10 ** 3)
line_num = p_num % (10 ** 4)
print()
print("The area code is", area_code, ",", "The prefix is", prefix, ",", "The line number is", line_num, ".")
#"""
