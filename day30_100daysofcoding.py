#code Exp1
#filenotfounderror
# with open("any file.txt") as file:
#     file.read()

#code Exp2
#keyerror
#when you typed the value that dosen't exist inside the dictionary you mention
# a_dict = {"key":"value"}
# value = a_dict["saad"]

#code Exp#3
#Indexerror
#when you're trying to access the index which is not available in the list
# cloth_lst = ["jacket", "shirt", "Pent","Suite"]
# cloth = cloth_lst[4]

#code Exp#04
#type Error
#whne you're trying to add the two different data types with changing their data type into one type then the error cause
# text = "abcd"
# print(text + 9)


#example for the the key words (try, except, else, finally)

try:
    #we open this file but actually it dosen't exist
    #this line will cause the error
    file = open("day30_file_exp.txt")
    a_dict={"key":"value"}
    #here again we're trying to access the key which is not a part of the dict
    print(a_dict["saad"])
except FileNotFoundError: #here we just excet the one error of the opening the file
    file = open("day30_file_exp.txt","w")
    file.write("something")
# except KeyError: #using this except will help to deal with the a_dict error
#     print("That key dosen't exist")

    #here we use the error message to tell that whcih key is the actual error
    #there is the one more concept to caught the exception
except KeyError as error_mssage:
    print(f"The key {error_mssage} dose not exist")

#this key is will wrok when the code in the block of try will work and after that
#you want to implement the else block of the code
#what type odf code can be added to the else block
#if the try block open the file then the else will read through the files
else:
     content = file.read()
     print(content)
     #another thing if the file dosen't exist before this line of code
     #the else block will never be trigger or implemented
     #because in the fisrt block "try" you try to make final then you went to the exception
     #and that except will created your file and it jump to the next error
     #and then it went the else to read and print the content
     #now the last key word for today's is finally
     #in this situaion thw fianlly is used to close the file and return a message
finally:
    file.close()
    print("File was closed.")