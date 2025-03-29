import tkinter
import tkinter.ttk
import csv

def load_movies(file_name):
    movies = []
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

def get_movies_by_date(date):
    movies = []
    for movie in movies_data:
        if movie["Date"] == date and movie["Movie_Name"] not in [m["Movie_Name"] for m in movies]:
            movies.append(movie)
    return movies

def get_times_by_movie(movie_name, date):
    times = []
    for movie in movies_data:
        if movie["Date"] == date and movie["Movie_Name"] == movie_name:
            times.append(movie["Time"])
    return times

def reset_fields():
    movie_var.set("")
    date_var.set("")
    time_var.set("")
    tickets_var.set("")
    label_ticket["text"] = "Ticket Price: ₹0"

def book_tickets():
    selected_movie = movie_var.get()
    selected_date = date_var.get()
    selected_time = time_var.get()
    requested_tickets = tickets_var.get()

    if not selected_movie or not selected_date or not selected_time or not requested_tickets:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not requested_tickets.isdigit() or int(requested_tickets) <= 0:
        messagebox.showerror("Error", "Please enter a valid number of tickets.")
        return

    requested_tickets = int(requested_tickets)

    for movie in movies_data:
        if movie["Movie_Name"] == selected_movie and movie["Date"] == selected_date and movie["Time"] == selected_time:
            available_seats = int(movie["Available_Seats"])
            ticket_price = int(movie["Ticket_Price"])
            break
    else:
        messagebox.showerror("Error", "Movie not found.")
        return

    if available_seats >= requested_tickets:
        total_cost = requested_tickets * ticket_price
        movie["Available_Seats"] = str(available_seats - requested_tickets)
        save_changes()
        messagebox.showinfo(
            "Booking Confirmation",
            f"Booking Confirmed\n\n"
            f"Movie: {selected_movie}\n"
            f"Date: {selected_date}\n"
            f"Time: {selected_time}\n"
            f"Tickets: {requested_tickets}\n"
            f"Total Cost: ₹{total_cost}"
        )
        reset_fields()
    else:
        messagebox.showwarning('Error',
            f"Only {available_seats} seats are available. Please adjust your ticket count."
        )

def save_changes():
    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Movie_Name", "Date", "Time", "Available_Seats", "Ticket_Price"])
        writer.writeheader()
        writer.writerows(movies_data)

def update_movies(event):
    selected_date = date_var.get()
    movies = [movie["Movie_Name"] for movie in get_movies_by_date(selected_date)]
    combo_movie["values"] = movies
    movie_var.set("")
    combo_time["values"] = []
    time_var.set("")

def update_times(event):
    selected_movie = movie_var.get()
    selected_date = date_var.get()
    times = get_times_by_movie(selected_movie, selected_date)
    combo_time["values"] = times
    time_var.set("")
    for movie in movies_data:
        if movie["Movie_Name"] == selected_movie and movie["Date"] == selected_date:
            label_ticket["text"] = f"Ticket Price: ₹{movie['Ticket_Price']}"
            break

file_name = "orange_sem1.csv"
movies_data = load_movies(file_name)

dates = sorted(set(movie["Date"] for movie in movies_data))
print(movies_data)
print(dates)
#-------------------------------------UI------------------------------------------------#
from tkinter import *
from tkinter import messagebox

w = Tk()
w.title("BookMyShow")

date_var = tkinter.StringVar()
movie_var = tkinter.StringVar()
time_var = tkinter.StringVar()
tickets_var = tkinter.StringVar()

label_head = Label(w, text="Movie Ticket Booking System", font=("Arial", 16))
label_head.grid(row=0, column=0, columnspan=2, pady=10)

label_date = Label(w, text="Select Date:")
label_date.grid(row=1, column=0, sticky="w", padx=10, pady=5)
combo_date = tkinter.ttk.Combobox(w, state="readonly", values=dates, textvariable=date_var)
combo_date.grid(row=1, column=1, padx=10, pady=5)
combo_date.bind("<<ComboboxSelected>>", update_movies)

label_movie = Label(w, text="Select Movie:")
label_movie.grid(row=2, column=0, sticky="w", padx=10, pady=5)
combo_movie = tkinter.ttk.Combobox(w, state="readonly", textvariable=movie_var)
combo_movie.grid(row=2, column=1, padx=10, pady=5)
combo_movie.bind("<<ComboboxSelected>>", update_times)

label_time = Label(w, text="Select Time:")
label_time.grid(row=3, column=0, sticky="w", padx=10, pady=5)
combo_time = tkinter.ttk.Combobox(w, state="readonly", textvariable=time_var)
combo_time.grid(row=3, column=1, padx=10, pady=5)

label_ticket = Label(w, text="Ticket Price: ₹0", font=("Arial", 12))
label_ticket.grid(row=4, column=0, columnspan=2, pady=5)

label_num = Label(w, text="Number of Tickets:")
label_num.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_tickets = Entry(w, textvariable=tickets_var)
entry_tickets.grid(row=5, column=1, padx=10, pady=5)

button_book = Button(w, text="Book Tickets", command=book_tickets)
button_book.grid(row=6, column=0, pady=10)
button_reset = Button(w, text="Reset", command=reset_fields)
button_reset.grid(row=6, column=1, pady=10)



w.mainloop()
