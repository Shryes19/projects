from tkinter import *
from tkinter import messagebox
import math

# w = Tk('Registration Form')
# label1 = Label(w,text="Registration form",bg='blue',font="courier 16 bold",fg='white',width=20,height=3).grid(row=0,column=1,columnspan=5)
# label2 = Label(w,text="Name: ",foreground='blue',width=15,height=2).grid(row=1,column=1,sticky=W)
# label3 = Label(w,text="Language known: ",foreground='blue',width=15,height=2).grid(row=2,column=1,sticky=W)
# label4 = Label(w,text="Gender: ",foreground='blue',width=15,height=2).grid(row=3,column=1,sticky=W)
# label5 = Label(w,text="Address: ",foreground='blue',width=15,height=2).grid(row=5,column=1,sticky=W)
# label6 = Label(w,text="Email id: ",foreground='blue',width=15,height=2).grid(row=6,column=1,sticky=W)
# label7 = Label(w,text="Contact no: ",foreground='blue',width=15,height=2).grid(row=7,column=1,sticky=W)
# label8 = Label(w,text="Country: ",foreground='blue',width=15,height=2).grid(row=8,column=1,sticky=W)
# label9 = Label(w,text="State: ",foreground='blue',width=15,height=2).grid(row=9,column=1,sticky=W)
# label10 = Label(w,text="Choose the course: ",foreground='blue',width=15,height=2).grid(row=10,column=1,sticky=W)
#
# v=Entry(w).grid(row=1,column=2)
# v=Entry(w).grid(row=2,column=2)
#
# var=IntVar()
# r1=Radiobutton(w, text= " Male",variable= var, value=1)
# r1.grid(row=3,column=2)
# r2=Radiobutton(w, text= "Female",variable= var, value=2)
# r2.grid(row=4,column=2)
#
#
# # v=Entry(w).grid(row=5,column=2)
# # v=Entry(w).grid(row=6,column=2)
# # v=Entry(w).grid(row=7,column=2)
#
# v=Text(w, height =5,width=15)
# v.insert(INSERT, 'Edit here')
# v.grid(row=5,column=2)
#
# v=Entry(w).grid(row=6,column=2)
#
# v=Entry(w).grid(row=7,column=2)
# v=Entry(w).grid(row=8,column=2)
# v=Entry(w).grid(row=9,column=2)
#
#
#
# c1 = IntVar()
# c2 = IntVar()
# cb1=Checkbutton(w, text = "Python", variable = c1,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=10,column=2)
# cb2=Checkbutton(w, text = "Block chain", variable = c2,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=11,column=2)
#
# def msg():
#     messagebox.showinfo('Registration ','Registration completed')
#
#
# B=Button(w,text="REGISTER HERE", height=1, width=15, bg="blue", fg="White",font="courier 16 bold",command=msg)
# B.grid(row=12,columnspan=3)
#
#
# w.mainloop()



# w = Tk()
# label = Label(w,text='Radius:').grid(row=0,column=1,columnspan=5)
#
# v = Entry(w)
# v.grid(row=1,column=1)
#
# def calc():
#
#     r= float(v.get())
#     a = math.pi * r*r
#     result.config(text=f"Area of Circle: {a}")
#
#
# b=Button(w,text='Calculate Area',command=calc).grid(row=2,column=1,columnspan=5)
#
# result = Label(w,text='')
# result.grid(row=3,column=1,columnspan=5)
#
# w.mainloop()


# from tkinter import *
#
# w = Tk()
#
# cv = Canvas(w,background='yellow').pack()
# frame1 = Frame(w,background='red',width=100,height=90).place(x=10,y=0)
# frame2 = Frame(w,background='blue',width=100,height=200).place(x=100,y=0)
# frame3 = Frame(w,background='white',width=90,height=100).place(x=10,y=100)
#
# w.mainloop()

L=[10,20,30,30,20,90,10,80]

class A:
    def __init__(self,l):
        self.l = l

class B(A):
    def s(self):
        print(set(self.l))

obj = B(L)