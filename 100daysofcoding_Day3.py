#exercise
# your job is to replace the mannual system with python to purchese the ticket

"""print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride!")
    age=int(input("What is your age? "))
    if age < 12:
        print("Please pay $5 for ticket")
    elif age <=18:
        print("Please pay $7 for ticket")
    else:
        print("Please pay $12 for ticket")
else:
    print("Sorry you can't ride")"""


#Asignment#3.1 day3

"""Instructions
Write a program that works out whether if a given 
number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
e.g. 86 is even because 86 ÷ 2 = 43
43 does not have any decimal places. Therefore the division is clean.
e.g. 59 is odd because 59 ÷ 2 = 29.5
29.5 is not a whole number, it has decimal places. 
Therefore there is a remainder of 0.5, so the division is not clean.
The modulo is written as a percentage sign (%) in Python.
 It gives you the remainder after a division.
e.g.
6 ÷ 2 = 3 with no remainder.
therefore: 6 % 2 = 0
5 ÷ 2 = 2 x 2 + 1, remainder is 1.
therefore: 5 % 2 = 1
14 ÷ 4 = 3 x 4 + 2, remainder is 2.
therefore: 14 % 4 = 2
Warning your output should match the Example Output format exactly,
even the positions of the commas and full stops."""

#code:
"""number = int(input("Which number do you want to check? "))

if number %  2==0:
    print('This is an even number')
else:
    print('This is an odd number')"""


"""
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese."""

"""Assignment#3.2 days3
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
BMI= (weight)/(height) ** (2)
answer=round(BMI)
#print("You BMI is",answer)
if answer <18.5:
    print(f"Your BMI is {answer}, you are underweight.")
elif answer <25:
    print(f"Your BMI is {answer}, you have a normal weight.")
elif answer <30:
    print(f"Your BMI is {answer}, you are slightly overweight.")
elif answer <35:
    print("Your BMI is {answer}, you are obese.")
else:
    print(f"Your BMI is {answer}, you are clinically abese.")"""

#Assignment# 3.3 day3 Leap year
"""year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400==0:
            print("Leap year.")
        else:
            print('Not leap year.')
    else:
        print("Leap year.")
else:
    print("Not leap year.")"""

#Assignment3.4 day3

"""Congratulations, you've got a job at Python Pizza.
 Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
Example Input
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
Example Output
Your final bill is: $28.
e.g. When you hit run, this is what should happen:"""

#code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
Bill =0
if size =="S":
    Bill +=15
elif size =="M":
    Bill=+20
elif size =="L":
    Bill +=25

if add_pepperoni == "Y":
    if size == "S":
        Bill+=2
    else:
        Bill+=3
if extra_cheese == "Y":
    Bill+=1

print(f'Your final bill is ${Bill}')


#exercise logical operator
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
Bill=0
if height >= 120:
    print("You can ride!")
    age=int(input("What is your age? "))
    if age < 12:
        Bill=5
        print("Child pay $5 for ticket")
    elif age <=18:
        Bill = 7
        print("Youth pay $7 for ticket")
    elif age >=45 and age <=55:
        print("Everything will be okay soon. Have a free ride ")
    else:
        Bill = 12
        print("Adult pay $12 for ticket")
    photo=input("Do you want have a picture?Type Y or N")
    if photo == "Y":
        Bill +=3
    print(f"Your final bill {Bill}")

else:
    print("Sorry you can't ride")


Assignment3.5 day3
"""💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73."""

#code
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
combine_name_string=name1+name2
lower_case_string=combine_name_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true= t + r + u + e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love= l + o + v + e

love_score= str(true) + str(love)
percentage=int(love_score)

if (percentage < 10) or (percentage > 90):
    print(f'Your score is {percentage}, you go together like coke and mentos.')
elif (percentage >= 40) and (percentage <= 50):
    print(f'Your score is {percentage}, you are alright together.')
else:
    print(f'Your score is {percentage}.')















