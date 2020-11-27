from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_optional, get_jwt_identity, jwt_required
from http import HTTPStatus

from utils import hash_password
from models.user import User

from schemas.user import UserSchema

user_schema = UserSchema()
user_public_schema = UserSchema(exclude=('email', ))


class UserListResource(Resource):
    # for creating an user, password is hashed to the database
    def post(self):
        json_data = request.get_json()

        data, errors = user_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        if User.get_by_username(data.get('username')):
            return {'message': 'username already in use'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(data.get('email')):
            return {'message': 'email already in use'}, HTTPStatus.BAD_REQUEST

        user = User(**data)
        user.save()

        return user_schema.dump(user).data, HTTPStatus.CREATED


class UserResource(Resource):

    # for getting on info, shows also email if logged in
    # and is_admin if user is admin
    @jwt_optional
    def get(self, username):

        user = User.get_by_username(username=username)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user == user.id:
            data = user_schema.dump(user).data

        else:
            data = user_public_schema.dump(user).data

        return data, HTTPStatus.OK

    # for user deletion, only admin
    @jwt_required
    def delete(self, username):

        identity = get_jwt_identity()
        current_user = User.get_by_id(identity)

        if not current_user.is_admin:
            return {'message': 'Not authorized'}, HTTPStatus.UNAUTHORIZED

        user = User.get_by_username(username=username)

        if User is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        user.delete()

        return {'message': 'user successfully deleted!'}, HTTPStatus.OK


# for getting own information when logged in
class MeResource(Resource):

    @jwt_required
    def get(self):

        user = User.get_by_id(id=get_jwt_identity())
        return user_schema.dump(user).data, HTTPStatus.OK


class AdminResource(Resource):

    # updating user to admin
    @jwt_required
    def put(self):

        user = User.get_by_id(id=get_jwt_identity())

        user.is_admin = True
        user.save()

        return {'message': 'You are now admin'}, HTTPStatus.OK
