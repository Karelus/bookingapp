
"""
from extensions import db


# for making the movie table in database
class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    description = db.Column(db.String(1000))
    director = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    age_rating = db.Column(db.Integer, nullable=False)
    added_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
"""

movie_list = []


def get_last_id():
    if movie_list:
        last_movie = movie_list[-1]
    else:
        return 1
    return last_movie.id + 1


class Movie:
    def __init__(self, name, year, rating, description, director, duration, age_rating):
        self.id = get_last_id()
        self.name = name
        self.year = year
        self.rating = rating
        self.description = description
        self.director = director
        self.duration = duration
        self.age_rating = age_rating

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'rating': self.rating,
            'description': self.description,
            'director': self.director,
            'duration': self.duration,
            'age_rating': self.age_rating
        }