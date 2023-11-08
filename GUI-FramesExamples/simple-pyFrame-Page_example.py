# here are some references to explore:
# https://pythonprogramming.net/change-show-new-frame-tkinter/
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/
# https://www.tutorialspoint.com/python/tk_frame.htm
# https://effbot.org/tkinterbook/frame.htm


import tkinter

root = tkinter.Tk()

homePage = tkinter.Frame(root, bg="blue", height=300, width=200)
homePage.grid_propagate(False) #lock the home page and others are limited to this size
homePage.grid(row=0, column=0, sticky="nsew")
#if you fill any page with widgets that make it larger than this,
#that will set the new size for all pages


#add as many pages as you need
pageOne = tkinter.Frame(root, bg="green")
pageOne.grid(row=0, column=0, sticky="nsew")
pageTwo = tkinter.Frame(root, bg="orange")
pageTwo.grid(row=0, column=0, sticky="nsew")

homePage.tkraise() #brings the homepage to the top to start with (or which ever page you choose)

def showHome():
    homePage.tkraise()

def showPageOne():
    pageOne.tkraise()


def showPageTwo():
    pageTwo.tkraise()

    
#Each page Frame has to be setup using grid() layouts

#putting the widgets on and arranging the home page
goToTwo = tkinter.Button(homePage, text="go to pg two", fg="red", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")

goToOne = tkinter.Button(homePage, text="go to pg one", fg="red", command=showPageOne)
goToOne.grid(row=0, column=0, sticky="nsew")



#putting the widgets on and arranging pageOne
goHome = tkinter.Button(pageOne, text="go to home", fg="brown", command=showHome)
goHome.grid(row=0, column=0, sticky="nsew")



#putting the widgets on and arranging pageTwo
label1 = tkinter.Label(pageTwo, text="i am label one")
label1.grid(row=0, column=0)

goHome = tkinter.Button(pageTwo, text="go to home", fg="brown", width=10, command=showHome)
goHome.grid(row=1, column=0)


root.mainloop()




