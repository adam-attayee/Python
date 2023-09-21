import string, random

alphabet = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print("Welcome to the password Generator!")

number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_digits = int(input("How many numbers would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))

password = []

for letter in range(1, number_of_letters + 1):
    password.append(random.choice(alphabet))

for symbol in range(1, number_of_symbols + 1):
    password.append(random.choice(symbols))

for digit in range(1, number_of_digits + 1):
    password.append(random.choice(digits))

random.shuffle(password)
password = "".join(password)

print(f"Here is your password: {password}")
