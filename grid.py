from tkinter import *

# create root window
root = Tk()
# define Label widget on top of the Root widget
label = Label(root, text="Hello World")
label2 = Label(root, text="My name is Khai Lai")
label3 = Label(root, text="---------------")

# instead of automating the placement using .pack()
# we can specify the position using tkinter's GRID system
# one will be on top while the other is in the bottom.
label.grid(row=0, column=0)
# the grid system is relative
# since there is nothing in column 2,3,4
# it just ignore our placement in column 5,
# place it in 2 instead
label2.grid(row=1, column=5)
label3.grid(row=0, column=1)

root.mainloop()
