
'''
this class makes a tkinter Label object that works like a button
intended use is to provide a button widget that
will allow configuring the background and foreground colors
when tkinter is run on MAC M.1 systems
'''

import tkinter as tk

class MButton:
    # -------- start init def --------
    def __init__(self, container, **kw):
        print(container, kw)

        self.command = self.do_nothing
        if "command" in kw:
            self.command = kw['command']

        self.hover_high='gray94'
        
        self.butt_bg = 'gray86'
        if "bg" in kw:
            self.butt_bg = kw['bg']

        self.butt_fg = 'black'
        if "fg" in kw:
            self.butt_fg = kw['fg']
        
        #self.labl_0 = tk.Label(container, bg = 'gray60' )
        #self.labl_0 = tk.Label(container, bg = self.butt_bg)
        
        self.m_butt_txt = "MButton"
        if "text" in kw:
            self.m_butt_txt = kw['text']

        self.bfont = ('', 20)
        if "font" in kw:
            self.bfont = kw['font']

        self.lbl_width = len(self.m_butt_txt) + 1
        if "width" in kw:
            self.lbl_width = kw['width'] 
            
        lbl_width = len(self.m_butt_txt) + 1
        #self.labl_1 = tk.Label(self.labl_0, text=self.m_butt_txt, font = self.bfont, bg=self.butt_bg, width=self.lbl_width)
        self.labl_1 = tk.Label(container, text=self.m_butt_txt, font = self.bfont, bg=self.butt_bg, width=self.lbl_width, relief='raised')
        #self.labl_1 = tk.Label(self.labl_0, text=self.m_butt_txt, font = self.bfont, bg=self.butt_bg, width=self.lbl_width, relief='raised')

        self.labl_1.bind("<Button-1>", self.click_lbl_butt)
        self.labl_1.bind("<ButtonRelease-1>", self.release_lbl_button)
        self.labl_1.bind("<Enter>", self.mac_butt_hover_enter)
        self.labl_1.bind("<Leave>", self.mac_butt_hover_leave)

    # -------- end init def --------

       
    def do_nothing(self):
        pass

    def mpack(self):
        #pass
        #self.labl_1.pack(padx=(0,1), pady=(0,1))
        #self.labl_0.pack(padx=1, pady=1)
        self.labl_1.pack(padx=0, pady=(2,1))
        

    def click_lbl_butt(self, e):
        #print("label button clicked", e)
        #self.labl_0.pack_configure(padx=(2,0), pady=(2,0))
        #self.labl_1.pack_configure(padx=(2,0), pady=(2,0))
        self.labl_1.config(relief='sunken')
        #self.labl_0.config(relief='sunken')
        self.command()

    def release_lbl_button(self, e):
        #self.labl_0.pack_configure(padx=1, pady=1)
        self.labl_1.config(relief='raised')
        #self.labl_0.config(relief='raised')
        

    def mac_butt_hover_enter(self, e):
        #print(e)
        self.labl_1.config(bg=self.hover_high)

    def mac_butt_hover_leave(self, e):
        #print(e)
        self.labl_1.config(bg=self.butt_bg)

    def config(self, **cfgkw):
        if "bg" in cfgkw:
            self.butt_bg = cfgkw['bg']
            self.labl_1.config(bg=self.butt_bg)
            
        if "fg" in cfgkw:
            self.butt_fg = cfgkw['fg']
            self.labl_1.config(fg=self.butt_fg)

        if "text" in cfgkw:
            self.m_butt_txt = cfgkw['text']
            self.labl_1.config(text=self.m_butt_txt)

        if "font" in cfgkw:
            self.bfont = cfgkw['font']
            self.labl_1.config(font=self.bfont)

        if "width" in cfgkw:
            sself.lbl_width = cfgkw['width']
            self.labl_1.config(width=self.lbl_width)


    
    
