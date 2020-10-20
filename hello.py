from tkinter import *

# create root window
root = Tk()
# define Label widget on top of the Root widget
label = Label(root, text="Hello World")
# now actually shoving it onto the screen using .pack()
label.pack()

root.mainloop()
