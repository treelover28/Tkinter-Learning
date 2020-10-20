from tkinter import *

# create root window
root = Tk()
# create a callback function for the button


def click():
    label = Label(root, text="Look! I just clicked a button!!")
    label.pack()


# you can pad a button's size
# like React, if you pass the function() with the parenthesis, it will run right away
# use it without the ()
button = Button(root, text="Click me", padx=50, pady=50,
                # fg = foreground, changes the text color
                # bg = changes the background color
                # you can also use hex color codes
                command=click, fg="white", bg="red")
# you can set button state --greyed out
button2 = Button(root, text="Can't click me :'(", state=DISABLED)

button.pack()
button2.pack()

root.mainloop()
