

import tkinter
from random import randint
import tkinter.messagebox

top = tkinter.Tk()

def roll_a_dice():
    j = randint(1,6)
    k = randint(1,6)
    tkinter.messagebox.showinfo("dice rolled", (j,k))

B1 = tkinter.Button(top, text = "roll a dice", command = roll_a_dice)
B1.pack()
top.mainloop()







