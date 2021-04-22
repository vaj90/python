from future.moves import tkinter
from tkinter import *
window = tkinter.Tk()
window.title('Gui in Python')
# set frame and geometry location widthxheight+xpos+ypos
window.geometry('900x500+100+100')

tkinter.Label(window, text="Username").grid(row=0)
tkinter.Entry(window, width=30).grid(row=0, column=1)
tkinter.Label(window, text="Password").grid(row=1)
tkinter.Entry(window, width=30).grid(row=1, column=1)
tkinter.Button(window, text='login', bg='red', fg='white').grid(columnspan=2, row=2)
window.mainloop()