from tkinter import *

# create root window
root = Tk()

# Entry widget for input box
entry = Entry(root, width=50, bg="salmon", fg="white", borderwidth=10)
# you can also insert a Default Text, since there is only 1 box, use index 0
entry.insert(0, "Enter your name")
entry.pack()


# create a callback function for the button
def click():
    # get information from the entry box by entry_box.get()
    label = Label(root, text="Hello {}".format(entry.get()))
    label.pack()


# you can pad a button's size
# like React, if you pass the function() with the parenthesis, it will run right away
# use it without the ()
button = Button(root, text="Enter Your Name", padx=50, pady=50,
                # fg = foreground, changes the text color
                # bg = changes the background color
                # you can also use hex color codes
                command=click, fg="white", bg="red")
# you can set button state --greyed out
button2 = Button(root, text="Can't click me :'(", state=DISABLED)

button.pack()
button2.pack()

root.mainloop()
