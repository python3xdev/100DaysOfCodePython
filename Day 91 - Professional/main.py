import numpy
import os

from PIL import Image
from flask import Flask, render_template, url_for, redirect, request, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b"f*&HB5&*gf^5ERG7FJ.,hj"


@app.route("/")
def home():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('colors', filename=filename))
    return redirect(url_for('home'))


@app.route("/colors/<filename>")
def colors(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image = Image.open(filepath)
    image_array = numpy.array(image)
    unique_colors = numpy.unique(image_array.reshape(-1, image_array.shape[-1]), axis=0, return_counts=True)
    results = {}
    colors_list = [list(color[:-1]) for color in unique_colors[0]]
    for color in colors_list:
        print(color)
        if str(color) not in results:
            results[str(color)] = list(unique_colors[1])[colors_list.index(color)]
        else:
            results[str(color)] += 1
    results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    os.remove(filepath)  # so the server does not build up image files...
    return render_template("colors.html", color_data=results)


if __name__ == "__main__":
    app.run(debug=True)
