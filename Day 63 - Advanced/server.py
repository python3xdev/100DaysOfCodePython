from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'  # or you can use: "<Title %r>" % self.title


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # creating a new record
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = request.args.get('id')
        book_to_update = Book.query.filter_by(id=book_id).first()
        book_to_update.rating = request.form['new-rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book = Book.query.filter_by(id=book_id).first()
    return render_template("edit.html", book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book = Book.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

