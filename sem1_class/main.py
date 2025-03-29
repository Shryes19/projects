def maxNum():
    l = []
    for i in range(3):
        n = int(input("Enter the num: "))
        l.append(n)
    print(f"Max: {max(l)}\n\n")


def sumNum(l):
    print(f"Sum: {sum(l)}\n\n")


def multiplyNum():
    m = 1
    l = [1, 2, 3]
    for i in l:
        m *= i
    print(f"Multiplication: {m}\n\n")


def reverse():
    s = input("Enter a string: \n")
    print(f"Reversed string: \n{s[::-1]}\n\n")


def remove_duplicate():
    l = [1, 2, 3, 2, 1]
    s = set(l)
    print(list(s), "\n")


def length_list():
    l = []
    print("List empty" if len(l) == 0 else "List not empty", "\n")


def common_element():
    l1 = [1, 2, 3]
    l2 = [10, 2]
    print(True if set(l1).intersection(set(l2)) else False, "\n")


def pop_elements():
    l = [1, 2, 3, 4, 5, 6, 7]
    l.pop(0)
    l.pop(3)
    l.pop(3)
    print(l)


#WAP that accepts a string and counts the number of upper and lowercase
def string_case(s):  #HeLLo
    u_c = 0
    l_c = 0
    for i in s:
        if i.islower():
            l_c += 1
        else:
            u_c += 1
    print(f"UpperCase: {u_c}\nLowerCase: {l_c}\n")


#WAP that takes a list and returns a new list with distinct elements from the 1st list
def distinct_list(l):
    print(f"Distinct list: {list(set(l))}\n")


#WAP to create n print a list were values are squares of number between 1 and 30
def sq():
    l = []
    for i in range(1, 31):
        l.append(i * i)
    print(l, "\n")


def sort_words():
    s = "green-red-yellow-black"
    n_s = ""
    l = []
    l = s.split("-")
    slist = sorted(l)
    for i in slist:
        n_s = n_s + i + "-"
    print(n_s.removesuffix("-"))


def pana():
    s = input("Enter a string").lower()
    letter = "abcdeighijklmnopqrstuvwxyz"
    # c=0
    # for i in s:
    #     if i in letter:
    #         c+=1
    #     else:
    #         pass--
    # if c>=len(letter):
    #     print("true")
    is_pana = True
    for i in letter:
        if i not in s:
            is_pana = False
            break
    if is_pana:
        print("panagram")


def sort_string():
    s = 'google.com'
    d = {}
    for i in s:
        d[i] = s.count(i)
    print(d, '\n')


def st_1st_2nd():
    s = input("Enter string: ")
    if len(s) < 2:
        print("Empty string", '\n')
    else:
        print(f"{s[0:2] + s[len(s) - 2:]}", '\n')


def st_replace_ch():
    s = input("Enter string: ")
    a = s[0]
    s = s[1:]
    s = s.replace(a, "$")
    print(f"{a + s}\n")


def st_replace():
    s1 = 'abc'
    s2 = 'xyz'
    x1 = s1[:2]
    x2 = s2[:2]
    print(f"{s1.replace(x1, x2)}\n{s2.replace(x2, x1)}\n")


def add_ing():
    s = input('Enter: ')
    if len(s) >= 3:
        if s.endswith('ing'):
            s+="ly"
        else:
            s += "ing"
        print(s)
    else:
        pass


# maxNum()
# sumNum([1, 2, 3, 4])
# multiplyNum()
# reverse()
# remove_duplicate()
# length_list()
# common_element()
# pop_elements()
# string_case("HeLLo")
# distinct_list([1,1,1,2,2,3])
# sq()
# sort_words()
# pana()
# sort_string()
# st_1st_2nd()
# st_replace_ch()
# st_replace()
# add_ing()

# def fac(n):
#     print(n)
#     if n==0:
#         r=1
#     else:
#         r = n*fac(n-1)
#         #print(n)
#     return r
#
# print(fac(3))
#
# def tower_of_hanoi(n, source, auxiliary, target):
#
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#
#     tower_of_hanoi(n - 1, source, target, auxiliary)
#
#     print(f"Move disk {n} from {source} to {target}")
#
#     tower_of_hanoi(n - 1, auxiliary, source, target)
#
#
# num_disks = 3
#
# tower_of_hanoi(num_disks, 'A', 'B', 'C')


