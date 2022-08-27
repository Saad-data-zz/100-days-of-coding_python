
#simple way of readlines of the csv file
# with open("weather_data.csv") as data_csv:
#     data = data_csv.readlines()
#     print(data)

#python have special library for csv as python deal with data processing
#importing the csv library
# import csv

#open the file
# with open ("weather_data.csv") as data_file:
     #the reader is the function of csv
     # data = csv.reader(data_file)
     # temperature = []
     #my code
     # data = [(int(row['temp'])) for row in csv.DictReader(data_file)]
     # temperature.append(data)
     #print(type(temperature))
     #try the easier way

     # for row in data :
     #     if row[1] != "temp" :
     #         temperature.append(int(row[1]))
     # print(temperature)

# As you see above we just deal with the one row of data and there is alot of code
#what oif we work with alot of data then the program get complicated with the csv
#here we need pandas which is the library of python for data analysis

import pandas
data = pandas.read_csv("weather_data.csv")
#this simple as that to print the data in pandas
#print(data)
#temperature = []
#how to get the hold of the temp row
#print(data["temp"])
#append the temp value's in the temperature list
#temperature.append(data["temp"])
#print(temperature)
#type check in panda

#type(data)
#print(data["temp"])

#use the function of dict to convert the data into the dict
#data_dict = data.to_dict()

#print(data_dict)
#it will return the list
#temp_list = data["temp"].to_list()
#print(temp_list)

#print(temp_list)
#temp_len= len(temp_list)
#final_len = float(temp_len)
#avrg_temp = sum(temp_list)/ final_len
# print(avrg_temp)

#now using pandas to calculate the average
#data_mean = data["temp"].mean()

#how to get the maximum value
#print(data["temp"].max)

#get data from the columns of "weather_data"


#there two wat oif  holding the data/ dataframe
#getting the holds like dictionary like we did it above
#print(data["condition"])

#the other way is the getting hold like the attribute
#here the condition is the attribute
#print(data.condition)


#how to get the data from row
#print(data[data.day == "Monday"])

#How to get hold of row in which contain the temperature value is max
#print(data[data.temp == data.temp.max()])

#challenge
#How to ge the hold of mondays temp
# convert into Celsius to fahrenheit
# temp_mon =
# print(temp_mon)
# row_monday = data[data.day == "Monday"]
#
# #converting the data type to integer
# monday_temp = int(row_monday.temp)
# #print(monday_temp)
# #converting to fahrenheit
# temp_cov_F = monday_temp * 9/5 + 32
# print(f"Monday's temperature in celsius:{monday_temp} and after converting to fahrenheit:{temp_cov_F}")

# How to create the Dataframe from scrach
# generating the data from the python
# here we got some values dictionary
data_dict = {
    "student": ["omar", "su", "max"],
    "score": [90, 98, 99]
}
# Creating the dataframe for the data_dict
data = pandas.DataFrame(data_dict)
print(data)

# Now let's create the CSV file from this data_dict and save it
data.to_csv("data_dict.csv")