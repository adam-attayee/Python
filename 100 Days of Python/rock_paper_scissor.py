import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissor = [rock, paper, scissors]

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_selection = random.randint(0,2)

if user_selection > 2:
    print("Invalid selection, You lose")
    exit()

print(rock_paper_scissor[user_selection])
print("Computer chose:\n" + rock_paper_scissor[computer_selection])

if computer_selection == user_selection:
    print("It's a draw")
elif computer_selection == 2 and user_selection == 0:
    print("You win!")
elif computer_selection == 0 and user_selection == 2:
    print("You lose")
elif computer_selection > user_selection:
    print("You lose")
elif user_selection > computer_selection:
    print("You win!")
