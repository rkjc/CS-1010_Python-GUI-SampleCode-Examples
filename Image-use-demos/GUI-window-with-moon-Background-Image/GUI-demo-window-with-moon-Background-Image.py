import tkinter as tk

groot = tk.Tk()
groot.geometry("400x400")
groot.title("The Moon")

#images have to be .png, .jpg does not work.
# img1 = tk.PhotoImage(file="spacesuitmoon.png")
# im1a = img1.subsample(5)

full_image=tk.PhotoImage(file="spacesuitmoon.png")
my_background_image = full_image.subsample(5)
my_background_label = tk.Label(groot, image=my_background_image)
my_background_label.place(x=0, y=0, relwidth=1, relheight=1)

L1 = tk.Label(groot, text = "The Moon")
L1.pack()

groot.mainloop()
