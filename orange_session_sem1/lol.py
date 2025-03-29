from tkinter import *
w = Tk()
w.title("NONCE candy store")
w.geometry('300x300')
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
c5 = IntVar()
c6 = IntVar()
c7 = IntVar()
c8 = IntVar()
c9 = IntVar()
cb1=Checkbutton(w, text = "Chocolate", variable = c1,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=1,column=0,sticky=W)
cb2=Checkbutton(w, text = "fruity", variable = c2,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=2,column=0,sticky=W)
cb3=Checkbutton(w, text = "caramel", variable = c3,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=3,column=0,sticky=W)
cb4=Checkbutton(w, text = "peanutyalmondy", variable = c4,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=4,column=0,sticky=W)
cb5=Checkbutton(w, text = "nougat", variable = c5,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=5,column=0,sticky=W)
cb6=Checkbutton(w, text = "nougat", variable = c6,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=6,column=0,sticky=W)
cb7=Checkbutton(w, text = "crispedricewafer", variable = c7,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=7,column=0,sticky=W)
cb8=Checkbutton(w, text = "hard", variable = c8,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=8,column=0,sticky=W)
cb9=Checkbutton(w, text = "pluribus", variable = c9,
                 onvalue=1,
                 offvalue=0,
                 height=2,
                 width=10).grid(row=9,column=0,sticky=W)
b1=Button(w,text="Show result",width=1,padx=50,pady=15).grid(row=10,column=1)
b2=Button(w,text="Clear filters",width=1,padx=50,pady=15).grid(row=11,column=1)
import csv

w.mainloop()