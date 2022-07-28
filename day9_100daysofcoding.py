#dictionaries
programming_dictionary = {
    "bug":"An error in teh program that prevents the program from running",
    "Loop":"A piece of code that you can easily call over and over again",
}

#extracting some specfic key of dictionary
#print(programming_dictionary["bug"])

#adding the key:value pair in the dictionary
programming_dictionary["Function"] = "The action of doing something over and over again"
#print(programming_dictionary)

#creating the empty dictionary and adding the value
empty_dictionary ={}
#adding the values in the empty dictionary
empty_dictionary["apple", "vegatables"]= "fruit", "Tomatos"
print(empty_dictionary)
#wipe the data inside the existing dictionary
#programming_dictionary = {} #wipe all the previous data
#very useful in game when you need to clear the data of the user

#edit the item inside the dictionary/ change the value
programming_dictionary["bug"] = "Error"
print(programming_dictionary) #output shows that the value of bug is update as now.

#how to loop through the dictionaries
for item in programming_dictionary:
    print(item) ##only print out the keys of the dictionary
    print(programming_dictionary[item]) #how o get both the key value (the pair in the output)


#coding assignment#9.2
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#TODO-1:
#creating the empty dictionary
student_grades = {}

#TODO-2:
#Write your code below to add the grades to student_grades.
student_grades["Harry"]="Exceeds Expectations"
student_grades["Ron"]="Acceptable"
student_grades["Hermine"]="Outstanding"
student_grades["Draco"]="Acceptable"
student_grades["Neville"]="Fail

for student in student_scores:
    #print(student)
    score = student_scores[student]
    #print(score)
    if score >= 91:
       student_grades[student] ="Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail

print(student_grades)

#nesting list and dictionaries
travel_log = [
    {
    "country":"pakistan",
     "cities_visited":["lahore","karach","rwp"],
     "Toatl_visit": 10
    },
    {
    "country":"china",
     "cities_visited":["nanchong","chengdu","chounqing","shenzen","Guangan", "suining"],
     "total_vist": "100+ times"
    },
]
print(travel_log)

#coding assignment#9.3
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited, total_visits, cities_visited):
    new_country={}
    new_country["country"] =country_visited
    new_country["visits"] = total_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#project Secret Auction Program
from replit import clear
print(logo)
#HINT: You can call clear() to clear the output in the console.
first_bidder = input("What is your name?: ")
first_bidder_amount = input("What's your bid?=$")
bidder_dic = {first_bidder:first_bidder_amount}
print(bidder_dic)