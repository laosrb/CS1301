num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if ((num1 <= num2) and (num1 <= num3)):
    print("Smallest number is ", num1)
# num1 conditional
elif ((num2 <= num1) and (num2 <= num3)):
    print("Smallest number is ", num2)
# num2 conditional
else:((num3 <= num2))
print("Smallest number is ", num3)
