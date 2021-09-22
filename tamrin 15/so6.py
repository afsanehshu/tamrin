from tkinter import *
import socket
win=Tk()
win.geometry("300x300")
win.configure(background="Dark Blue")


    
def scan():
    try:
        s.connect((ip,int(port)))

        print("open port")
        print()
        print("_______________________")

    except:

        print("close port")
        print()
        print("_______________________")

l=Label(win, text="enter ip :" ,bg="gray")
l.grid(row=0,column=0)
l3=Label(win, text="enter port:")
l3.grid(row=1,column=0)

n = StringVar()
e = Entry(win, width=32, textvariable=n)
e.grid(row=0,column=1)
k=StringVar()
b = Entry(win, width=32, textvariable=k)
b.grid(row=1,column=1)
x = Button(win, text="Ckeck",bg="orange",command=scan)
x.grid()

l2 = Label(win, text="",fg="green",bg="black")
l2.grid()


win.mainloop()
