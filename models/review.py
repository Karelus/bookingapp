from extensions import db

review_list = []


def get_last_id():
    if review_list:
        last_review = review_list[-1]
    else:
        return 1
    return last_review.id + 1


# for making the review table in database
class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    added_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))


"""
    @classmethod
    def get_by_id(cls, movie_id):
        return cls.query.filter_by(movie_id=movie_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
"""