import tkinter as tk
    
count=0
mymessage="what?"

app = tk.Tk()

numb1 = 0
numb2 = 0
whichnum=1

labelone = tk.Label(app,  text="input 1")
labeltwo = tk.Label(app,  text="input 2")
labelthree = tk.Label(app,  text="result")

def change_label_number(num):
    global numb1
    global numb2
    global whichnum
    if whichnum == 1:
        numb1=num
        whichnum = 2
        labelone.config(text=str(num))
    else: # whichnum == 2:
        numb2=num
        whichnum = 1    
        labeltwo.config(text=str(num))


def docalculation(mathit):
    global numb1
    global numb2
    output = "none"
    if mathit == "+":
        output = numb1 + numb2
        funout = "+ " + str(numb2)
        labeltwo.config(text=funout)
        labelthree.configure(text=str(output))
    elif mathit =="=":
        print("what")
        
    
    
button1 = tk.Button(app, text="1", width=30, command=lambda: change_label_number(1))

button2 = tk.Button(app, text="2", width=30, command=lambda: change_label_number(2))

button3 = tk.Button(app, text="+", width=30, command=lambda: docalculation("+"))

superbutton = tk.Button(app, text="=", width=30, command=lambda: docalculation("="))


button1.pack()
button2.pack()

button3.pack()
superbutton.pack()

labelone.pack()
labeltwo.pack()
labelthree.pack()


app.mainloop()
