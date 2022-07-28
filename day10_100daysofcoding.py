#function with output
#convert the user input to title case regardless what they input

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    #print(f"{formatted_f_name} {formatted_l_name}")
    return (f"{formatted_f_name} {formatted_l_name}")
#print(format_name("sAaD", "HaSaN"))

#code for taking input from the user for and if the input not valid stop the code

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "ATTENTION! You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    #print(f"{formatted_f_name} {formatted_l_name}")
    return (f"Title case full Name: {formatted_f_name} {formatted_l_name}")
print(format_name(input("What's your first name?"),input("Whats your last name?")))

#coding execirse 10.1
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year, month):
#     """Take the year and the month return the days in that
#     specific year's month"""
#     if year <1000:
#         return "You have typed the invalid input in year"
#     elif month >12 or month <= 0:
#         return "You have typed the invalid input in month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month -1]
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

#project day10
#building the calculator
from art_calculator import logo
print(logo)
def add(n1, n2):
    """Add function"""
    return n1 + n2
def subtract(n1, n2):
    """perfrom subtraction between two numbers"""
    return n1 - n2
def multiple(n1, n2):
    """perform multiplication between two numbers"""
    return n1 * n2
def divide(n1, n2):
    """perform divide between two numbers"""
    return n1 / n2
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" : divide
}
#ask the user for the number and that number must be converted into the int
def calculator():
    num_1 = float(input("What's the first number you like to enter?: "))

#op=input("which operation you want to do?:)
    for sign in operators:
        print(sign)
    should_continue = True

    while should_continue:
        operation_sign = input("Pick an operation: ")
        num_2 = float(input("What's the next number you like to enter?: "))
        calculation_function = operators[operation_sign]
        answer = calculation_function(num_1, num_2)

        print(f"Here you go: {num_1} {operation_sign} {num_2} = {answer}")
        # for sign in operators:
        #     print(sign)
        # operation_sign = input("Pick an operation from the above: ")
        # num_3 =int(input("What's the next number?: "))
        # calculation_function = operators[operation_sign]
        # second_answer = calculation_function(calculation_function(num_1,num_2), num_3)
        #
        # print(f"{first_answer} {operation_sign} {num_3} = {second_answer}")
        if input(f" Type 'y' to continue calculating with {answer}, or type 'n' if you start a new calculator") == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()

calculator()