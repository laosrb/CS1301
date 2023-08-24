"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_number = int(input('Enter number to use as index: '))
# input has to be in between range of 0 and 25 (n-1)
print()

print('\nThe letter at index', user_number, 'of the alphabet is', alphabet[user_number])

str = "America"
u_input = int(input("type number used as index"))
print()

print('\n', u_input, 'is the number character in america', str[u_input])

str = "America"
u_input = int(input("type number used as index"))
print()

print('\n', u_input, 'is the number character in america', str[u_input])

address = '900 Universty Ave'
address[0] = '6'
address[1] = '2'
print(address)

person_name = input()
person_age = int(input())
print('In 5 years', person_name, 'will be', person_age + 5)
# Concatenating strings
current_time = '2020-07-26 02:12:18:'

''' Your solution goes here '''
my_city = input()
my_state = input()

log_entry = current_time + " " + my_city + " " + my_state
print(log_entry)
"""
"""
# creating a liist
price = ['$20', 14.99, 5]
print(price)
names = ['Daniel', 'Roxananna', 'Jean']

print(names)

# statement my_nums that contains elements 5, 10, and 20
# my_nums = [5, 10, 20]
# print(my_nums)
# my_list = [-100, 'lists are fun']
# print(my_list)
class_grades = []
print(class_grades)
short_names = ['Gus', 'Bob', 'Zoe']

print(short_names[0])
print(short_names[1])
print(short_names[2])
# update list elements 
# lists are mutable, programmer list contents can be changed
my_nums = [5, 12, 20]
print(my_nums)

# Update a list element
my_nums[1] = -28
print(my_nums)

house_prices = ['$140,000', '$550,000', '$480,000']
house_prices[1] = '$175,000'        #update second item price
house_prices.append('$1,000,000')   #append the house price at the end to house_prices
house_prices.pop(2)                 #pop first item
house_prices.remove('$140,000')
print(house_prices)"""
