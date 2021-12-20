from application import db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    ads = db.relationship('Ad', backref='author', lazy='dynamic')

    @staticmethod
    def to_collection_dict(query):
        users = query.all()
        data = {
            'users': [user.to_dict() for user in users]
        }
        return data

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data.get('password'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=date.today)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'created_at': self.created_at,
            'user_id': self.user_id,
        }
        return data

    def from_dict(self, data):
        for field in ['title', 'text', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return f'<Ad: <Title:{self.title}>>'

