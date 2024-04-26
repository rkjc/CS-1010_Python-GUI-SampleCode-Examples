
import tkinter
groot = tkinter.Tk()
groot.geometry("600x600")

'''
https://pythonexamples.org/python-tkinter-label-bold/


list of pangrams for printing from wikipedia:

"The quick brown fox jumps over the lazy dog"
"Glib jocks quiz nymph to vex dwarf." (28 letters)[2]
"Sphinx of black quartz, judge my vow." (29 letters)[4]
"The five boxing wizards jump quickly." (31 letters)[3]
"Pack my box with five dozen liquor jugs." (32 letters)


font attributes that can be mixed and matched:
"italic"
"underline"
"bold"

small list of fonts:
Arial
Helvetica
Times New Roman
Segoe Script
OCR A
Terminal
Georgia
Purisa 
'''

panatxt_a = "The quick brown fox jumps over the lazy dog"
panatxt_b = "Sphinx of black quartz, judge my vow."
panatxt_c = "Glib jocks quiz nymph to vex dwarf."
panatxt_d = "The five boxing wizards jump quickly."
panatxt_e = "Pack my box with five dozen liquor jugs."



label_1 = tkinter.Label(groot, text="different font attributes") 
label_2 = tkinter.Label(groot, font=("Helvetica", 16, "bold"), text="font=('Helvetica', 16, 'bold') font attributes\n" + panatxt_a)
label_3 = tkinter.Label(groot, font=("Arial", 20, "italic"), text="font=('Arial', 20, 'bold') font attributes\n" + panatxt_b)
label_4 = tkinter.Label(groot, font=("OCR A", 8, "underline", "italic"), text="font=('OCR A', 8, 'bold') font attributes\n" + panatxt_c)
label_5 = tkinter.Label(groot, font=("Segoe Script", 18, "bold", "italic"), text="font=('Segoe Script', 18, 'bold') font attributes\n" + panatxt_d)
label_6 = tkinter.Label(groot, font=("Purisa", 12, "bold", "italic", "underline"), text="font=('Purisa', 12, 'bold') font attributes\n" + panatxt_e)


label_1.pack(ipadx=20,ipady=20) 
label_2.pack(ipadx=20,ipady=20)
label_3.pack(ipadx=20,ipady=20)
label_4.pack(ipadx=20,ipady=20)
label_5.pack(ipadx=20,ipady=20)
label_6.pack(ipadx=20,ipady=20) 


groot.mainloop()
