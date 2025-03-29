from tkinter import *


window = Tk()
window.minsize(width=500, height=300)
window.title("Mile to Km converter")
window.config(padx=200, pady=100)

input = Entry(width=10)
input.insert(END, string="")
input.grid(column=1, row=0)
#input.config(padx=100,pady=100)
my_label = Label(text="Miles", font=("Arial", 16, "bold"))
my_label.grid(column=2, row=0)
my_label2 = Label(text="is equal to", font=("Arial", 16, "bold"))
my_label2.grid(column=0, row=1)
my_label3 = Label(text="km", font=("Arial", 16, "bold"))
my_label3.grid(column=2, row=1)


def calc():
    v = float(int(input.get()) * 1.609)
    my_label4 = Label(text=v, font=("Arial", 16, "bold"))
    my_label4.grid(column=1, row=1)


button = Button(text="Calculate", width=10, height=1, command=calc)
button.grid(column=1, row=2)

window.mainloop()
