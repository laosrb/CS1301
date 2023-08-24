"""zy책 section 4
user_num = int(input("Type a number: "))
if user_num <= 9:
    print("1")
elif user_num >= 11:
    print("2")
else:
    print("3")
"""
"""
num_puppies = 6
   
if num_puppies <= 4:
    print('c')
else:
    print('d')
   
print('k')
""

a = 'shark'
b = 'tiger'
c = [a, b]
d = c
d[0] = 'mouse'

if (c is d):
    print('f')
if (a is d[0]):
    print('g')
if (b is d[1]):
    print('h')
""
num_items = 5

if num_items > 3:
   print('b')
elif num_items < 8:
   print('e')
else:
   print('h')
   
print('p')
""

num_sandwiches = 5

if num_sandwiches < 2:
   print('c')
elif num_sandwiches > 7:
   print('f')
else:
   print('g')

print('m')
"""
num_boxes  = 0
num_apples = 9 

if num_apples < 10:
    if num_apples < 5:
        num_boxes = 1
    else: 
        num_boxes = 2
elif num_apples < 20:
    num_boxes = num_boxes + 1