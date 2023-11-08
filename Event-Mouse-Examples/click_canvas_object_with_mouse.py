# https://stackoverflow.com/questions/42175815/python-tkinter-canvas-when-rectangle-clicked


from tkinter import Tk, Canvas

window = Tk()

c = Canvas(window, width=300, height=300)

def clear():
    canvas.delete(ALL)

def clicked(*args):
    print(args)
    print("You clicked play!")

playbutton = c.create_rectangle(75, 25, 225, 75, fill="red",tags="playbutton")
playtext = c.create_text(150, 50, text="Play", font=("Papyrus", 26), fill='blue',tags="playbutton")

c.tag_bind("playbutton","<Button-1>",clicked)

c.pack()

window.mainloop()
