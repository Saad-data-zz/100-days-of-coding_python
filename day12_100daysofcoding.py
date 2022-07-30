
#Scope
#code example: 12.1
enemies = 1   #suppose this is the tree outside the house / because it's outside the function.


def increase_enemies():
    enemies =2 #apple tree inside the house
    print(f"enemies inside the block of code:{enemies}") #calling the enemies inside the function


increase_enemies()
print(f"enemies outside the block of code: {enemies}") #outside the function
#This code is example is similar to the apple tree.

#concept of local Scope
#code example 12.2


balls_left =10
#global scope


def calculate_balls():
    balls_left =5
    # local scope

calculate_balls()
print(f"left balls: {balls_left}")


#why the output: 10 because on the top of the function w defined the global scope

#nested local socpe
#code example 12.3
#this code is to understand the concept of the how local scope actual work adn we defined the local variable in the function


life_count = 100


def life_game():
    def total_life():
        life_count = 500
        print(f"life count inside the block:{life_count}")

    total_life()


print(f"life count outside the block:{life_count}")


#Dose python have the Block Scope
#the answer is no
#taking a exampl of if condition


game_level = 3
enemise =["skeleton","Zombie","Alien"]


#the code perfectly work why is just because in the if condition or loops
#there will be no local or glaob scope#but if we out the same cade in the function
#let see wat happened
def new_game():
    if game_level <5:
        new_enemies = enemise[0]
    print(new_enemies)
#here we have to put the print statement inside the function otherwise it gives error
#the impotant point th understadn here is
#if we defined the function then the print statment should be inside the function
#in the blocl otherwise it wouldn't work at all

#how to modify the global variable
enemies =  1   #global variable

#modifing the global varible in the function is very risky adn cause bugs
#you can read through the global varibale use them but don't modofy them
#specially in the function
#it's a very bad idea to give a same name to global and local variable
#here we gave the same name for to make things clear.
def increase_enemies():
    #this is the one way of modifcation of global variable
    #global enemies
    #enemies +=1
    #Another way for the modification
    #using the return function
    return enemies +1
    print(f"enemies inside the block of code:{enemies}")
    #calling the enemies inside the function


increase_enemies()
print(f"enemies outside the block of code: {enemies}")

#Constant and global scope
#code Example: 12.4
PI =3.14
URL = "http//www.google.com"
TWITTER_HANDLE = "@saadxxxxx"


def a_function(a_parameter):
    a_variable = 15
    return a_parameter

a_function(10)
print(a_variable)
