############DEBUGGING#####################

# Describe Problem (Problem: 1.1)
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
#solution:
#TODO Q.1 - what is the for-loop doing?
#The for-loop is looping through the range of the number 1-20, but actually it's 0-19 beacuse the
#index begain with 0.
#TODO Q.2 - When is the function meant to print "you got it?
#There are two option either you change the range or you need to change constant in the if condition
#TODO Q.3 - What are your assumptions about it?
#i is equall to the value in range and all the value in range is represted by i.

#solution code (1.1)
# def my_function():
#   for i in range(1, 21):   #we change the range from 20 to 21
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug #(problem 1.2)
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])
#soultion

# Play Computer (Problem 1.3)

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#solution:
#we're pretending the input is 1994
#let's visullize waht hapened then
# year = int(input("What's your year of birth?")) #1994
# Then every place where year it becomes 1994
# if 1994 > 1980 =True and 1994 < 1994= False:
# this as whole will return nothing because True adn false is=false
#   print("You are a millenial.")
# elif 1994 > 1994= False:
#so this will also retuns nothing
#   print("You are a Gen Z.")
#so in the output we get nothing
#Solution code:
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1995:
#   print("You are a Gen Z.")

# Fix the Errors (Problem 1.4)

# age = int(input("How old are you?"))
# if age > 18:
# print(f"You can drive at age {age}.")

# solution code:
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# solution text:
# there is the indentation error




#Print is Your Friend (Problem 1.5)
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#solution
# you need to use print function to understand the inside working of the code
#so the print fiunction is the real safer.
# #solution code:
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# #print(pages)
# #print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# #mutate([1,2,3,5,8,13])
#
# #sloution code:
#
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) #this line should be inside the loop
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
#Solution with the help of debugger we exactly know that where is the problem in the code

#Assignment 13-1
# Instructions
# - Read this the code in main.py
# - Spot the problems 🐞.
# - Modify the code to fix the program.

#Solution Code:
# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#solution Texr:
# Difference between == and = in Python
# In Python and many other programming languages, a single equal mark is used to assign a value to a variable,
# whereas two consecutive equal marks is used to check whether 2 expressions give the same value .
# = is an assignment operator
# == is an equality operator
# x=10, y=20, z=20
# (x==y) is False because we assigned different values to x and y.
# (y==z) is True because we assign equal values to y and z.

#Assignment 13-2
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.

#solution code
# year = int(input("Which year do you want to check?"))
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

#solution text:
#the error is the type error, we are taking input and when ever you take input it's basically in string data type
#we must have to convert it into integer

#Assignment code: 13-3
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing
# the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing
# the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15
# then instead of the number it should print "FizzBuzz"
#solution code
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
#Solution text:
# 1 - We must need to use the AND instead of OR. because  1 and 1 = 1 on the other hand
# OR is like 1 or 0 = 1.
#We only need one if condition and for others we can use the elif.