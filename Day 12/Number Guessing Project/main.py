import random
import art

def set_game_difficulty(difficulty):
    if difficulty.lower() == "easy":
        return EASY_LEVEL_TURNS
    if difficulty.lower() == "hard":
        return HARD_LEVEL_TURNS

def compare_number(player_number, correct_number):
    if player_number == correct_number:
        print(f"You got it! The answer was {correct_number}.")
        exit()
    elif player_number > correct_number:
        print(f"Too high.")
    elif player_number < correct_number:
        print(f"Too low.")

def game():
    EASY_LEVEL_TURNS = 10
    HARD_LEVEL_TURNS = 5


    print(art.logo)

    print("Welcome to the Number Guessing Game!")
    game_on = "y"

    while game_on== "y":

        number = random.randint(1,100)
        attempts = set_game_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))

        while attempts != -1:

            if attempts != 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
                guessed_number = int(input("Make a guess: "))
                compare_number(guessed_number, number)
            else:
                print(f"You've run out of guesses, you lose.")
                exit()


            attempts -= 1



        game_on = input("Would you like to play again? Type 'y' for yes and 'n' for no.")


game()