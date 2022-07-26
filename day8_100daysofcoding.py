#task 1. Create the functiona and call it.
def greet():
    print("myname")
    print("my body")
    print("my_action")

greet()

#function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how are you {name}")
greet_with_name("saad")

#Task make a function which contains the name and location
def my_function(name,location):
    print(f"Hello {name}")
    print(f"I'm going to {location}")

my_function("saad","islamabad")

#Using the Keyword Arugment

def my_function(a,b,c,d):
    print(f'While 1 is equal: {c}')
    print(f'While 2 is equal: {d}')
    print(f'While 3 is equal: {a}')
    print(f'While 4 is equal: {b}')
#defiing the keyword arguments
my_function(d=2,a=3,c=1,b=4)

#day#8 coding Assignemnt 8.1
# Instructions
# You are painting a wall. The instructions on the paint can says that
# **1 can of paint can cover 5 square meters** of wall.
# Given a random height and width of wall,
# calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5  = 1.6
# But because you can't buy 0.6 of a can of paint,
# the **result should be rounded up** to **2** cans.
#
# IMPORTANT: Notice the name of the function and parameters
# must match those on line 13 for the code to work.
#Write your code below this line 👇
#import  math
def paint_calc(height,width,cover):
  area = height * width #formaula for h x w
  numb_cans = round(area / cover) #round will provide the same answer
  print(f"You'll need {numb_cans} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#day#8 coding Assignemnt 8.2


#codes
# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#project day 8:
#exercise
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
def ceasar(start_text, shift_amount, cipher_direction):
    plain_text = ""
    if cipher_direction == "decode":
        shift_amount += -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            plain_text += alphabet[new_position]
        else:
            plain_text+=char
    print(f"Here's is the {direction}d result {plain_text}")
def encrypt(plain_text, shift_amount):
    cipher_text = "" 
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encode text is {cipher_text}")
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decode text is {plain_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("goodbye")
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

#shorter and smarter version of th code









