import random
from game_data import game_data
import game_art

# CURRENT_SCORE = 0

def generate_random_index(iterable):
    """This function returns a random number to be used as the index of each random item in the game"""
    random_index = random.randint(0,len(iterable)-1)
    return random_index

def follower_count(index):
    """This function returns the number of followers given the index of the item in the game_data list"""
    num_following = game_data[index]["follower_count"]
    return num_following

def game():

    # generate 2 random items from the list and create a variable to keep track of score
    item_a_index = generate_random_index(game_data)
    item_b_index = generate_random_index(game_data)
    CURRENT_SCORE = 0

    continue_game = True
    print(game_art.logo)

    while continue_game:

        #make sure that the indexes do not match
        while item_a_index == item_b_index:
            item_b_index = generate_random_index(game_data)

        #create variables to track the following count so that it can be compared
        a_following = follower_count(item_a_index)
        b_following = follower_count(item_b_index)

        #print the description of each item and ask user which one has a higher following
        print(f"Compare A: {game_data[item_a_index]['name']}, a {game_data[item_a_index]['description']}, from {game_data[item_a_index]['country']}.")
        print(game_art.vs)
        print(f"Against B: {game_data[item_b_index]['name']}, a {game_data[item_b_index]['description']}, from {game_data[item_b_index]['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        #write the logic to figure out if the user was right or wrong
        #if user gets it right, item B should become item A, and a new item is chosen for B
        if answer == 'a' and a_following > b_following:
            CURRENT_SCORE += 1
            item_a_index = item_b_index
            item_b_index = generate_random_index(game_data)
            print(f"You're right! Current score: {CURRENT_SCORE}.")
        elif answer == 'b' and b_following > a_following:
            CURRENT_SCORE += 1
            item_a_index = item_b_index
            b_following = generate_random_index(game_data)
            print(f"You're right! Current score: {CURRENT_SCORE}.")
        else:
            print(f"Sorry, that's wrong. Final score: {CURRENT_SCORE}")
            continue_game = False

game()
