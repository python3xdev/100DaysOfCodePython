from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6don56hy5yu7u5x7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

endpoint = "https://api.themoviedb.org/3"
api_key = "your_api_key"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10, e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    ordered_movies = Movie.query.order_by(Movie.rating).all()  # https://www.youtube.com/watch?v=BJeiVGAvEFI - 👍
    for movie in ordered_movies:
        movie.ranking = ordered_movies[::-1].index(movie) + 1
    db.session.commit()
    return render_template("index.html", all_movies=ordered_movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    movie_id = request.args.get('movie_id')
    if movie_id:
        parameters = {
            "api_key": api_key,
        }
        response = requests.get(f"{endpoint}/movie/{movie_id}", params=parameters)
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            year=data['release_date'][:4],
            description=data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))
    form = AddForm()
    if form.validate_on_submit():
        movie_title = request.form['title']
        parameters = {
            "api_key": api_key,
            "query": movie_title
        }
        response = requests.get(f"{endpoint}/search/movie", params=parameters)
        data = response.json()
        all_results = data['results']
        print(all_results)
        return render_template("select.html", movies_list=all_results)
    return render_template("add.html", form=form)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie_to_edit = Movie.query.filter_by(id=movie_id).first()
    if form.validate_on_submit():
        new_rating = request.form['rating']
        new_review = request.form['review']
        movie_to_edit.rating = new_rating
        movie_to_edit.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_edit, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
