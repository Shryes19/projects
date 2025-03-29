from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
my_label = Label(text="This is my label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.grid(column=0, row=0)

def button_click():
    new_text = input.get()
    my_label["text"] = new_text
button = Button(text="Click me",command=button_click)
button.grid(column=1, row=1)

input = Entry(width=10)
input.insert(END, string = "type here")
input.grid(column=2, row=2)
#
# text = Text(height=5, width = 30)
# text.focus()
# text.insert(END, "Example is here")
# text.pack()
#
# spinbox = Spinbox(from_=0, to=10, width=5)
# spinbox.pack()
#
# def scale_box(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_box)
# scale.pack()
#
#
# def check():
#     print(checked_state.get())
# checked_state = IntVar()
# checkbutton = Checkbutton(text="is ON?", variable=checked_state, command=check)
# #checked_state.get()
# checkbutton.pack()
#
# def radio():
#     print(radio_state.get())
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Banana", "Orange"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()


window.mainloop()