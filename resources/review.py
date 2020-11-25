from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus

from models.review import Review
from models.movie import Movie


class ReviewListResource(Resource):

    # for getting all reviews
    def get(self):

        reviews = Review.get_all_published()
        
        data = []

        for review in reviews:
            data.append(review.data())

        return {'data': data}, HTTPStatus.OK

    # for creating a new review
    @jwt_required
    def post(self):

        json_data = request.get_json()
        current_user = get_jwt_identity()
        review = Review(movie_id=json_data['movie_id'],
                        content=json_data['content'],
                        author_id=current_user)

        review.save()

        return review.data(), HTTPStatus.CREATED


class ReviewResource(Resource):

    # for getting a specific review
    def get(self, review_id):

        review = Review.get_by_id(review_id=review_id)

        if review is None:
            return {'message': 'review not found'}, HTTPStatus.NOT_FOUND

        return review.data(), HTTPStatus.OK

    # for updating a review, can only be done by user who created it
    @jwt_required
    def put(self, review_id):
        json_data = request.get_json()

        review = Review.get_by_id(review_id=review_id)

        if review is None:
            return {'message': 'review not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != review.author_id:
            return {'message': 'Only user who created this can update it!'}, HTTPStatus.FORBIDDEN

        review.content = json_data['content']
        review.movie_id = json_data['movie_id']

        review.save()

        return review.data(), HTTPStatus.OK

    # for deleting a review, can only be done by user who created it
    @jwt_required
    def delete(self, review_id):

        review = Review.get_by_id(review_id=review_id)

        if review is None:
            return {'message': 'review not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != review.author_id:
            return {'message': 'Only user who created this can delete it!'}, HTTPStatus.FORBIDDEN

        review.delete()

        return {'message': 'deleted successfully'}, HTTPStatus.OK


class ReviewPublishResource(Resource):

    # for publishing a review, can only be done by user who created it
    @jwt_required
    def put(self, review_id):
        review = Review.get_by_id(review_id=review_id)

        if review is None:
            return {'message': 'review not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != review.author_id:
            return {'message': 'Only user who created this can publish it!'}, HTTPStatus.FORBIDDEN

        review.is_publish = True

        review.save()

        return {'message': 'review published'}, HTTPStatus.OK

    # for unpublishing a review, can only be done by user who created it
    @jwt_required
    def delete(self, review_id):
        review = Review.get_by_id(review_id=review_id)

        if review is None:
            return {'message': 'review not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != review.author_id:
            return {'message': 'Only user who created this can unpublish it!'}, HTTPStatus.FORBIDDEN

        review.is_publish = False

        review.save()

        return {'message': 'review deleted'}, HTTPStatus.OK
