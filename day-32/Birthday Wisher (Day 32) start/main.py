import smtplib
import datetime as dt
import random

now = dt.datetime.now()
week_day = now.weekday()
hour = now.min
print(hour)
if week_day == 0  :
    with open("quotes.txt") as f:
        q = f.readlines()
        quote = random.choice(q)

    my_email = "shryesPython19@gmail.com"
    password = "vrrsuydjhnzxleub"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shryes107@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

