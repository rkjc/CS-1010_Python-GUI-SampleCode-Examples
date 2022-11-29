from tkinter import *
from tkinter import filedialog

groot = Tk()
groot.geometry("500x400")

thefilepath = ""
tempstr = ""

def writeToFile():
   global thefilepath
   myfile = open(thefilepath, "w")
   tempstr2 = txtwin.get("1.0","end-1c")
   myfile.write(tempstr2)
   myfile.write("\n")
   myfile.close()

def openFile():
    global thefilepath
    global tempstr
    
    groot.filename =  filedialog.askopenfilename(title = "Select file")
    thefilepath = groot.filename
    
    myfile = open(thefilepath, "r")
    bob = myfile.read()
    myfile.close()

    txtwin.insert(END, bob)


   
butn_1 = Button(groot, text="save", command = writeToFile)
butn_1.pack()

butn_2 = Button(groot, text="Open file", command=openFile)
butn_2.pack()

txtwin = Text(groot, height=20, width=50)
txtwin.pack()
txtwin.insert(END, tempstr)


groot.mainloop()
