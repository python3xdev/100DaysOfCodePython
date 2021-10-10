import smtplib
import requests
from flask import Flask, render_template, request

my_email = "your_email@email.com"
password = "your_password"

app = Flask(__name__)

all_blog_data = []


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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
    return render_template("contact.html")


def send_email(name, email, phone, message):
    print("Sending The Email...")
    full_message = f'''Name: {name}\n- - - - - - -\nMessage:\n{message}\n- - - - - - -\nEmail:{email}\nPhone:\n{phone}'''
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Blog Website Contact Form\n\n{full_message}"
        )
    print("Email Has Been Sent")

@app.route("/post/<int:id_num>")
def post(id_num):
    requested_blog = all_blog_data[id_num - 1]
    return render_template("post.html", blog_data=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
