from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)


class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    map_url = db.Column(db.String, unique=True, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String, nullable=False)
    coffee_price = db.Column(db.String, nullable=False)


@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        try:
            new_cafe = Cafe(
                name=request.form['name'],
                map_url=request.form['map_url'],
                img_url=request.form['img_url'],
                location=request.form['location'],
                has_sockets=1 if request.form['has_sockets'][0].lower() == 'y' else 0,
                has_toilet=1 if request.form['has_toilet'][0].lower() == 'y' else 0,
                has_wifi=1 if request.form['has_wifi'][0].lower() == 'y' else 0,
                can_take_calls=1 if request.form['can_take_calls'][0].lower() == 'y' else 0,
                seats=request.form['seats'],
                coffee_price=f"£{request.form['coffee_price']}"
            )
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for('home'))
        except:
            return "<h1>This cafe already exists! Go Back to <a href='/add'>Add</a> or <a href='/'>Home</a>.</h1>"
    return render_template("add.html")


@app.route("/delete/<cafe_id>")
def delete(cafe_id):
    Cafe.query.filter_by(id=cafe_id).delete()
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
