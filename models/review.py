"""
from extensions import db


# for making the review table in database
class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(1000))
    added_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())

    @classmethod
    def get_by_id(cls, movie_id):
        return cls.query.filter_by(movie_id=movie_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
"""

review_list = []


def get_last_id():
    if review_list:
        last_review = review_list[-1]
    else:
        return 1
    return last_review.id + 1


class Review:
    def __init__(self, movie_id, author, content):
        self.id = get_last_id()
        self.movie_id = movie_id
        self.author = author
        self.content = content

    @property
    def data(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'author': self.author,
            'content': self.content
        }