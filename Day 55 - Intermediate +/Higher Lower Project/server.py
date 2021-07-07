from random import randint
from flask import Flask

app = Flask(__name__)

random_number = randint(0, 9)
print(random_number)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9. Hint: Use the URL bar to guess you number... E.G: /1</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def number_page(number):
    if number == random_number:
        return "<h1>You guessed it!</h1>" \
               "<img src='https://media.giphy.com/media/3ohs4xsq0oEhqC4why/giphy.gif'>"
    elif number > random_number:
        return "<h1>To high, try again...</h1>" \
               "<img src='https://media.giphy.com/media/6USOqXUeLxFFGLR8Rz/giphy.gif'>"
    else:
        return "<h1>To low, try again...</h1>" \
               "<img src='https://media.giphy.com/media/rZaBBQ6uAkCBi/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
