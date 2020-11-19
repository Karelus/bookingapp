from extensions import db


# for making the review table in database
class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    added_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    movie_id = db.Column(db.Integer, nullable=False)
    is_publish = db.Column(db.Boolean(), default=False)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def data(self):
        return {
            'id': self.id,
            'content': self.content,
            'movie_id': self.movie_id,
            'author_id': self.author_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, review_id):
        return cls.query.filter_by(id=review_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
