import tkinter

root = tkinter.Tk()
root.geometry("200x300")


def doButton(textt):
    print(textt)


def showPosEvent(event):
    print ('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def doRightClick(event):
    print ('Got right mouse button click:'), 
    showPosEvent(event)



btn_1 = tkinter.Button(root, width=10, text="button 1", command= lambda: doButton("button is 1"))
btn_2 = tkinter.Button(root, width=10,text="button 2", command= lambda: doButton("button is 2"))
btn_3 = tkinter.Button(root, width=10, text="button 3", command= lambda: doButton("button is 3"))
btn_4 = tkinter.Button(root, width=10, text="button 4", command= lambda: doButton("button is 4"))

btn_1.bind('<Button-3>', doRightClick)
root.bind('<Button-3>', doRightClick)

btn = {}
for x in range(4):
    name = "button"
    btn[x]= tkinter.Button(root, width=10, command=doButton, text=name)

btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=1, column=0)
btn_4.grid(row=1, column=1)





root.mainloop()
