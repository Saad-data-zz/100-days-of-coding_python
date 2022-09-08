import tkinter
#it will create the screen
window = tkinter.Tk()
window.title("My first GUI program")
#define the screen size
window.minsize(width=500, height=300)
#how to put thing inside the screen
#using the class Label
my_label = tkinter.Label(text="my first label Saad", font=("arial", 28, "bold"))
#this will not show up the screen untill you call the function called pack()

#calling the function of diplay our text on screen
my_label.pack()
#if you liek to put the new text on the label
my_label["text"] = "New Text"
my_label.config(text="New Text")

#to keep the screen on we'll use
window.mainloop()

