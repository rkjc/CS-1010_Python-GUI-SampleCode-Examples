 
 
from tkinter import *
from tkinter import filedialog
import time




groot = Tk()
groot.geometry("500x400")

thefilepath = ""
tempstr = ""

def writeToFile():
   global thefilepath
   if thefilepath == "":
       mycurrenttime = time.strftime("%Y_%m_%d_%H-%M-%S")
       thefilepath = "textJournal_" + mycurrenttime + ".txt"
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


butn_2 = Button(groot, text="Open file", command=openFile)
butn_2.grid(column=0, row=0)

txtwin = Text(groot, height=20, width=50)

txtwin.grid(row=1, column=0, columnspan=2)
txtwin.insert(END, tempstr)

butn_1.grid(column=1, row=0)

groot.mainloop()
