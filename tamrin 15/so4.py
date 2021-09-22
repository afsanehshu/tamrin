from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Calculator")
def CleanJavab(labl):
    labl.config(text="")
    labl.update() 
def Add(labl,text):
    g =labl["text"]
    labl.config(text=g + text)
    labl.update()
def Remove_a_Number(label):
    g = label["text"]
    resualt=""
    if(len(g) > 0):
       for i,j in enumerate(g):
           if i == len(g)-1:
               pass
           else:
               resualt =resualt + j
    label.config(text=resualt)
    label.update()
    jvab = eval(g)
    label.config(text=str(jvab))
    label.update()
def hesab(label): 
    g = label["text"]
    g = g.replace("x","*")
    g = g.replace("÷","/")
    try:
        jvab=evel(g)
        label.config(text=str(jvab))
    except:
        label.config(text="")
        messagebox.showinfo("Error","نامعتبر است")
    label.update()                  
    
javab = Label(win,width=52,bg="gray",text="",borderwidth=10)
btnJam = Button(win,text="+",padx=40,pady=20,command=lambda:Add(javab,"+"))
btnTafrig = Button(win,text="-",padx=40,pady=20,command=lambda:Add(javab,"-"))
btnZarb = Button(win,text="x",padx=41,pady=20,command=lambda:Add(javab,"x"))
btnTagsim = Button(win,text="÷",padx=40,pady=20,command=lambda:Add(javab,"÷"))
btn1 = Button(win,text="1",padx=40,pady=20,command=lambda:Add(javab,"1"))
btn2 = Button(win,text="2",padx=40,pady=20,command=lambda:Add(javab,"2"))
btn3 = Button(win,text="3",padx=40,pady=20,command=lambda:Add(javab,"3"))
btn4 = Button(win,text="4",padx=40,pady=20,command=lambda:Add(javab,"4"))
btn5 = Button(win,text="5",padx=40,pady=20,command=lambda:Add(javab,"5"))
btn6 = Button(win,text="6",padx=40,pady=20,command=lambda:Add(javab,"6"))
btn7 = Button(win,text="7",padx=40,pady=20,command=lambda:Add(javab,"7"))
btn8 = Button(win,text="8",padx=40,pady=20,command=lambda:Add(javab,"8"))
btn9 = Button(win,text="9",padx=40,pady=20,command=lambda:Add(javab,"9"))
btn0 = Button(win,text="0",padx=40,pady=20,command=lambda:Add(javab,"0"))
btnEqual = Button(win,text="=",padx=40,pady=116,command=lambda:hesab(javab))
btnClean = Button(win,text="C",padx=40,pady=20,command=lambda:CleanJavab(javab))
btnRemove = Button(win,text="R",padx=40,pady=20,command=lambda:Remove_a_Number(javab))
btnJam.grid(row=1,column=1)
btnTafrig.grid(row=1,column=2)
btnZarb.grid(row=1,column=3)
btnTagsim.grid(row=1,column=4)
btn1.grid(row=2,column=1)
btn2.grid(row=2,column=2)
btn3.grid(row=2,column=3)
btn4.grid(row=3,column=1)
btn5.grid(row=3,column=2)
btn6.grid(row=3,column=3)
btn7.grid(row=4,column=1)
btn8.grid(row=4,column=2)
btn9.grid(row=4,column=3)
btn0.grid(row=5,columnspan=3,column=1)
btnEqual.grid(row=2,rowspan=4,column=4)
btnClean.grid(row=5,column=1)
btnRemove.grid(row=5,column=3)
javab.grid(row=0,column=0,columnspan=6)

win.mainloop()
