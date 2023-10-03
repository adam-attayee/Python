# simple program that asks for the user's name and email, and appends it to google sheets.
# the sheet contains 3 headers: [First Name, Last Name, Email]
# Sheety API is used for this program

import requests

SHEET_ENDPOINT = ""ENTER SHEET ENDPOINT"

print("Welcome to the book club.")
print("Povide the information below to join.")

first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()
email = input("What is your email?\n")
confirm_email = input("Type your email again?\n")

if email == confirm_email:
    print("You're in the club!")

    parameters = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=parameters)
    response.raise_for_status()
    print(response.text)
