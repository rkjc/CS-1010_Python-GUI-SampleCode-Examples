# example of file save/open using a text writing program
from tkinter import *
from tkinter import filedialog

groot = Tk()
groot.geometry("500x500")

thefilepath = "new text file.txt"
tempstr = ""


def writeToFile():
    global thefilepath
    myfile = open(thefilepath, "w")
    tempstr2 = myTextBox.get("1.0", END)
    myfile.write(tempstr2)
    myfile.write("\n")
    myfile.close()


def openFile():
    global thefilepath
    global tempstr
    groot.filename = filedialog.askopenfilename(title="Select file")
    thefilepath = groot.filename
    myfile = open(thefilepath, "r")
    textFileContent = myfile.read()
    myfile.close()
    myTextBox.delete("1.0", END)
    myTextBox.insert("insert", textFileContent)


def saveAsFile():
    global thefilepath
    groot.filename = filedialog.asksaveasfilename(title="Select file")
    thefilepath = groot.filename
    myfile = open(thefilepath, "w")
    tempstr2 = myTextBox.get("1.0", END)
    myfile.write(tempstr2)
    myfile.write("\n")
    myfile.close()


butn_1 = Button(groot, text="save", command=writeToFile)
butn_1.pack()

butn_3 = Button(groot, text="save as", command=saveAsFile)
butn_3.pack()

butn_2 = Button(groot, text="Open file", command=openFile)
butn_2.pack()

myTextBox = Text(groot, height=20, width=50)
myTextBox.pack()
myTextBox.insert(END, tempstr)

groot.mainloop()
