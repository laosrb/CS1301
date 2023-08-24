"""
Things I am still confused about
1. Recursive Functions
2. ASCII
3. file format
"""
# Recursion
"""def Recursion(num):
    print(num)
    #if num % 2 != 0:
    #    print("please enter an even number")
    if num == 3:
        return num
    else:
        return Recursion(num-3)
Recursion(9)"""
"""
Base case printed last"""
# Fibonacci number loop
"""def Fibonacci(idx):
    sequence = [0,1]
    for i range(idx):
        sequence.append(sequence[-1]+sequence[0])
    return sequence[-1]"""

def fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return fibonacci(idx-1) + fibonacci(idx-2)
print(fibonacci(0))