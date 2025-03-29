from tkinter import *

w = Tk()
w.config(bg="grey")
w.geometry("1000x800")
main_label = Label(w,text='CricPLUS',font=("Arial", 50),background='light blue',foreground='orange',bd=2, relief="solid").pack(pady=50)

live_button = Button(w,text='LIVE',font=("Arial", 20),height=5,width=10,bg='brown',activebackground='grey').place(x=130,y=300)
sc_button = Button(w,text='SCORECARD',font=("Arial", 20),height=5,width=11,bg='brown',activebackground='grey').place(x=380,y=300)
commentry_button = Button(w,text='COMMENTRY',font=("Arial", 20),height=5,width=11,bg='brown',activebackground='grey').place(x=630,y=300)


w.mainloop()