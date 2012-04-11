from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId
from pymongo import *
import datetime
from lib.utils import Solution


@Mongo.db.connection.register
class Question(Document):
    '''
        position.subject - предмет
        position.module - дидактическая единица
        body - содержание вопроса
        type - тип вопроса. С типами еще определиться надо.
        solution - правильный ответ
        complexity - сложность вопроса
        history - список словарей типа {editor_id: ObjectId, modified_date: datetime.datetime, comment: unicode}

        db.question.insert({'position':{'subject':'matan', 'module':'intergal'}, 'body':'kak etu huetu reshat', 'solution':'asdasgasgrh4rh4y', 'complexity':100500, 'author_id':ObjectId("4f41cdc9b2c79a182e000000"), 'created_at':ISODate("2011-09-01T00:00:00Z"), 'history':{'editor_id': ObjectId("4f41cdc9b2c79a182e000000"), 'modified_date': ISODate("2011-09-01T00:00:00Z"), 'comment': 'trororlororl'} })

    '''
    structure = {
        'position': {
            'subject': unicode,
            'module': unicode
        },
        'body': unicode,
        'solution': Solution,
        'complexity': int,
        'author_id': ObjectId,
        'created_at': datetime.datetime,
        'history': [dict]
    }

    required_fields = ['position', 'position.subject', 'position.module', 'body', 'solution', 'complexity', 'author_id']

    use_dot_notation = True
