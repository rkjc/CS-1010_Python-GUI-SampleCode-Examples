
import tkinter

groot = tkinter.Tk()
groot.geometry("300x200")

print("about to make variable")

myStoreZ = tkinter.IntVar()
print("after make variable")

myStrVar = tkinter.StringVar()
myStrVar.set("wow cool")

myStoreZ.set(9876)
print("after set variable")

print(myStoreZ.get())

print("after set get()")

zondar = tkinter.Label(groot, text=myStoreZ.get())
lab_2 = tkinter.Label(groot, text=myStrVar.get())

zondar.pack()
lab_2.pack()



groot.mainloop()
