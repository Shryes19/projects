import datetime as dt
import pandas, smtplib, random

my_email = "shryesPython19@gmail.com"
password = "vrrsuydjhnzxleub"
today = (dt.datetime.now().month , dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}



file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
if today in birthdays_dict:
    person = birthdays_dict[today]
    with open(file_path) as letter1:
        l1 = letter1.read()
        l1 = l1.replace("[NAME]", person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject:Happy Birthday!\n\n{l1}")


