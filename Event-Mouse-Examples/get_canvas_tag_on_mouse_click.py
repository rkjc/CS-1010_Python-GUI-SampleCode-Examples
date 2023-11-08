 
# https://stackoverflow.com/questions/70423920/how-do-i-detect-tags-of-clicked-objects-in-tkinter-canvas

import tkinter


canvas = tkinter.Canvas(width=800, height=400)
canvas.pack()

canvas.create_line(20, 100, 150, 350, tags="lines")
canvas.create_oval(400, 250, 500, 350, fill="blue", tags="ovals")

for j in range(4):
    for i in range(10):
        canvas.create_rectangle(i * 70 + 10, j * 60 + 10, i * 70 + 60, j * 60 + 50, fill="lightblue", tags=f"square_{j}_{i}")

def click(event):

    #currently_clicked = canvas.find_withtag("current")
    #if currently_clicked:
    print(canvas.gettags("current")) # the first index will contain your desired output
   
canvas.bind("<Button-1>", click)
canvas.mainloop()
