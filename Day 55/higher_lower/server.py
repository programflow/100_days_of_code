from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def guess_number():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDJybWxxcXZteXJsM2p3eXM4MGNyNmRzMDlkbjVpODZxYWhrNjY5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CjmvTCZf2U3p09Cn0h/giphy.gif' width=400>")

generated_num = random.randint(1,9)

@app.route("/<int:guess>")
def check_guess(guess):
    if int(guess) < generated_num:
        return (f"<h1 style='color: Tomato'>Sorry, you guessed too low</h1>"
                f"<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemNlMHh5am9yd282M3huYnNkcDJ6dTNlenQ1d2FpYzVkY3h4b3luZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/saJYuwjsF8Kfm/giphy.gif' width=400>")
    elif int(guess) > generated_num:
        return (f"<h1 style='color: SlateBlue'>Sorry, you guessed too high</h1>"
                f"<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWdzenE3YmljZDF0dG5nbnhsODVvaTU4ZjJoaW40MmRjYmZrc293ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/x3xccAsYXuslW/giphy.gif' width=400>")
    else:
        return (f"<h1 style='color: MediumSeaGreen'>Woot, you guessed the correct number</h1>"
                f"<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXVtamlrdmY0Z2FuMHZiOXNld3FwbnRvejJ0YXl3bTA2cm9sNDRndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PSKAppO2LH56w/giphy.gif' width=400>")

if __name__ == "__main__":
    app.run(debug=True)

