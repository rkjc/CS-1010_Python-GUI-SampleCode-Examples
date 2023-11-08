import tkinter

root = tkinter.Tk()
root.geometry("200x300")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes('-fullscreen', True)

def doButton():
    print("you have been hacked")
    label_img.config(image= img3)
    entry_1.place_forget()

print("width= ", w, " height= ", h)


img1 = tkinter.PhotoImage(file = "FirefoxFrontpage.png")
img1a = img1.subsample(2)

img2 = tkinter.PhotoImage(file = "arrow.png")

img3 = tkinter.PhotoImage(file = "FirefoxFrontpageHack.png")

label_img = tkinter.Label(root, image=img1)
label_img.place(relx=.5, rely=.5, anchor="center", relwidth=1, relheight=1)

#label_1 = tkinter.Label(root, text="empty", width=100)
#label_1.place(relx=.5, rely=.5, anchor="center")

entry_1 = tkinter.Entry(root, width=80)
entry_1.place(relx=.53, rely=.5, anchor="center")

button_1 = tkinter.Button(root, width=40, command=doButton, image=img2)
button_1.place(relx=.72, rely=.5, anchor="center")



root.mainloop()
