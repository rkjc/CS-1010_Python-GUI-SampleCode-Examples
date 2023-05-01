 
import tkinter as tk
  
groot = tk.Tk()
groot.geometry("400x400")
groot.title("The cat")
  
def doThis1():
    button_1.config(text="cat Button has Landed")
  
# --------- make a bunch of buttons  ------

w, h = 5, 5
labels = [[0 for x in range(w)] for y in range(h)]

for colz in range(5):
    for rowz in range(5):
        the_text = str(colz) + ' ' + str(rowz)
        labels[colz][rowz] = tk.Label(groot, text=the_text, width=7, height=3)
        labels[colz][rowz].grid(row=rowz, column=colz, sticky=(tk.NSEW))


##cat_image = tk.PhotoImage(file="redcat.png")
##
##cat_image_sm = cat_image.subsample(8)
##
##cat_label = tk.Label(groot, image= cat_image_sm)
##
##cat_label.place(x=0, y=0, relwidth=1, relheight=1)
##  
##L1 = tk.Label(groot, text = "The Cat")
##L1.grid(row=3, column=3, sticky=(tk.NSEW))
  
##button_1 = tk.Button(groot, text="Moon Button", command=doThis1)
##button_1.pack(side=tk.BOTTOM)
  
groot.mainloop()


# got code from:
# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
