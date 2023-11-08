from tkinter import *

class Sample(Tk):
    def __init__(self,*args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)

        self.frames = {}

        for F in (MainPage, OtherPage):
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        Label(self, text="Start Page").pack(pady=10,padx=10)
        Button(self, text="other page?", command=lambda:controller.show_frame(OtherPage)).pack()

class OtherPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="Next Page").pack()
        Button(self, text="back", command=lambda:controller.show_frame(MainPage)).pack()

app = Sample()
app.mainloop()
