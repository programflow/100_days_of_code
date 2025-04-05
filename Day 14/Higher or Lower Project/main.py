import random
from game_data import data
import art

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def new_profiles(answer, p_a, p_b):
    if answer == 'B':
        p_a = p_b
    p_b = random.choice(data)
    return p_a, p_b

def get_two_distinct_profiles(profiles):
    p_a = random.choice(profiles)
    p_b = random.choice(profiles)
    while p_a['name'] == p_b['name']:
        p_b = random.choice(data)
    return p_a, p_b

print(art.logo)

game_on = 'y'
while game_on == 'y':

    profile_a, profile_b = get_two_distinct_profiles(data)

    score = 0
    keep_playing = True
    while keep_playing:
        print(f"Compare A: " + format_data(profile_a))


        print(art.vs)

        print("Compare B: " + format_data(profile_b))

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess not in ['A', 'B']:
            print("Invalid input. Please type 'A' or 'B'.")
            continue
        elif profile_a['follower_count'] > profile_b['follower_count']:
            correct_answer = "A"
        else:
            correct_answer = "B"

        if guess == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
            profile_a, profile_b = new_profiles(guess, profile_a, profile_b)

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    game_on = input(f"Would you like to play again? Type 'y' for yes and 'n' for no: ")