# def generator_func():
#     yield 10
#     yield 20
# print(generator_func())


# from tkinter import *
# from tkinter import messagebox
#
# win=Tk()
# win.title('ToDo App')
# win.geometry('1908x1080')
# win.configure(background='green')
# l=Label(win,text='Enter Your Task',bg='green')
# l.pack()
# def click_submit():
#     messagebox.askyesno('MESSAGE','Do you want to submit?')
# submit=Button(win,text="Submit",bg='red',command=click_submit)
# text1=Entry(win,width='100')
# text1.pack()
# submit.pack()
# text2=Text(win,width='50')
# text2.pack()
# def click_delete():
#     messagebox.showinfo('MESSAGE','Task number deleted!')
# del_button=Button(win,text='Delete Task Number',command=click_delete,bg='blue')
# del_button.pack()
# text3=Entry(win,width='5')
# text3.pack()
# def click_delete_1():
#     messagebox.showinfo('MESSAGE',text='Deleted!')
# del_button_1=Button(win,text='Delete',bg='red',command=click_delete_1)
# del_button_1.pack()
# win.mainloop()

# from tkinter import *
# from tkinter import messagebox
#
#
# win=Tk()
# win.title('Food Order App')
# win.geometry('1000x1000')
#
# l1=Label(win,text='Food Order Form',font=28)
# l2=Label(win,text='What do you want to order?')
# l3=Label(win,text='How do you want to pay?')
# cv1=IntVar();cv2=IntVar();cv3=IntVar();cv4=IntVar()
# cb1=Checkbutton(win,text='Sandwich',variable=cv1,onvalue=1,offvalue=0)
# cb2=Checkbutton(win,text='Soup',variable=cv2,onvalue=1,offvalue=0)
# cb3=Checkbutton(win,text='Salad',variable=cv3,onvalue=1,offvalue=0)
# cb4=Checkbutton(win,text='Pizza',variable=cv4,onvalue=1,offvalue=0)
# r=IntVar()
# rb1=Radiobutton(win,text='CreditCard',variable=r)
# rb2=Radiobutton(win,text='Paypal',variable=r)
# rb3=Radiobutton(win,text='Other',variable=r)
# next_button=Button(win,text='Next')
#
# l1.pack()
# l2.place(x=10,y=50)
# cb1.place(x=10,y=100)
# cb2.place(x=10,y=150)
# cb3.place(x=10,y=200)
# cb4.place(x=10,y=250)
# l3.place(x=10,y=300)
# rb1.place(x=10,y=350)
# rb2.place(x=10,y=400)
# rb3.place(x=10,y=450)
# next_button.place(x=500,y=700)
#
# win.mainloop()


# from tkinter import *
#
# win=Tk()
# win.geometry('800x800')
# win.title('tk')
# canvas=Canvas(win,bg='blue',width='500',height='300')
# coord=(10,10,300,300)
# arc=canvas.create_arc(coord,start=0,extent=160,fill='red')
# canvas.pack()
# win.mainloop()


# from tkinter import *
# from tkinter import messagebox
# 
# w=Tk()
# w.title('MARKSHEET')
# 
# l = Label(text='Name: ').grid(row=0,column=1)
# e = Entry(w).grid(row=0,column=2)
# l = Label(text='Roll.No: ').grid(row=1,column=1)
# e = Entry(w).grid(row=1,column=2)
# 
# l = Label(text='Sl.No ').grid(row=2,column=1)
# l = Label(text='1 ').grid(row=3,column=1)
# l = Label(text='2 ').grid(row=4,column=1)
# l = Label(text='3 ').grid(row=5,column=1)
# l = Label(text='4 ').grid(row=6,column=1)
# 
# l = Label(text='Subject ').grid(row=2,column=2)
# l = Label(text='CS 201 ').grid(row=3,column=2)
# l = Label(text='CS 202 ').grid(row=4,column=2)
# l = Label(text='MA 201 ').grid(row=5,column=2)
# l = Label(text='EC 201 ').grid(row=6,column=2)
# 
# l = Label(text='Grade ').grid(row=2,column=3)
# e = Entry(w).grid(row=3,column=3)
# e = Entry(w).grid(row=4,column=3)
# e = Entry(w).grid(row=5,column=3)
# e = Entry(w).grid(row=6,column=3)
# 
# l = Label(text='Reg.No ').grid(row=0,column=4)
# e = Entry(w).grid(row=0,column=5)
# 
# l = Label(text='Sub credit ').grid(row=2,column=4)
# l = Label(text='4 ').grid(row=3,column=4)
# l = Label(text='4 ').grid(row=4,column=4)
# l = Label(text='3 ').grid(row=5,column=4)
# l = Label(text='4 ').grid(row=6,column=4)
# l = Label(text='Total credit ').grid(row=7,column=4)
# l = Label(text='SGPA ').grid(row=8,column=4)
# 
# l = Label(text='Credit obtained').grid(row=2,column=5)
# 
# 
# b = Button(w,text='submit',bg='green').grid(row=8,column=2)
# 
# 
# w.mainloop()


