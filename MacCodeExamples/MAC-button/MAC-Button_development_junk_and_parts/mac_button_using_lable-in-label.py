import tkinter as tk
import MAC_button

groot = tk.Tk()
groot.geometry("400x300")

hover_high='gray94'
butt_bg = 'gray86'

def click_lbl_butt(e):
    print(e)
    print("label button clicked")
    labl_1.pack_configure(padx=(1,0), pady=(1,0))

def release_lbl_button(e):
    labl_1.pack_configure(padx=(0,1), pady=(0,1))

def mac_butt_hover_enter(e):
    print(e)
    labl_1.config(bg=hover_high)

def mac_butt_hover_leave(e):
    print(e)
    labl_1.config(bg=butt_bg)
    


labl_0 = tk.Label(groot, bg = 'gray60' )
labl_0.pack(padx=1, pady=1)

fk_butt_txt = "fake button"
lbl_width = len(fk_butt_txt) + 1
labl_1 = tk.Label(labl_0, text=fk_butt_txt, font = ('', 20), bg=butt_bg, width=lbl_width)
labl_1.pack(padx=(0,1), pady=(0,1))

labl_1.bind("<Button-1>", click_lbl_butt)
labl_1.bind("<ButtonRelease-1>", release_lbl_button)
labl_1.bind("<Enter>", mac_butt_hover_enter)
labl_1.bind("<Leave>", mac_butt_hover_leave)



button_1 = tk.Button(groot, text='real button 1', font = ('', 20))
button_1.pack()

button_2 = tk.Button(groot, text='real button 2', font = ('', 20))
button_2.pack()



print(labl_1.winfo_x(), labl_1.winfo_y() )





groot.mainloop()
