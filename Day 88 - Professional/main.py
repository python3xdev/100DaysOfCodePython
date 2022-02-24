from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_list.db'
db = SQLAlchemy(app)


class TodoItem(db.Model):
    __tablename__ = "todo_list"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    complete = db.Column(db.Boolean, nullable=False)


@app.route("/")
def home():
    todos = TodoItem.query.all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_item = TodoItem(
            title=request.form['title'],
            complete=False
        )
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete/<todo_item_id>", methods=['GET', 'POST'])
def delete(todo_item_id):
    TodoItem.query.filter_by(id=todo_item_id).delete()
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/update/<todo_item_id>", methods=['GET', 'POST'])
def change_status(todo_item_id):
    todo_item = TodoItem.query.filter_by(id=todo_item_id).first()
    todo_item.complete = True if not todo_item.complete else False
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)

