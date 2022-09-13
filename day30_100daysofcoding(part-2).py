#taking the example
#calculating the BMI (Body Mass Index)

height =float(input("Height in meters: "))
weight = float(input("Weight in Kilogram: "))

#putting exceptions
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
#formula for BMI
BMI = weight / (height **2)
print(BMI)

#PROBLEM: Related to IndexError
# Issue
# We've got some buggy code. Try running the code. The code will crash and give you an **IndexError**. This is because ' \
# we're looking through the list of `fruits` for an index that is out of range.
#Instructions
# Use what you've learnt about exception handling to **prevent** the program from crashing. If the user enters' \
# something that is out of range just print a default output of `"Fruit pie"`. e.g.
#Hint
# 1. You'll need to catch the IndexError exception.
# 2. You'll need the try, except and else keywords.
# TODO: Catch the exception and make sure the code runs without crashing.
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
make_pie(4)

#PROBLEM Related to KeyError handling
# Issue
# We've got some buggy code, try running the code. The code will crash and give you a
# **KeyError**. This is because some of the posts in the `facebook_posts`
# don't have any `"Likes"`.
#
#Instructions
# Use what you've learnt about exception handling to **prevent** the program from
# crashing.
#Hint
# 1. You'll need to catch the KeyError exception.
# 2. Posts without any likes can be counted as 0 likes.

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
total_likes = 0
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass
print(total_likes)

#PROBLEM Related 