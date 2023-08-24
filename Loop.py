# zy 书
# Loops

# Nested Loops
"""                                                                                         |
Nested loops have various uses. One use is to generate all combinations of some items. 
Ex: The following program generates all two letter .com Internet domain names. 
Recall that ord() converts a 1-character string into an integer, 
and chr() converts an integer into a character. Thus, chr(ord('a') + 1) results in 'b'.
                                                                                            
"""                                                                                         

# Example:
'''
letter1 = 'j'
while letter1 < 'k':
    letter2 = 'r'
    while letter2 <= 's':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)
'''
#'''

# Example:
i = 3
while i < 24:
    j = 2
    while j <= 12:
        print(f'{i}{j}')
        j = j + 4
    i = i + 16

'''
num_rows = int(input())
num_cols = int(input())


for i in range(num_rows):
    #num_rows *= 
    # print('*', end=' ')
    for j in range(num_cols):
        
        print('*', end=' ')
    print()
'''