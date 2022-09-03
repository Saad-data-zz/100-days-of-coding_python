# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(2, 99, 98, 44 ,3, 37, 7, 8, 34, 12))
#you can add ass much number of value's as much you want

#syntax example of unlimited argument
# def calculate(n, **kwargs):
#     print(kwargs)
#     n *= kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=4, multiply=6)
# this is how when we check the pack() in the tkinter it show as the  dictionary
#now let's make our our class "car"
class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)