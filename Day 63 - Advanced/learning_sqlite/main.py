# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask Instance
app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize The Database
db = SQLAlchemy(app)


# Create a Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'  # or you can use: "<Title %r>" % self.title


# Creating the Database
# db.create_all()

# CREATE RECORD
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# READ ALL records
# all_books = db.session.query(Book).all()
# print(all_books)

# READ A SPECIFIC record by QUERY
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# UPDATE A Particular Record By QUERY
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# UPDATE A Record By PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# DELETE A Particular Record By PRIMARY KEY (you can also find the record by other values)
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
