import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def show_partial_score():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")


def show_full_score():
    print(f"Your final cards: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final card: {computer_cards}, final score: {sum(computer_cards)}")


def start_game():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        global player_cards
        global computer_cards
        player_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        player_turn()
    elif choice == 'n':
        return


def computer_turn():
    computer_score = sum(computer_cards)

    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)

    if computer_score > 21:
        for i in range(0, len(computer_cards)):
            if computer_cards[i] == 11:
                computer_cards[i] = 1
                break
        else:
            show_full_score()
            print("You Win!")
            start_game()

        computer_turn()

    elif computer_score > sum(player_cards):
        show_full_score()
        print("Computer Wins!")
        start_game()
    elif sum(player_cards) > computer_score:
        show_full_score()
        print("You Win!")
        start_game()
    else:
        show_full_score()
        print("It's a Draw!")
        start_game()


def player_turn():

    player_score = sum(player_cards)
    
    continue_game = True
    
    while continue_game:
        if player_score > 21:
            for i in range(0, len(player_cards)):
                if player_cards[i] == 11:
                    player_cards[i] = 1
                    show_partial_score()
                    break
            else:
                show_full_score()
                print("You went over. Your lose.")
                start_game()
        elif player_score == 21:
            computer_turn()
    
        player_action = input("Type 'y' to get another card, type 'n' to pass: ")
    
        if player_action == 'y':
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)
            show_partial_score()
        else:
            computer_turn()


start_game()
