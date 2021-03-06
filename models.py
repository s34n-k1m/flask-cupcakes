"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_CUPCAKE_IMG = "https://tinyurl.com/demo-cupcake"


class Cupcake(db.Model):
    """ Cupcake model """

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    flavor = db.Column(
        db.Text,
        nullable=False)

    size = db.Column(
        db.Text,
        nullable=False)

    rating = db.Column(
        db.Integer,
        nullable=False)

    image = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_CUPCAKE_IMG)

    def __repr__(self):
        return f"Cupcake id={self.id} flavor={self.flavor} size={self.size} rating={self.rating}"

    def serialize(self):
        """ Serialize to dictionary """

        # TODO: can we go through the keys programmatically?
        # When dealing with APIs, never loop through all the columns
        # return { 
        #     k: v for k,v in [self.__dict__.items()] 
        #     if k != '_sa_instance_state'}
        # Instead loop through a list of the keys/columns




        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
