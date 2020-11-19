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

    @classmethod
    def get_all_movies(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_by_id(cls, movie_id):
        return cls.query.filter_by(id=movie_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
