
from tkinter import *

import subprocess as sub

win = Tk()
win.geometry("200x50")
win.resizable(0,0)

def ipconfig():
    
        cmd=sub.check_output("Ipconfig /all",shell=True).decode()
        print(cmd)

button1 = Button(win,text="ipconfig",command=ipconfig,bg="yellow")
button1.grid()

win.mainloop()




"""
#روش دوم
from tkinter import *
import os

win = Tk()
win.geometry("200x50")
win.resizable(0,0)

def ipconfig():
    a=os.system("Ipconfig /all")
    print(a)

button1 = Button(win,text="ipconfig",command=ipconfig,bg="yellow")
button1.grid()

win.mainloop()
"""
