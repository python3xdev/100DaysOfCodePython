import requests
from post import Post
from flask import Flask, render_template

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/bcee3d8376f927f4a680").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    endpoint = "https://api.npoint.io/bcee3d8376f927f4a680"
    response = requests.get(endpoint)
    all_blogs = response.json()
    return render_template("index.html", blogs=all_blogs)


@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    for blog in post_objects:
        if blog.id == blog_id:
            return render_template("post.html", post=blog)


if __name__ == "__main__":
    app.run(debug=True)
