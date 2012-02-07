from whirlwind.db.mongo import Mongo
from pymongo import *
import datetime


@Mongo.db.connection.register
class Group(Document):
    '''
        profession - специальность (МО)
        created_at - дата образования группы
        current_name - текущее название группы (3А, через год надо поменять на 4А)
        current_course - текущий курс. Скорее всего не пригодится
        graduated - выпустилась ли группа
    '''
    structure = {
        'profession': unicode,
        'created_at': datetime.datetime,
        'current_name': unicode,
        'current_course': int,
        'graduated': bool
    }

    required_fields = ['profession', 'created_at', 'current_course', 'current_name', 'graduated']

    default_values = {'graduated': False}

    use_dot_notation = True
