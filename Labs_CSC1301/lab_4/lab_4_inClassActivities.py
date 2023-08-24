# Problem 2: Write a program where you create a function, called employee_info(), this function will take in 6 parameters, first name, last name, department, email, rate, and annual_or_quarterly. 
# You will be calling 2 other functions within this. You will need to call format_name() and calculate_income() to help you with this function.
def employee_info(firstname, lastname, department, email, rate, annual_or_quarterly):
    name = format_name(firstname, lastname)
    salary = calculate_income(rate, annual_or_quarterly)
    info = name + "\n" + department + "\n" + email + "\n" + "\n$" + str(salary)
    return info

def format_name(firstname, lastname):
    name = lastname + ", " + firstname
    return name

def calculate_income(rate, annual_or_quarterly):
    salary = rate * annual_or_quarterly
    return salary

def main():
    firstname = input("Enter your first name: ")
    lastname = input("Enter you last name: ")
    department = input("Enter your department: ")
    email = input("Enter you email: ")
    rate = int(input("Enter your salry rate: "))
    annual_or_quarterly = int(input("Enter 1 for annual and 4 for quarterly: "))
    print()
    print(employee_info(firstname, lastname, department, email, rate, annual_or_quarterly))
main()








