# example of file save/open using a text writing program
from tkinter import *
from tkinter import filedialog

groot = Tk()
groot.geometry("500x500")

myfilepath = "" # holds the name of the file being used
tempstr = ""

def writeToFile():
   global myfilepath
   if (len(myfilepath) == 0):
       saveAsFile()
   else:
       groot.title(myfilepath)
       myfile = open(myfilepath, "w")
       tempstr2 = myTextBox.get("1.0", END)
       myfile.write(tempstr2)
       myfile.write("\n")
       myfile.close()

def openFile():
    global myfilepath
    global tempstr
    myfilepath = filedialog.askopenfilename(title = "Select file")
    groot.title(myfilepath)
    if (len(myfilepath) > 0):
        myfile = open(myfilepath, "r")
        textFileContent = myfile.read()
        myfile.close()
        myTextBox.delete("1.0", END)
        myTextBox.insert("insert", textFileContent)

def saveAsFile():
    global myfilepath
    #groot.filename = filedialog.asksaveasfilename(title = "Select file")
    myfilepath = filedialog.asksaveasfilename(title = "Select file")
    if(len(myfilepath) > 0):
        myfile = open(myfilepath, "w")
        tempstr2 = myTextBox.get("1.0", END)
        myfile.write(tempstr2)
        myfile.write("\n")
        myfile.close()
   
butn_1 = Button(groot, text="save", command = writeToFile)
butn_1.pack()

butn_3 = Button(groot, text="save as", command=saveAsFile)
butn_3.pack()

butn_2 = Button(groot, text="Open file", command=openFile)
butn_2.pack()

myTextBox = Text(groot, height=20, width=50)
myTextBox.pack()
myTextBox.insert(END, tempstr)


groot.mainloop()
