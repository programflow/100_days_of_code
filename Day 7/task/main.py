import random


import hangman_words
import hangman_art
word_list = hangman_words.word_list

lives = 6


print(hangman_art.logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    guessed_letters = ""
    if guess not in guessed_letters:
        guessed_letters += guess

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)



        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            if lives == 0:
                game_over = True


                print(f"***********************YOU LOSE**********************")
                print(f"The answer is {chosen_word}")
                exit()

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")
            exit()

        # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
        print(hangman_art.stages[lives])
    else:
        print(f"You've already guessed {guess}")