from future.moves import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = tkinter.Tk()
window.title('Gui in Python')
# set frame and geometry location widthxheight+xpos+ypos
window.geometry('900x500+100+100')

# Label
lblHello = tkinter.Label(window, text='Enter your name: ', font=("Arial", 16))
lblHello.grid(row=0, column=0)

lblOutput = tkinter.Label(window, text='Output:', font=("Arial", 16))
lblOutput.grid(row=1, column=0)


# Textbox
txtEntry = Entry(window, widt=30)
txtEntry.grid(row=0, column=1)


# Action
def clicked():
    res = "Hello " + txtEntry.get()
    lblOutput.configure(text='Output:' + res)
    messagebox.showinfo('Greetings Window', res)


# Combobox
cboLocation = Combobox(window)
cboLocation['values'] = ('Toronto', 'Scarborough', 'North York', 'Etobicoke', 'Cabbage town')
cboLocation.current(0)
cboLocation.grid(row=2, column=0)

# Checkbox
chkSelect = BooleanVar(window)
chkSelect.set(True)
chkObj = Checkbutton(window, text='Select if True', var=chkSelect)
chkObj.grid(row=3, column=0)

# Radio button
rad1 = Radiobutton(window, text='Python', value=1)
rad1.grid(row=4, column=0)
rad2 = Radiobutton(window, text='Java', value=2)
rad2.grid(row=4, column=1)
rad3 = Radiobutton(window, text='C#', value=3)
rad3.grid(row=4, column=2)

# Button
btnClick = tkinter.Button(window, text='Submit', bg='blue', fg='white', command=clicked)
btnClick.grid(row=6, column=0)

# Spinbox
spnNumber = tkinter.Spinbox(window, from_=0, to=100, width=20)
spnNumber.grid(row=5, column=0)




window.mainloop()