 
import tkinter as tk
 
window_main = tk.Tk(className='Tkinter - TutorialKart')
window_main.minsize(300,250)
 
listbox_1 = tk.Listbox(window_main, selectmode=tk.SINGLE,  height="6")
listbox_1.insert(0, 'Apple')
listbox_1.insert(0, 'Banana')
listbox_1.insert(0, 'Cherry')
listbox_1.insert(0, 'rock')
listbox_1.insert(0, 'Mango')
listbox_1.insert(0, 'Orange')
listbox_1.pack()
listbox_1.select_set(0)
 
def submitFunction():
    selection_index_number = listbox_1.curselection()
    temp_text = 'selection index= ' + str(selection_index_number[0]) + " \n selected item= " + listbox_1.get(selection_index_number)
    L1.configure(text=temp_text)
 
 
B1 = tk.Button(window_main, text='Submit', command=submitFunction)
B1.pack()
 
L1 = tk.Label(window_main, text='your selection')
L1.pack()
 
window_main.mainloop() 
