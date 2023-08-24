
"""def change():
    change = input("Enter change amount:\n")
    if change is 0:
        print("no change")
    else:
        result = change // 100
        for x in range(100,1):
            for y in range(100,1):
                solve1 = ()
def quarter():
    result """
"""
def exact_change(user_total):
    cents = user_total
     # HINT: Floor
    # cents = input_val
    num_quarters = (cents // 25) 
    cents = cents - (num_quarters*25)

    
    num_dimes = (cents // 10) 
    cents = cents - (num_dimes *10)
    num_nickels = cents // 5
    cents = cents - (num_nickels)
    num_pennies = cents
    return cents

if __name__ == '__main__': 
    input_val = int(input("Enter value:\n"))    
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    # exact_change(input_val)
    print("Number of quarters", num_quarters)
    # Type your print statement here.

"""
# Swap variable values
"""
def swap_values(user_i):
    list_1[0] = list_1[1]
    list_1[1] = list_1[0]
    list_1[2] = list_1[3]
    list_1[3] = list_1[2]
    return(user_i)
if __name__ == '__main__':
    list_1 = input(")
    list_2 = input(")
    list_3 = input(")
    list_4 = input(")
    swap_values(user_i) = list_1, list
    print()"""
def swap_values(user_1, user_2, user_3, user_4):
    temp = user_1
    user_1 
