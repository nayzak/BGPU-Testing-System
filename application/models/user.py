# coding: utf-8
from whirlwind.db.mongo import Mongo
from mongokit import *
import datetime
import hashlib


@Mongo.db.connection.register
class User(Document):
    '''
        name.first - имя
        name.last - фамилия
        name.middle - отчество
        roles - список прав доступа: admin, tutor, student
    '''
    structure = {
        '_type': unicode,
        'name': {
            'first': unicode,
            'last': unicode,
            'middle': unicode
        },
        'email': unicode,
        'password': unicode,
        'roles': list,
        'created_at': datetime.datetime,
        'history': {
            'last_login': datetime.datetime,
            'num_logins': long
        }
    }

    use_dot_notation = True

    required_fields = ['name.first', 'name.last', 'roles']

    @staticmethod
    def get_by(field, value):
        return Mongo.db.ui.users.User.find_one({field: value})

    @staticmethod
    def destroy_session(userid):
        Mongo.db.ui.sessions.remove({'username': userid})

    @staticmethod
    def chpass(_id, password):
        Mongo.db.ui.users.update(
            {'_id': _id},
            {'$set': {'password': hashlib.sha1(password).hexdigest()}}
        )

    def update_history(self):
        self.history.last_login = datetime.datetime.utcnow()
        self.history.num_logins += 1L
        self.save()

    def has_role(self, role):
        return role in self.roles
