'''
version 2024-04-26
Using a tkinter Button widget object on Apple Mac computers has
always been a poor experience. In particular configuring colors
attributes usually recuired workarounds. With the introduction of
the Apple M.2 silicon it has gotten worse.
This tkinter helper class uses a tkinter Label widget to simulate the
functions of a button widget.
Its intended use is to provide a button widget that will allow more
asthetic control when running on Mac systems with both
Intel and Apple silicon.
This is a 'close enough' replacement aimed at providing students of
Python Tkinter on Macs more of a cross platform experience.
This is going to have bugs and inconsistancies as I don't have
a Mac computer to test this on. Good Luck.

*see bottom of page for MIT license statement*
'''

# TODO - how to add images to a label/button?

import tkinter as tk

class Button:

    default_bg = 'gray86'
    default_fg = 'black'
    default_highlight = 'gray94'

    # -------- start init def --------
    def __init__(self, container, **kw):

        self.butt_bg = self.default_bg
        self.butt_fg = self.default_fg
        self.hover_high=self.default_highlight

        self.command = self.do_nothing
        if "command" in kw:
            self.command = kw['command']
            del kw['command']

        if "bg" in kw:
            self.butt_bg = kw['bg']

        if "fg" in kw:
            self.butt_fg = kw['fg']
        
        # TODO adjust width to pad the edges like a button does
        # self.lbl_width = 0 #len(self.m_butt_txt) # + 1
        # if "width" in kw:
        #     self.lbl_width = kw['width']
            

        self.labl_1 = tk.Label(container, kw)
        self.labl_1.config(relief='raised')


        self.labl_1.bind("<Button-1>", self.click_lbl_butt)
        self.labl_1.bind("<ButtonRelease-1>", self.release_lbl_button)
        self.labl_1.bind("<Enter>", self.mac_butt_hover_enter)
        self.labl_1.bind("<Leave>", self.mac_butt_hover_leave)

    # -------- end init def --------

       
    def do_nothing(self):
        pass

    def pack(self):
        self.labl_1.pack(padx=0, pady=(2,1))
        

    def click_lbl_butt(self, e):
        self.labl_1.config(relief='sunken')
        self.command()

    def release_lbl_button(self, e):
        self.labl_1.config(bg=self.butt_bg)
        self.labl_1.config(relief='raised')


    def mac_butt_hover_enter(self, e):
        self.labl_1.config(bg=self.hover_high)

    def mac_butt_hover_leave(self, e):
        self.labl_1.config(bg=self.butt_bg)

    def set_width(self, wide):
        pass
        # TODO adjust width to pad the edges like a button does
        # get len of text
        # if "width" in kw:
        #     self.lbl_width = kw['width']
        # self.labl_1.config(width=self.lbl_width)



    def config( **kw):
        if "command" in kw:
            self.command = kw['command']
            del kw['command']

        self.labl_1.config(kw)
        #print("kw bg color", kw['bg'])
        self.butt_bg = kw['bg']

    
'''
Copyright (c) 2024 Richard kj Cross

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

