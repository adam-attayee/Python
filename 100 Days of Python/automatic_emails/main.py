#choose a random quote from the quotes.txt file and send it to the recipient if its a monday

import smtplib
import datetime as dt
import random

my_email = "test.email@gmail.com"
password = "app_password"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote_of_the_day = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="another.email@gmail.com",
                            msg=f"Subject:Quote of the day\n\n{quote_of_the_day}")
