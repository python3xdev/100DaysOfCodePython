from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<strong>{func()}</strong>"
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
def hello_world():
    return "<h1 style='text-align: center;'>Hello World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
