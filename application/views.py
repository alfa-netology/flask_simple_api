from flask import request, jsonify
from flask.views import MethodView

from application import db
from application.errors import bad_request
from application.models import User, Ad

class UserView(MethodView):
    @staticmethod
    def get(user_id):
        user = User.query.get(user_id)
        if not user:
            return bad_request('user not found')
        user = user.to_dict()
        return user

    @staticmethod
    def post():
        data = request.json
        if 'username' not in data or 'email' not in data or 'password' not in data:
            return bad_request('must include username, email and password fields')
        if User.query.filter_by(username=data['username']).first():
            return bad_request('please use a different username')
        if User.query.filter_by(email=data['email']).first():
            return bad_request('please use a different email address')
        user = User()
        user.from_dict(data, new_user=True)
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

class AdView(MethodView):
    @staticmethod
    def get(ad_id):
        ad = Ad.query.get(ad_id)
        if not ad:
            return bad_request('ad not found')
        return ad.to_dict()

    @staticmethod
    def post():
        data = request.json
        if 'title' not in data or 'text' not in data or 'user_id' not in data:
            return bad_request('must include title, text and user_id fields')
        if not User.query.filter_by(id=data['user_id']).first():
            return bad_request('no such user id')
        ad = Ad()
        ad.from_dict(data)
        db.session.add(ad)
        db.session.commit()
        response = jsonify(ad.to_dict())
        response.status_code = 201
        return response

    @staticmethod
    def put(ad_id):
        ad = Ad.query.get(ad_id)
        data = request.json
        if not ad:
            bad_request('ad not found')
        ad.from_dict(data)
        db.session.commit()
        return ad.to_dict()

    @staticmethod
    def delete(ad_id):
        ad = Ad.query.get(ad_id)
        if not ad:
            return bad_request('nothing to delete')
        db.session.delete(ad)
        db.session.commit()
        return jsonify({
            'status_code': 204,
            'message': 'ad successfully deleted'
        })
