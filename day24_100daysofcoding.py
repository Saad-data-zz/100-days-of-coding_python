#one way to open the file
# file = open("d24_text-file.txt")
# content = file.read()
# print(content)
# file.close()

#another way to open the file without
#And the goood part you don't to write the code to close the file like we did earlier


#absolute file path
#with open("/Users/samy/Desktop/d24_text-file.txt") as file:
#relative file Path
with open("../../Desktop/d24_text-file.txt") as file:
    content = file.read()
    print(content)


# the "w" in th open sytax is the mood in which we're opening the file
# with is the key word to open the file
#in this case when we write the file  thew pervious vcontent or dat in the fiel is vanished
# we can use the append fuction to add the data into the file
#example with the append
# with open("d24_text-file.txt", mode="a") as file:
#     file.write("\nand i'm saaad")


#another feature of the write file is that if youre writing the file it dosen't exist so
#python automatically creates file for you


# with open("d24_newfile.txt", "w") as file:
#     file.write("life comes with good and bad thing we just need to understand")