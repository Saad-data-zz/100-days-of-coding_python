#How to create yourown class
#we're going to use the key word class then put the name of the class
#class User:
   #pass
#we want to leave the user class empty but in python in the function if you leave it empty then it gives you the indentation error
#so we used the key word "pass" whcih means we don't want to add anything in the functiona dn just pass

#user_1 = User()

#we also seen that the name of the classes in python first letter of every single word is capital.
#This particular type of naming is called the Pascal Case.
#there is another type of class called camel case. In this every first is lower case adn evry subsequent words have first letter capital
#one more type is the snake_case in which allthe words are lower case but separted with the uunderscore
#In python you will see the PascalCase for Class Name
#and the snake_case is used for every other thing,
#you will not see the camel case in python.

#Creating the Attributes
#
# user_1.id = "001"
# user_1.username = "samy"
# print(user_1.username)
#here the user is the object and the variable after the dot is the attribute

#code example: 17.1


#attributes for user1
# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         #self.id is the attribute and user is the parameter we're passing to attribute
#         #there is another concept of default value so that you don't to pass it from the parameter
#         self.follower = 0
#         self.following = 0
#         print("new user being created")
#
#         #whenever the new user is created it return what is written in print function
#
#
#     def follow(self, user):
#         user.follower += 1
#         self.follower += 1
#
#
#
# user_1 = User("001","samy")  # here in te class we pass the value to the parameter which finally gonna be fit it to attribute self.id
# user_2 = User("007", "james bond")
# so now down here we down need to create this extra attributes
# user_1.id = "001"
# we also defined this in our init function
# user_1.username = "samy"

# print(user_1.id, user_1.username)
# print(user_1.follower) #in the output it return zero
#with the help of this function we able to reduce alot of code and make it more simpler

# user_1.follow(user_2)
# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)


#attributes for user1
# user_2 = User()
# user_2.id = "002"
# user_2.username = "samy"
# print(user_2.username)


#Adding Method to th class
#methods is the thing which object dose


