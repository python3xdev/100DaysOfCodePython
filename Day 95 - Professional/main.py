import requests
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

URL = "https://owlbot.info/api/v4/dictionary"
headers = {
    "Authorization": 'Token YOUR_TOKEN_FOR_OWLBOTS_API'
}

# Words to test the functionality: Apple, Truck, Chicken, Monkey, Money


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        word = request.form['word']
        response = requests.get(f'{URL}/{word}', headers=headers)
        data = response.json()
        is_dict = True if type(data) is dict else False
        return render_template("search.html", data=data, is_dict=is_dict)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
