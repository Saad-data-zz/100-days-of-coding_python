#
#
# class Animal():
#      def __init__(self):
#          self.num_eyes_have = 2
#
#
#      def breath(self):
#          print("Inhale, exhale")
#
# #basically inheritance allow us not to reinvent the whell from the start and and build over the pervious class
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#
#     def breath(self):
#         super().breath()
#         print("Fish can inhale and exhale inside the water")
#
#
#     def swim(self):
#         print("Fish can move inside water")
#
# choti = Fish()
# choti.swim()
# choti.breath()
# print(choti.num_eyes_have)

#Concept of Slicing

#we go the list of the piano_keys
piano_keys = ["a","b","c","d","e","f","g"]

print(piano_keys[3:6])
#if you don't type any value it measn that, then the default value is 0 on the both ends

#In addition to that we can give 3 values in the square brackets
print(piano_keys[2:6:2])
#the 3rd value is the jump in the sequence
#we can also use the - negative sign whcih means satrt from the opposite side
print(piano_keys[::-1])

#Similarly we slice the tuple
piano_tuple = ("a","b","c","d","e","f","g")
print(piano_tuple[3:5])
