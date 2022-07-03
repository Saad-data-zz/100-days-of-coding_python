#Quiz 1 QUESTION

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)

#Day 1.1 (1st coding assignment)
"""Instructions
Write a program in main.py that prints the same notes from the previous lesson 
using what you have learnt about the Python print function.
Warning: The output in your program should match the example
output shown below exactly, character for character,
even spaces and symbols should be identical, otherwise the tests won't pass."""
#Write your code below this line 👇

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')") #most important

#newline character
print("Hello World\nHello "
      "World\nHello World")

#string concatenation

print("Hello" + "Samy")

#how to add the space in the "Hello and Samy"
print("Hello" + " Samy")

#Day 1.2 (2nd coding assignment)
"""Instructions
Look at the code in the code editor on the right. There are errors in all of the lines of code.
Fix the code so that it runs without errors.
Warning: The output in your program should match the example output
shown below exactly, character for character, even spaces and
symbols should be identical, otherwise the tests won't pass.
Example Output
When you run your program, it should print the following:
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n."""
#Code:

print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#Excrise
print("Hello" + input("What is your name?"))
#Day 1.3 (3rd coding assignment)
"""Write a program that prints the number of characters in a user's name. You might need to
Google for a function that calculates the length of a string.
e.g.
https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow
Warning. Your program should work for different inputs. e.g. any name that you input.
Example Input
Angela
Example Output
6"""
#Code:
x = input("What is your name? ")
print(len(x))

#Excirse

name= "Jack"
print(name)

name = "Angela"
print(name)

name=input("What is your name? ")
length = len(name)
print(length)

"""Instructions
Write a program that switches the values stored in
the variables a and b.
Warning. Do not change the code on lines 1-4 and 12-18. 
Your program should work for different inputs. e.g. any value of a and b.

Example Input
a: 3
b: 5
Example Output
a: 5
b: 3"""

#Write your code below this line 👇
a = input("a:")
b = input("b:")
print("a:",b)
print("b:",a)

# Another way
a = input("a:")
b = input("b:")
c = a
a = b
b = c


#Day 1 Project Solution
print("Welcome to the Band Name Generator.")
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
