#lecture2 exercise
#there is no differece between these following two numbers
x=345686
x=34_56_86 # they are actually the same
#like in maths we write 45,000,09 or 4500009 the both have the same meaning

#How to count the Alphabets in your name
"""name_count=len(input("What is your name?"))
print("Your name have", name_count, "characteristics")"""

#how to convert the data type in python
#there are 4 type of data 1. Integar  2. Strings  3. Float   4 boolean

"""a=45 #integar
b=str(4544) #string
c=453.098
print(type(a),type(b), type(c))"""
# boolean gives
#either True or False in reture of statement
#Assignment Solution 2.1

"""Instructions
Write a program that adds the digits in a 2 digit number. e.g.
if the input was 35, then the output should be 3 + 5 = 8
Warning. Do not change the code on lines 1-3.
Your program should work for different inputs. e.g. any two-digit number.
Example Input
39
Example Output
3 + 9 = 12
12"""
# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
#print(type(two_digit_number))
"""x=two_digit_number[0]
y=two_digit_number[1]
z=int(x) +int(y)
print(z)"""
####################################
#Write your code below this line 👇

#Rule for Mathematical Operators
# (3) (2) parantheses
# 3 ** 2 Exponent
# 3 * 2 multiplication
# 3 / 2 divide
# 3 + 2 Addition
# 3 - 2 subtraction

#we follow the Sequence of PEMDAS
#here the important thing the pirorty is same for follow to solve
 #parantheses and exponent
 #Multiplication and divide
 #add and subtract
 #lets have a example
print(3 * 3 + 3/3-3) #guess teh output before you run the code
#steps how python solves it multiple, divide, add and subtract.
#as told that multiple and divide are equally important but the
#sloving rule follow left --> right

#Now the same line of code will give you the out of 3
#by just changing the pirorties using PEMDAS
print(3 * (3 + 3)/3-3)
#here  python will solve the parantheses first then multiple, divide, add and subtract

#assignment# 2.2 day2

"""Instructions
Write a program that calculates the Body Mass Index (BMI)
from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. 
e.g. If a tall person and a short person both weigh the same amount,
the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg)
by the square of their height (in m):
Warning you should convert the result to a whole number.
Example Input
weight = 80
height = 1.75
Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837
26"""

"""height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#h=float(height)
#w=float(weight)
BMI= float(weight)/float(height) ** (2)
answer=int(BMI)
print(answer)"""

#Exercise
#if we divide the two integars the output will be the float
#print(3/3)
# using // double sign will giives yout he outut with the integar
#print(3//3)

#Short hand
#result = 2
#result += 4 #instead of writing the resut again using ghis short hand are quite easy
#print(result) # usefull for multiple, divide, add, subtract


#f-string
#score=9
#height=1.9
#iswining=True
#using the f-string
#just putting the f in front of the string
#print(f'your score is{score},your heighr is {height},Your are wining is{iswining}')
#short way to yor your string data

#Assignment# 2.3 day2

"""Instructions
I was reading this article by Tim Urban -
Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html
Create a program using maths and f-Strings that tells us how many days,
 weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
Warning your output should match the Example Output format exactly,
 even the positions of the commas and full stops.
Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left."""

#code:

#age = input("What is your current age?")

#int(age)
limit_age= 90
"""days_in.year=365
months_in.year=12
weeks_in.year=52"""
"""years_remaining = int(limit_age) - int(age)
days_remaining = years_remaining *365
weeks_remaining = years_remaining *52
months_remaining = years_remaining *12

print(f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left')

"""
#project#2 day2
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
sp_people = int(input("How many people to splite the bill? \n$"))

bill_withtip =  tip / 100 * bill +bill
num_spliting_people =  bill_withtip / sp_people
#final=round(num_spliting_people, 2)
#here the problem
final =  "{:.2f}".format(num_spliting_people)
print(f"Each person should pay ${final}")