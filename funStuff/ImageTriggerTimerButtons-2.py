import tkinter

root = tkinter.Tk()
#root.geometry("500x400")
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)

buttonOn3 = False
buttonOn4 = False
buttonOn5 = False

def setImage():
    label_1.config(image=img01)


def restart():
     global counter
     counter = 6
     label_1.config(image="")
     countDown()

def countDown():
    global counter
    counter -= 1
    label_1.config(text=counter)
    if(counter > 0):
        root.after(500, countDown)
    else:
        setImage()


counter = 6

#images have to be .png, .jpg does not work.
img01 = tkinter.PhotoImage(file="Sciencecandoit.png")

img01_size_2 = img01.subsample(2)

label_1 = tkinter.Label(root, text=counter)
label_1.config(font=("Arial", 48) )
label_1.grid(row=1, rowspan=3, column=1)


MyButton1 = tkinter.Button(root, text="Reset", bg="orange", width=5, height=5, command = restart)
MyButton1.grid(row=1, column=0)


countDown()
root.mainloop()
