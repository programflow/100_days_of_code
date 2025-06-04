from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)
# When the user navigates to the url with just the forward slash. show them the homepage with "hello world"
@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

# THe @app.route("/") syntax is a python decorator. A decorator function gives additional functionality to an existing function
if __name__ == "__main__":
    app.run()
