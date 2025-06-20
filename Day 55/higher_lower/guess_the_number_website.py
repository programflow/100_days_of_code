from flask import Flask, render_template

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/")
def hello_word():
    return ('<h1 style="text-align: center;">Guess the Number</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDJybWxxcXZteXJsM2p3eXM4MGNyNmRzMDlkbjVpODZxYWhrNjY5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CjmvTCZf2U3p09Cn0h/giphy.gif" width=200>')

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

@app.route("/username/<name>/<int:number>")
def greet(name,number=12):
    return f"Hello there bird {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
