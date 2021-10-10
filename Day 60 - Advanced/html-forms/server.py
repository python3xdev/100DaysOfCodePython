from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return f'<h1>Username: {username}<br>Password: {password}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
