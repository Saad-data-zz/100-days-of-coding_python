# the concept of the list comprehension
#noramlly if we like to create tyhe list from list we usethe for loop

# num_list = [1,2,3,4,5]
# new_list = []
# for n in num_list:
#     add_1 = n +1
#     new_list.append(add_1)
# print(new_list)

#now using the list comprehension  this code will be squeeze into 1 line
# num_list = [1,2,3,4,5]
# new_lst_comph = [n + 1 for n in num_list]
# print(new_lst_comph)

#list comprehension dosen't means that you can only work with the list you can also take the string
#example with the sting

# name = "saad"
# new_list = [letter for letter in name]
# print(new_list)

#list comprehension dosen't means that you can only work with the list you can also take the range
#example with the range()
#each item multiple by 2
# new_list = [n*2 for n in range(1,5)]
# print(new_list)

#the new concept of conditional list comprehension
#we're adding the if test/ condition in the list
#that condition test the new_item and able to control it by stopping it or passing it

names = ["ali", "su", "omar", "aitsam", "sarfraz", "waleed", "Abdullah", "Xumei", "Talha",
         "saad"]
#required only short naem with 4 alphabets
short_names = [n for n in names if len(n) < 5]
print(short_names)

#Code Challenge
#you only need to print the name their length is greater then 4
#in addition all the name should be in Upper case
short_names = [n.upper() for n in names if len(n) > 5]
print(short_names)