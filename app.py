"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'its-a-secret'

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route("/api/cupcakes")
def list_cupcakes():
    """ Gets data about all cupcakes """

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """ Get data about a single cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """ Create a cupcake with flavor, size, rating 
    and image data from the body of the request.
    """

    data = request.json
    flavor = data["flavor"]
    size = data["size"]
    rating = data["rating"]
    image = data["image"] or None

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)