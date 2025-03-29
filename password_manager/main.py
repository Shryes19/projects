from tkinter import *
from tkinter import messagebox
import pyperclip, json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def passw():
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    p_letters = [random.choice(letters) for _ in range(nr_letters)]
    p_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    p_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = p_numbers + p_symbol + p_letters
    random.shuffle(password_list)

    Password = "".join(password_list)
    input3.insert(0, Password)
    pyperclip.copy(Password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    global is_ok
    password = input3.get()
    gmail = input2.get()
    Website = input1.get()
    new_data = {
        Website: {
            "email": gmail,
            "password": password
        }
    }
    if len(password) == 0 or len(Website) == 0:
        messagebox.showwarning(title=Website, message="INVALID ENTRY")
        print("no")

    else:
     is_ok = messagebox.askokcancel(title=Website, message=f"These are the details entered:\nEmail: {gmail}\nPassword: {password}\nIs it ok to save?")

     if is_ok:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            input3.delete(0, END)
            input1.delete(0, END)


# --------------------------------------------------------------------- #
def find_password():
    dic = {}
    try:
        with open("data.json", 'r') as data_file:
            d = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found")

    else:
            if input1.get() in d.keys():
                dic = (d[input1.get()])
                #print(dic["email"])
                messagebox.showinfo(title=input1.get(), message=f"Email: {dic["email"]}\nPassword: {dic["password"]}")

            else:
                messagebox.showwarning(title=input1.get(), message="No details for the website")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Courier", 16, "normal"))
email = Label(text="Email/Username:", font=("Courier", 16, "normal"))
password = Label(text="Password:", font=("Courier", 16, "normal"))
website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)

input1 = Entry(width=21)
input1.focus()
#input1.insert(END, string = "")
input1.grid(column=1, row=1, columnspan=2, sticky=EW)
input2 = Entry(width=35)
input2.insert(END, string="shryes107@gmail.com")
input2.grid(column=1, row=2, columnspan=2, sticky=EW)
input3 = Entry(width=21)
#input3.insert(END, string = "")
input3.grid(column=1, row=3, sticky=EW)

button1 = Button(text="Generate Password", command=passw)
button1.grid(column=2, row=3, sticky=EW)
button2 = Button(text="Add", width=35, command=save)
button2.grid(column=1, row=4, columnspan=2, sticky=EW)
button3 = Button(text="Search", command=find_password)
button3.grid(column=2, row=1, sticky=EW)

window.mainloop()
