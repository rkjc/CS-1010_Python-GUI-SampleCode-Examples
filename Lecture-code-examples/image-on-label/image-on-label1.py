import tkinter as tk
  
groot = tk.Tk()
groot.geometry("400x400")
groot.title("The cat")
  
def doThis1():
    button_1.config(text="cat Button has Landed")
  
#images have to be .png, .jpg does not work.
# img1 = tk.PhotoImage(file="spacesuitmoon.png")
# im1a = img1.subsample(5)
  
cat_image = tk.PhotoImage(file="redcat.png")

cat_image_sm = cat_image.subsample(8)

cat_label = tk.Label(groot, image= cat_image_sm)

cat_label.place(x=0, y=0, relwidth=1, relheight=1)
  
L1 = tk.Label(groot, text = "The Cat")
L1.pack()
  
button_1 = tk.Button(groot, text="Moon Button", command=doThis1)
button_1.pack(side=tk.BOTTOM)
  
groot.mainloop()
