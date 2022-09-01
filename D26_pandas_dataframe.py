import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

#you can loop through the pandas Dataframe IN TH SIMILAR WAY

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#loop  through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)

#pandas inbuild function which loop through rows of a data frame by using the iterrows
for (index, row) in student_data_frame.iterrows():
    print(row)