# 1st coding exercise
word_list = ["ardvark", "baboon","camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
random_letter = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in random_letter:
    if letter == guess:
        print("right")
    else:
        print("wrong")

# 2nd coding exercise
word_list = ["ardvark", "baboon", "camel"]
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display = []
end_of_game= False
import random

random_letter = random.choice(word_list)
for word in range(len(random_letter)):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter").lower()
    for position in range(len(random_letter)):
        letter = random_letter[position]
        print(f"Current Position: {position}\n Curretn letter: {letter}\n Gueesed Letter: {random_letter}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win.")


#Step# 01
import random
from hangman_words import word_list
from hangman_art import logo
print(logo)

#word_list = ["ardvark", "baboon","camel"]
chosen_word = random.choice(word_list)
lives = 6
print(f'Pssst, the solution is {chosen_word}.')
#create blanks
display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
#print(display)
end_of_game = False
while not end_of_game:
    guess=input("Guess a Letter").lower()

    if guess in display:
        print(f"you already guessed: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")


#check if the user has got  all letter
    if "_" not in display:
        end_of_game = True
        print("you win")
    print(f"{' '.join(display)}")

    from hangman_art import stages
    print(stages[lives])



