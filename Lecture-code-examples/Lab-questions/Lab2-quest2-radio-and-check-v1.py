 


import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('400x400')

# ------ variables -------
var1 = tk.StringVar()
var1.set("not selected yet")
var2 = tk.StringVar()

tkVar_rad = tk.IntVar()

# ------ functions -------


def update_checkbox_message():
    temp_1 =  str(var1.get())
    temp_2 =  str(var2.get())
    temp_text = temp_1 + " - " + temp_2
    label_1.configure(text = temp_text)


def do_rad_butn():
    temp_var = tkVar_rad.get()
    label_rad_1.configure(text=temp_var)

def do_it_all():
    update_checkbox_message()
    do_rad_butn()
    
# -------- widgets ---------

label_1 = tk.Label(window, bg='white', width=20, text='empty')

chk_button_1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue="blue", offvalue="rock")
chk_button_2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue="happy", offvalue="lost")

button_1 = tk.Button(window, text="do all update", command=do_it_all)

# ---- radio button code -------

 
label_rad_1 = tk.Label(window, text="selection", font=('arial', 20))
 
my_radio_1 = tk.Radiobutton(window)
my_radio_1.config(text="Radiobutton 1", variable=tkVar_rad, value=1)
 
my_radio_2 = tk.Radiobutton(window)
my_radio_2.config(text="Radiobutton 2", variable=tkVar_rad, value=2)
 
my_radio_3 = tk.Radiobutton(window)
my_radio_3.config(text="Radiobutton 3", variable=tkVar_rad, value=3)
 
#button_radio_do = tk.Button(window, text="post radio", command=do_rad_butn)

# --------- layout --------

label_1.pack()
chk_button_1.pack()
chk_button_2.pack()
tk.Label(window, text="-----------------------------------").pack()

label_rad_1.pack()
my_radio_1.pack()
my_radio_2.pack()
my_radio_3.pack()

tk.Label(window, text="-----------------------------------").pack()
button_1.pack()
#button_radio_do.pack()

window.mainloop()


'''
chk_button_1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
chk_button_2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
'''
