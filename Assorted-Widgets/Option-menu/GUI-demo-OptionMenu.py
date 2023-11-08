# using the OptionMenu widget
from tkinter import *

# Top level window
window = Tk()

window.title("Studyfied.com")
window.geometry('350x200')

# Function to respond to menu change
def showOutput(x):
    global cost
    tempt = optionVar.get()
    if(tempt == "Basic"):
        cost = 10
        outputLabel.config(text="$10" )
    if (tempt == "Premium"):
        cost = 25
        outputLabel.config(text="$25")
    if (tempt == "Deluxe"):
        cost = 65
        outputLabel.config(text="$65")
    if (tempt == "Presidential"):
        cost = 99
        outputLabel.config(text="$99")

# variables
cost = 10

# Option menu variable
optionVar = StringVar()
optionVar.set("Basic")

outputLabel = Label(window, text="$10")
outputLabel.pack()

# Create a option menu
option = OptionMenu(window, optionVar, "Basic", "Premium", "Deluxe", "Presidential", command=showOutput)
option.pack()

window.mainloop()

# modified from source: https://studyfied.com/tutorial/tkinter/optionmenu-widget/
