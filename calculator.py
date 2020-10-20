from tkinter import *

# create root window
root = Tk()
root.title("Simple Calculator by Khai Lai")


# Entry widget for input box
entry = Entry(root, width=35, borderwidth=5)
# have it span 3 columns
entry.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

# Global variables
OPERAND_A = None
OPERAND_B = None
OPERATION = None


def button_click(number):
    # insert number at the end
    entry.insert(END, number)


def button_clear():
    entry.delete(0, END)


def read_operand_A():
    global OPERAND_A
    OPERAND_A = float(entry.get())


def read_operand_B():
    global OPERAND_B
    OPERAND_B = float(entry.get())


def button_addition():
    read_operand_A()

    global OPERATION
    OPERATION = "ADD"
    # delete entry
    entry.delete(0, END)


def button_subtraction():
    read_operand_A()
    global OPERATION
    OPERATION = "MINUS"
    # delete entry
    entry.delete(0, END)


def button_multiplication():
    read_operand_A()
    global OPERATION
    OPERATION = "MULTIPLY"
    # delete entry
    entry.delete(0, END)


def button_division():
    read_operand_A()
    global OPERATION
    OPERATION = "DIVIDE"
    # delete entry
    entry.delete(0, END)


def button_equals():
    # read in operand B
    read_operand_B()
    # clear space for result
    entry.delete(0, END)
    if (OPERATION == "ADD"):
        entry.insert(0, OPERAND_A + OPERAND_B)
    elif (OPERATION == "MINUS"):
        entry.insert(0, OPERAND_A - OPERAND_B)
    elif (OPERATION == "MULTIPLY"):
        entry.insert(0, OPERAND_A * OPERAND_B)
    else:
        if OPERAND_B != 0:
            entry.insert(0, OPERAND_A / OPERAND_B)
        else:
            # use property that float("inf") is a valid number
            entry.insert(0, "inf")


# Define numeric buttons
button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: button_click(0))

# Define Operations Buttons
button_add = Button(root, text="+", padx=40,
                    pady=20, command=button_addition)
button_minus = Button(root, text="-", padx=40,
                      pady=20, command=button_subtraction)
button_multiply = Button(root, text="X", padx=40,
                         pady=20, command=button_multiplication)
button_divide = Button(root, text="/", padx=40,
                       pady=20, command=button_division)

button_equal = Button(root, text="=", padx=90, pady=20,
                      command=button_equals)
button_clear = Button(root, text="CLEAR", padx=79, pady=20,
                      command=button_clear)

# Put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_minus.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

# Runs calculator
root.mainloop()
