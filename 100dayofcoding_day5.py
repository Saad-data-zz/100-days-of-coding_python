#loop in the list
#let's take a list of fruits
furits = ["Apple", "Banana", "orange","Peach"]
for furit in furits:
    print(furit)
    print(furit +" pie")
    #output like applepie,bananapia....

#assignment#5.1 day5
student_height = input("input a list of student height ").split()
total_height=0
#student_height=list[height]
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

for height in student_height:
    total_height += height

#print(total_height)
number_of_student=0
for student in student_height:
    number_of_student +=1
average_student_height=total_height/number_of_student
print(round(average_student_height))

# input values 156 178 165 171 187
#print(number_of_student)
#total_length=len(student_height)
#sum_of_total=sum(student_height)
#average_student_height=sum_of_total/total_length
#print(round(average_student_height))

#Exersie#5.2 Day 5
#input to list 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_scores = 0
for score in student_scores:
    if score > highest_scores:
        highest_scores =score
print(f'The highest score in the class is: {highest_scores}')

#using lopp wit the range function

for n in range(1,15):
    print(n) #you can see that the output is till 14 why? because the last number is elimanted because index start from 0
#if you like to go upto the 15 then you must define teh range till 16

#We can also put the gap between the range numbers
for number in range(1,21,3):
    print(number) #this 3 in the last is the gap size between each range

#execrise
sum_of_number=0 #eqmiliter
for number in range(1,101):
    sum_of_number +=number
print(sum_of_number)

#assignment#5.4
#calculate the sum of even numbers
sum=0

for numbers in range(2, 101, 2):
    sum += numbers
print(sum)
#my code
sum=0
for numbers in range(1,101):
    if numbers %2 ==0:
        sum +=numbers
print(sum)
#two different solution of the problem

#assignment 5. day5

for number in range(1,101):
    if number % 3==0 and number %5==0:
        print("FizzBuzz")
    elif number %3==0:
        print("Fizz")
    elif number %5==0:
        print("Buzz")
    else:
        print(number)
