from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6dzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    post = db.session.query(BlogPost).filter_by(id=index).first()
    return render_template("post.html", post=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = db.session.query(BlogPost).filter_by(id=post_id).first()
    edit_form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        img_url=post_to_edit.img_url,
        author=post_to_edit.author,
        body=post_to_edit.body
    )
    if edit_form.validate_on_submit():
        post_to_edit.title = request.form.get('title')
        post_to_edit.subtitle = request.form.get('subtitle')
        post_to_edit.author = request.form.get('author')
        post_to_edit.img_url = request.form.get('img_url')
        post_to_edit.body = request.form.get('body')
        db.session.commit()
        return redirect(url_for('show_post', index=post_to_edit.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        x = datetime.datetime.now()
        new_blog_post = BlogPost(
            date=x.strftime("%B %d, %Y | %I:%M %p"),
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            author=request.form.get('author'),
            img_url=request.form.get('img_url'),
            body=request.form.get('body'),
        )
        db.session.add(new_blog_post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.session.query(BlogPost).filter_by(id=post_id).first()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
