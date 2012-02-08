# coding: utf-8
from whirlwind.db.mongo import Mongo
from mongokit import *
import datetime


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
