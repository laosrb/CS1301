#Problem 3: A half-life is the amount of time it takes for a substance or entity to fall to half 
# its original value. Caffeine has a half-life of about 6 hours in humans. Given caffeine amount 
# (in mg) as input, output the caffeine level after 6, 12, and 24 hours. 
# Use a string formatting expression with conversion specifiers to output the caffeine 
# amount as floating-point numbers.
caf_amount = int(input("Enter caffine amount (in mg): "))
caf_6hr = caf_amount / 2
caf_12hr = caf_amount / 4
caf_24hr = caf_amount / 16
print()
print("After 6 hours: ", f'{caf_6hr:.2f}', " mg")
print("After 6 hours: ", f'{caf_12hr:.2f}', " mg")
print("After 6 hours: ", f'{caf_24hr:.2f}', " mg")
