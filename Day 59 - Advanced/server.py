import requests
from flask import Flask, render_template

app = Flask(__name__)

all_blog_data = []

'''
Blog Post Dict/JSON Format (Free API Creator: npoint.io):
    {
    "id": 5,
    "title": "New Blog Post Title",
    "subtitle": "New Blog Post Subtitle",
    "body": "New Blog Post Body Text",
    "date":"October 1st, 2021",
    "author":"Template",
    "image_url":"https:://www.images.com/your-image",
    },
'''


def get_blog_data():
    global all_blog_data
    response = requests.get("https://api.npoint.io/09054336867fdb691112")
    json = response.json()
    all_blog_data = json


@app.route('/')
def home():
    get_blog_data()
    return render_template('index.html', all_posts=all_blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:id_num>")
def post(id_num):
    requested_blog = all_blog_data[id_num - 1]
    return render_template("post.html", blog_data=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
