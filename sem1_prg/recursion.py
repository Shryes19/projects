# def gcd(x,y):
#     if x==y:
#         return x
#     elif x >= y:
#         return gcd(x-y,y)
#     else:
#         return gcd(x,y-x)
#
# print(gcd(65,91))

#************************************************************************#

# def fib(x):
#     if x <= 1:
#         return x
#     else:
#         return fib(x - 1) + fib(x - 2)
#
#
# for i in range(10):
#     print(fib(i))

#*************************************************************************#

# def length(s):
#     if s == '':
#         return 0
#     return length(s[1:]) + 1
#
#
# print(length("hello"))

#*************************************************************************#

# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# print(sum(10))

#*************************************************************************#

# def power(x,y):
#     if y==0:
#         return 1
#     return x*power(x,y-1)
# print(power(2,4))

#*************************************************************************#

# def divide(x, y):
#     if x < y:
#         return 0
#     else:
#         return divide(x - y, y) + 1
#
#
# print(divide(1000, 100))

#**************************************************************************#

# def mimic_in(x, s):
#     if len(s)==0:
#         return False
#     elif s[0] == x:
#         return True
#     else:
#         return mimic_in(x, s[1:])
#
# print(mimic_in('2', ['1','2']))

#****************************************************************************#

# def multiply(x,y):
#     if y==0:
#         return 0
#     else:
#         return x+multiply(x,y-1)
# print(multiply(0,10))

import tkinter
master=tkinter.Tk()
master.geometry("450x350")
button1=tkinter.Button(master, text="LEFT", command = master.destroy, bg = "#FFCCDD")
button1.pack(side=tkinter.LEFT) #side can be
button2=tkinter.Button(master, text="RIGHT")
button2.pack()
button3=tkinter.Button(master, text='TOP')
button3.pack()
button4=tkinter.Button(master, text="BOTTOM")
button4.pack() # "bottom"
master.mainloop()