from tkinter import *
from tkinter import messagebox

w=Tk()
# w.geometry('800x300')
#
# frame1 = Frame(w,background='red',width='150',height='200').place(x=0,y=0)
# frame2 = Frame(w,background='yellow',width='400',height='200').place(x=150,y=0)
#
#
# b1=Button(frame1,text='Button1').place(x=50,y=50)
# b1=Button(frame1,text='Button2').place(x=50,y=125)
#
#
# # b1=Button(frame2,text='Button3').place(x=200,y=75)
# # b1=Button(frame2,text='Button4').place(x=280,y=75)
#
#
# w.mainloop()


# l = Label(text='Choose your favourite prg language:').grid(row=0,column=1)
# var1=IntVar()
# var2=IntVar()
# var3=IntVar()
# var4=IntVar()
# var5=IntVar()
# r1=Radiobutton(w, text= " python",variable= var1, value=1)
# r1.grid(row=1,column=1,sticky=W)
# r2=Radiobutton(w, text= "perl",variable= var2, value=1)
# r2.grid(row=2,column=1,sticky=W)
# r1=Radiobutton(w, text= "java",variable= var3, value=1)
# r1.grid(row=3,column=1,sticky=W)
# r1=Radiobutton(w, text= " c++",variable= var4, value=1)
# r1.grid(row=4,column=1,sticky=W)
# r1=Radiobutton(w, text= " c",variable= var5, value=1)
# r1.grid(row=5,column=1,sticky=W)
#
# w.mainloop()


# l = Label(text='Select how do u feel today:').grid(row=0,column=1)
#
# c1 = IntVar()
# c2 = IntVar()
# c3 = IntVar()
# c4 = IntVar()
# c5 = IntVar()
# cb1=Checkbutton(w, text = "ALl", variable = c1,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=1,column=1,sticky='W')
# cb2=Checkbutton(w, text = "Happy", variable = c2,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=2,column=1,sticky='W')
# cb2=Checkbutton(w, text = "Sad", variable = c3,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=3,column=1,sticky='W')
# cb2=Checkbutton(w, text = "Angry", variable = c4,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=4,column=1,sticky='W')
# cb2=Checkbutton(w, text = "None", variable = c5,
#                  onvalue=1,
#                  offvalue=0,
#                  height=2,
#                  width=10).grid(row=5,column=1,sticky='W')
#
# b1 = Button(w,text="Select",width=10).grid(row=6,column=1,sticky='W')
#
# w.mainloop()



l = Label(text='Enter name:').grid(row=0,column=1)
l = Label(text='Enter email:').grid(row=1,column=1)
l = Label(text='Contact number:').grid(row=2,column=1)
l = Label(text='Select Gender:').grid(row=3,column=1)
l = Label(text='Select country:').grid(row=5,column=1)
l = Label(text='Enter password:').grid(row=6,column=1)
l = Label(text='Re-Enter password:').grid(row=7,column=1)



e = Entry(w).grid(row=0,column=2)
e = Entry(w).grid(row=1,column=2)
e = Entry(w).grid(row=2,column=2)
e = Entry(w).grid(row=6,column=2)
e = Entry(w).grid(row=7,column=2)

b = Button(w,text='Register',width=16).grid(row=8,column=2)


var1=IntVar()
var2=IntVar()
var3=IntVar()
r1=Radiobutton(w, text= " Male",variable= var1, value=1)
r1.grid(row=3,column=2,columnspan=2)
r2=Radiobutton(w, text= "Female",variable= var2, value=2)
r2.grid(row=4,column=2,columnspan=2)
r1=Radiobutton(w, text= " Others",variable= var3, value=1)
r1.grid(row=5,column=2,columnspan=2)


w.mainloop()

import pytest