import random
import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    agify_endpoint = "https://api.agify.io?"
    agify_response = requests.get(f"{agify_endpoint}name={name.title()}")
    agify_data = agify_response.json()

    genderize_endpoint = "https://api.genderize.io?"
    genderize_response = requests.get(f"{genderize_endpoint}name={name.title()}")
    genderize_data = genderize_response.json()

    return render_template("guess.html", agify_data=agify_data, genderize_data=genderize_data)


@app.route("/blog/<blog_id>")
def get_blog(blog_id):
    blog_url = "https://api.npoint.io/bcee3d8376f927f4a680"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)
