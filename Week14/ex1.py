# in cmd line
# pip install future
# then restart pycharm

from future.moves import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Gui in Python')
lblHello = tkinter.Label(window, text='Hello World').pack()
window.mainloop()