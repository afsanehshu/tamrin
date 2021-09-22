from tkinter import *
import os
win = Tk()
win.geometry("300x300")

def Paint():
    os.system("mspaint")

def Chromet():
    os.system("start Chrome")

def FireFox():
    os.system("start FireFox")

def Notepad():
    os.system("start Notepad")
     

bpaint =Button(win,text="Paint",bg="pink",padx=29,pady=10 ,command=Paint)
bchrome =Button(win,text="Chromet",bg="pink",padx=19,pady=10,command=Chromet)
bfirefox =Button(win,text="FireFox",bg="pink",padx=24,pady=10,command=FireFox)
bnotepad =Button(win,text="Notepad",bg="pink",padx=19.5,pady=10,command=Notepad)

bpaint.grid(row=1,column=2)
bchrome.grid(row=2,column=2)
bfirefox.grid(row=3,column=2)
bnotepad.grid(row=4,column=2)


win.mainloop()
