import random
from game_data import data
import art

def new_profiles(answer, p_a, p_b):
    if answer == 'A':
        p_b = random.choice(data)
        return p_a, p_b
    else:
        p_a = p_b
        p_b = random.choice(data)
        return p_a, p_b

print(art.logo)

game_on = 'y'
while game_on == 'y':

    profile_a = random.choice(data)
    profile_b = random.choice(data)
    while profile_a['name'] == profile_b['name']:
        profile_b = random.choice(data)

    score = 0
    keep_playing = True
    while keep_playing:
        print(f"Compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']} ")


        print(art.vs)

        print(f"Compare B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']} ")

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if profile_a['follower_count'] > profile_b['follower_count']:
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


