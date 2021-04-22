from future.moves import tkinter
from tkinter import *
window = tkinter.Tk()
window.title('Gui in Python')
# set frame and geometry location widthxheight+xpos+ypos
window.geometry('900x500+100+100')

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")


btn1 = tkinter.Button(top_frame, text='Button 1', bg='red', fg='white').pack()
btn2 = tkinter.Button(top_frame, text='Button 2', bg='green', fg='white').pack()
btn3 = tkinter.Button(bottom_frame, text='Button 3', bg='blue', fg='white').pack(side="left")
btn4 = tkinter.Button(bottom_frame, text='Button 4', bg='blue', fg='orange').pack(side="left")

window.mainloop()