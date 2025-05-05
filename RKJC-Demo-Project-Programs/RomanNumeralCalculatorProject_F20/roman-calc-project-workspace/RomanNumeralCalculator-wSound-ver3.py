# built using roman numeral converter function code from this site:
# see bottom of file for code sources

import tkinter as tk
from pygame import mixer


mainwindow = tk.Tk()
mainwindow.geometry("500x550")
mainwindow.title("ROMAN NUMERAL CALCULATOR")
mainwindow.config(pady=20)

# ===== Variables and resource imports ============
mixer.init()

cash_sound=mixer.Sound("Various-06.wav")
click_sound=mixer.Sound("button-click-sound-effect-short.wav")

mixer.Sound.play(cash_sound)


full_image=tk.PhotoImage(file="Italy-512.png")
my_background_label = tk.Label(mainwindow, image=full_image)
my_background_label.place(x=0, y=0, relwidth=1, relheight=1)

inputBox = 1
inbox1string = ''
inbox2string = ''
answerboxstring = ''

#infectus -> broken

# ===========================================================
def int_to_roman(input_val):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input_val, type(1)):
        # raise TypeError, "expected integer, got %s" % type(input)
        print("expected integer")
    if not 0 < input_val < 4000:
        # raise ValueError, "Argument must be between 1 and 3999"
        print("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input_val / ints[i])
        result.append(nums[i] * count)
        input_val -= ints[i] * count
    return ''.join(result)

def roman_to_int(input_val):
    """ Convert a Roman numeral to an integer."""
    if not isinstance(input_val, type("")):
        #raise TypeError, "expected string, got %s" % type(input)
        print("TypeError, expected string")
    input_val = input_val.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input_val)):
        try:
            value = nums[input_val[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input_val) and nums[input_val[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            # raise ValueError, 'input is not a valid Roman numeral: %s' % input
            print("input is not a valid Roman numeral - 54")
    # easiest test for validity...
    if int_to_roman(sum) == input_val:
        return sum
    else:
        # raise ValueError, 'input is not a valid Roman numeral: %s' % input
        print("input is not a valid Roman numeral - 60")
        return "input is not a valid Roman numeral"


# ===========================================================
def clear():
    global inbox1string, inbox2string, answerboxstring, inputBox
    inbox1string = ''
    inbox2string = ''
    answerboxstring = ''
    inputBox = 1
    inBox1.config(text=inbox1string, bg="gray95")
    inBox2.config(text=inbox2string, bg="gray95")
    L_answer.config(text=answerboxstring, bg="gray95")

def changeInbox_1():
    global inputBox
    inputBox = 1
    inBox1.config(borderwidth=3)
    inBox2.config(borderwidth=1)

def changeInbox_2():
    global inputBox
    inputBox = 2
    inBox2.config(borderwidth=3)
    inBox1.config(borderwidth=1)

def add_to_inbox(val):
    global inbox1string, inbox2string, inputBox
    if inputBox == 1:
        inbox1string = inbox1string + val
        inBox1.config(text=inbox1string)
    else:
        inbox2string = inbox2string + val
        inBox2.config(text=inbox2string)

def B_I_push():
    add_to_inbox('I')
    mixer.Sound.play(click_sound)

def B_V_push():
    add_to_inbox('V')
    mixer.Sound.play(click_sound)

def B_X_push():
    add_to_inbox('X')
    mixer.Sound.play(click_sound)

def B_L_push():
    add_to_inbox('L')
    mixer.Sound.play(click_sound)

def B_C_push():
    add_to_inbox('C')
    mixer.Sound.play(click_sound)

def B_D_push():
    add_to_inbox('D')
    mixer.Sound.play(click_sound)

def B_M_push():
    add_to_inbox('M')
    mixer.Sound.play(click_sound)

def addRN():
    global inbox1string, inbox2string, answerboxstring
    num1 = roman_to_int(inbox1string)
    if type(num1) == type(""):
        inBox1.config(text='infectus', bg='red')
        num1 = 0
    num2 = roman_to_int(inbox2string)
    if type(num2) == type(""):
        inBox2.config(text='infectus', bg='red')
        num2 = 0
    sum = num1 + num2
    answerboxstring = int_to_roman(sum)
    L_answer.config(text=answerboxstring)
    mixer.Sound.play(click_sound)

def subtractRN():
    global inbox1string, inbox2string, answerboxstring
    num1 = roman_to_int(inbox1string)
    num2 = roman_to_int(inbox2string)
    sum = num1 - num2
    answerboxstring = int_to_roman(sum)
    L_answer.config(text=answerboxstring)
    mixer.Sound.play(click_sound)

def multiplyRN():
    global inbox1string, inbox2string, answerboxstring
    num1 = roman_to_int(inbox1string)
    num2 = roman_to_int(inbox2string)
    sum = num1 * num2
    answerboxstring = int_to_roman(sum)
    L_answer.config(text=answerboxstring)
    mixer.Sound.play(click_sound)

def divideRN():
    global inbox1string, inbox2string, answerboxstring
    num1 = roman_to_int(inbox1string)
    num2 = roman_to_int(inbox2string)
    sum = num1 / num2
    answerboxstring = int_to_roman(sum)
    L_answer.config(text=answerboxstring)
    mixer.Sound.play(click_sound)

def stringPop(str):
    if len(str) > 0:
        str = str[:(len(str) - 1)]
    return str

def delRN():
    global inbox1string, inbox2string, inputBox
    if inputBox == 1:
        inbox1string = stringPop(inbox1string)
        inBox1.config(text=inbox1string, bg="gray95")
    else:
        inbox2string = stringPop(inbox2string)
        inBox2.config(text=inbox2string, bg="gray95")
    mixer.Sound.play(click_sound)


# ======================
Frm1 = tk.Frame(mainwindow)
Frm2 = tk.Frame(mainwindow)
Frm3 = tk.Frame(mainwindow)
Frm4 = tk.Frame(mainwindow)
Frm5 = tk.Frame(mainwindow)

dispFrame1 = tk.LabelFrame(Frm3, text='Initus est numerus uno', font=("",16))
dispFrame2 = tk.LabelFrame(Frm3, text='Initus est numerus duo', font=("",16))
dispFrame3 = tk.LabelFrame(Frm3, text = 'Responsum', font=("",16))

#L1_inBox1 = tk.Label(Frm3, text = '', relief='sunken', width=34, height=2)
L2 = tk.Label(Frm3, text='Initus est numerus uno', font=("",16))
#L3_inBox2 = tk.Label(Frm3, text = '', relief='sunken', width=34, height=2)
L4 = tk.Label(Frm3, text='Initus est numerus duo', font=("",16))
L_answer = tk.Label(dispFrame3, text = '', relief='sunken', width=40, height=2, font=("",16))
#L6 = tk.Label(Frm3, text = 'Responsum')
inBox1 = tk.Button(dispFrame1,  command=changeInbox_1, relief='sunken', width=34, height=1 , font=("",16))
inBox2 = tk.Button(dispFrame2,  command=changeInbox_2, relief='sunken', width=34, height=1, font=("",16))

B_I = tk.Button(Frm1, text = 'I', command=B_I_push, font=("",16))
B_V = tk.Button(Frm1, text = 'V', command=B_V_push, font=("",16))
B_X = tk.Button(Frm1, text = 'X', command=B_X_push, font=("",16))
B_L = tk.Button(Frm1, text = 'L', command=B_L_push, font=("",16))
B_C = tk.Button(Frm1, text = 'C', command=B_C_push, font=("",16))
B_D = tk.Button(Frm1, text = 'D', command=B_D_push, font=("",16))
B_M = tk.Button(Frm1, text = 'M', command=B_M_push, font=("",16))
B_plus = tk.Button(Frm1, text = '+', command=addRN, font=("",16))
B_minus = tk.Button(Frm1, text = '-', command=subtractRN, font=("",16))
B_times = tk.Button(Frm1, text = '*', command=multiplyRN, font=("",16))
B_divide = tk.Button(Frm1, text = '/', command=divideRN, font=("",16))
del_button = tk.Button(Frm1, text=" delere", command=delRN, font=("",16))
clear = tk.Button(Frm1, text="a  c\nu  u\nf  n\ne  c\nr  t\no  u\n   s", width=2, height=6, command=clear, font=("",16))
#  C\nL\nE\nA\nR
# ======================================
inBox1.config(borderwidth=3)
Frm3.pack(side=tk.TOP)

inBox1.pack()
# inBox1.grid(column=1, row=0)
dispFrame1.grid(column=1, row=0)
#L2.grid(column=1, row=1)

inBox2.pack()
# inBox2.grid(column=1, row=3)
#L4.grid(column=1, row=4)
dispFrame2.grid(column=1, row=4)

L_answer.pack()
#L_answer.grid(column=0, row=5, columnspan=2)
# L6.grid(column=1, row=6)
dispFrame3.grid(column=1, row=6)

Frm1.pack(side=tk.BOTTOM)
B_I.grid(row=0, column=1)
B_V.grid(row=0, column=2)
B_X.grid(row=1, column=1)
B_L.grid(row=1, column=2)
B_C.grid(row=2, column=1)
B_D.grid(row=2, column=2)
B_M.grid(row=3, column=1, columnspan=2)
B_plus.grid(row=0, column=4)
B_minus.grid(row=1, column=4)
B_times.grid(row=2, column=4)
B_divide.grid(row=3, column=4)
del_button.grid(row=3, column=0)
clear.grid(row=0, column=0, rowspan=3)

tk.Label(Frm1, width=2).grid(row=0, column=3)



mainwindow.mainloop()

# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html


