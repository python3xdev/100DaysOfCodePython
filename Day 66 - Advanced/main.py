from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1
        dictionary = {}
        # Loop though each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry where the key is the name
            # of the column and the value is the value of the column.
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2 (same thing just with a dictionary comprehension)
        # return {column.name: getattr(self, column.name) for column in self.__table__columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return jsonify(random_cafe.to_dict()), 200


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    cafes_list_of_dicts = {"cafes": [cafe.to_dict() for cafe in cafes]}
    return jsonify(cafes_list_of_dicts), 200


@app.route("/search")
def search():
    user_search = request.args.get('loc')
    is_all = eval(request.args.get('all'))  # True or False
    if is_all:
        cafes = db.session.query(Cafe).filter_by(location=user_search).all()
        if not cafes:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    cafe = db.session.query(Cafe).filter_by(location=user_search).first()
    return jsonify(cafes=[cafe.to_dict()]), 200


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(int(request.form.get('has_toilet'))),
        has_wifi=bool(int(request.form.get('has_wifi'))),
        has_sockets=bool(int(request.form.get('has_sockets'))),
        can_take_calls=bool(int(request.form.get('can_take_calls'))),
        coffee_price=request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


# https://stackoverflow.com/questions/53611800/how-handle-patch-method-in-flask-route-as-api/53614394
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if not cafe_to_update:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    new_price = request.args.get('new_price')
    cafe_to_update.coffee_price = new_price
    db.session.commit()
    return jsonify(success="Successfully updated the price."), 200


API_KEY = "7ik6hr7i7u65564gg56h7ge5tg"  # Random characters


# HTTP DELETE - Delete Record
@app.route("/delete/<cafe_id>", methods=['DELETE'])  # https://httpstatuses.com/
def delete(cafe_id):
    users_api_key = request.args.get('api-key')
    if not users_api_key == API_KEY:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403
    cafe_to_delete = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if not cafe_to_delete:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return jsonify(success="Successfully deleted the cafe."), 200


if __name__ == '__main__':
    app.run(debug=True)
