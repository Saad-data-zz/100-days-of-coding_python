# 2nd coding exercise
word_list = ["ardvark", "baboon","camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display=[]
import random
random_letter = random.choice(word_list)
word_length = len(random_letter)

for word in range(word_length):
    display += "-"

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for position in range(word_length):
    letter = random_letter[position]
    
    if letter == guess:
        print("right")
    else:
        print("wrong")
        