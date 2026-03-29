from tkinter import *

root = Tk()

def IClicked():
    buttonClickLabel=Label(root, text="You Clicked The Button!")
    buttonClickLabel.pack()

    root.after(2000, buttonClickLabel.destroy)

disableButton=Button(root, text="Don't Click Me!", state=DISABLED)
disableButton.pack()

activeButton=Button(root, text="Click Me!", padx=50, pady=50, command=IClicked, fg="red")
activeButton.pack()

root.mainloop()