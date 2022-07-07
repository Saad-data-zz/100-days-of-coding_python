#randomisation
import random
"""import day4randommodule
random_integer = random.randint(1,10)
print(random_integer) #anything bwtween 1 to 10
print(day4randommodule.pi)"""
"""random_float = random.random()
random_float_range = random.uniform(10, 100) #give us the range between two numbers
#another way to get the random floating value
x=random_float *5.09888
print(x) #everytime reture new value of floating point"""

#assignment#4.1 day#4
import random
"""import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: ")) #anynumber for test
test_seed = random.randint(0, 1)

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")"""

#list (data str ucture)

"""#make a list
friends=["monica", "rachel", "phoebe", "joey", "Ross", "Chandler"]
print(friends) #you get a list
#how to change the element of list
friends[3] = "mike"
print(friends) #joey replaced by mike
#how to add the element in the list
friends.append("saad")
print(friends) #this append function will add up the one element
#if you want to add more then one element
#use the extent function
friends.extend(["saad", "aitsam"])
#remember to put the list in the function not only strings
print(friends)
#how to access the different element of list
print(friends[4]) #output -- Ross
#also can use the minuse sign to access the list elements
print(friends[-1]) #it actuallly start from the end of the list (output -- aitsam)"""

#There many more function of list
#go through the lsit document see what is possible while working with list


#Assignment#4.2 Day4
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
list_friends=[names_string]
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#print(names[0])
x=len(names)
y=random.randint(0, x-1)
name_person_pay=names[y]
print(f'{name_person_pay} is going to buy the meal today!')

#Error in List index
alphabets=["A","B","C","D","E","F","G"]
#print(alphabets[7]) #list index out of range ERROR
print(len(alphabets)) #output is 7
count_abc=(len(alphabets))
print(alphabets[count_abc-1]) #just add -1 to make index 6 to 7

#consider and example to dirty dozen a list of fruits and vegtables
dity_dozen = ["Spinach","ale","collard","mustard greens","Nectarines","hot peppers","Celery",
              "Tomatoes","Strawberries", "Apples","Grapes","Cherries","Peaches","Pears"]
fruits=["Strawberries", "Apples","Grapes","Cherries","Peaches","Pears"]
vegtables=["Spinach","ale","collard","mustard greens","Nectarines","hot peppers","Celery","Tomatoes"]
#here we got the list we want to separete fruits and vegtables
#this is nested lsiting (list within list is know as nested list)
dirty_dozen_combine=[fruits,vegtables] #this is list within list
print(dirty_dozen_combine)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

#Assignment#4.3 day4
Instructions
You are going to write a program that will mark a spot with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what the nested list looks like:
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
First, your program must take the user input and convert it to a usable format.
Next, you need to use it to update your nested list with an "x".

#code:
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 
#print(map[1],[23])
#Write your code below this row 
horizontal =int(position[0])
vertical =int(position[1])

selected_row=map[vertical-1]
selected_row[horizontal-1] ="X



