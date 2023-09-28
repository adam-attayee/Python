import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "name@gmail.com"
MY_APP_PASS = "app_pass"

current_month = dt.datetime.now().month
today = dt.datetime.now().day

df = pd.read_csv("birthdays.csv")
data = df[(df.month == current_month) & (df.day == today)]

if not data.empty:
    # There are 3 letter templates to randomly choose from.
    num_templates = 3
    random_template = random.randint(1, 3)
    with open(f"./letter_templates/letter_{random_template}.txt") as file:
        letter_template = file.read()

        for index, row in data.iterrows():
            recipient_name = row["name"]
            recipient_email = row["email"]
            birthday_letter = letter_template.replace("[NAME]", recipient_name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_APP_PASS)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient_email,
                                    msg=f"Subject:Happy Birthday {recipient_name}!!\n\n{birthday_letter}")
