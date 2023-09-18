import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

def check(computer_number, user_guess):
    if computer_number > user_guess:
        print("Too low.\nGuess again.")
    elif computer_number < user_guess:
        print("Too high.\nGuess again.")

def user_guess():

    number = random.choice(range(1, 101))
    attempts_remaining = attempts

    while attempts_remaining > 1:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        print(f"the number is {number}")
        user_choice = int(input("Make a guess: "))

        if number == user_choice:
            print(f"You got it. The answer was {number}")
            return

        check(computer_number=number, user_guess=user_choice)
        attempts_remaining -= 1

    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    user_choice = int(input("Make a guess: "))

    if user_choice == number:
        print(f"You got it. The answer was {number}")
    else:
        print(f"You've run out of guesses, you lose. The number was {number}")

user_guess()
