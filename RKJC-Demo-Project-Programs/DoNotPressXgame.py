'''
Free and Open Source under the MIT licence

by Richard kj Cross
2023-11-06
last updated 2023-11-07
'''

import tkinter as tk
import time
import random

groot = tk.Tk()
groot.geometry("600x550") #width, height
groot.config(bg="light grey")

alphbet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']

count = 100  # how many letters it will show
timeout = 1000 # time between letters at the start, this will shorten between each letter shown

space_was_pressed = False
correct = 0
failed = 0
missed = 0
enable_key = False
prev_letter = ''
current_letter = ''
key_up = True

dn_count = 3
def start_count_down():
    global dn_count, enable_key 
    if dn_count > -1:
        letter_label.config(text=dn_count, font=("OCR A", 64))
        dn_count -= 1
        # the function '.after' waits that many millisecs and calls the function name given
        groot.after(400, start_count_down)
    else:
        letter_label.config(text=" ", font=("OCR A", 242))  
        groot.after(400, show_letter)

    
def show_letter():
    global count, timeout, space_was_pressed, enable_key
    global correct, failed, missed
    global current_letter, prev_letter
    
    if count >= 0:
        #current_letter = letter_label.cget("text")
        if space_was_pressed:
            if current_letter == "X":
                failed += 1
            else:
                correct += 1
        else:
            missed +=1
        
        space_was_pressed = False
        groot.config(bg="light grey")

        pre_letter = current_letter
        
        while current_letter == pre_letter: # so letters aren't repeated back-to-back
            maybe_x = random.randint(0,5) # gives it a 1 in 6 chance of being an x
            if maybe_x == 0:
                current_letter = 'X'
            else:
                randum = random.randint(0,24)
                current_letter = alphbet[randum]
                
        letter_label.config(text=current_letter)       
        count -= 1
        timeout -= 3  # *** speeds up *** change this value to the rate is speeds up each letter
        enable_key = True
        groot.after(timeout, show_letter)
        
    else:
        enable_key = False
        groot.config(bg="light grey")
        letter_label.config(text="ツ")
        end_text = "FINISHED! | correct= " +str(correct) + " | pressed X = " + str(failed) + " | missed = " + str(missed)
        bottom_label.config(text=end_text)


def space_key_press(event):
    global space_was_pressed
    global enable_key, key_up
    if enable_key and key_up:
        key_up = False
        space_was_pressed = True
        groot.config(bg="green")

def space_key_release(event):
    global key_up
    key_up = True
    #groot.config(bg="light grey")
    pass



groot.bind("<KeyRelease-space>", space_key_release)
groot.bind("<KeyPress-space>", space_key_press)

letter_label = tk.Label(groot, font=("OCR A", 242), text= "⍨", bg="light grey")
bottom_label = tk.Label(groot, text= "")

letter_label.pack()
bottom_label.pack()

start_count_down()

groot.mainloop() 

