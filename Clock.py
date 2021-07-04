# Importing modules
from tkinter import *
from tkinter.ttk import *

# Importing strftime function to
# retrieve system's time
from time import strftime
# Creating tkinter window
root = Tk()
root.title('Digital Clock')


# Creating Function to
# display time on the label
def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget
lbl = Label(root, font=('courier', 50, 'bold'), background='#856ff8', foreground='white')

# Placing the clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
