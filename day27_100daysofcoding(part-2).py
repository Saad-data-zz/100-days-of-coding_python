from tkinter import *
#this * means import everything from the module

window = Tk()
window.title("My first GUI program")
#define the screen size
window.minsize(width=500, height=300)
#how to put thing inside the screen
#using the class Label
my_label = Label(text="my first label Saad", font=("arial", 28, "bold"))
#this will not show up the screen untill you call the function called pack()

#calling the function of diplay our text on screen
my_label.pack()
#if you liek to put the new text on the label
my_label["text"] = "New Text"
my_label.config(text="New Text")

#the function which used for button
def button_clicked():
    print("I got clicked")
    #this line show wahtever you enter from the window of tkinter
    new_text = input.get()
    my_label.config(text=new_text)
#creating the button
button = Button(text="Click here", command=button_clicked)
button.pack()
#now we can see there is the interation

#using the function of Entry
input = Entry(width=20)
input.pack()
print(input.get())

window.mainloop()
