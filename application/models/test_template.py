from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId
from pymongo import *
import datetime


@Mongo.db.connection.register
class TestTemplate(Document):
    structure = {
        'title': unicode,
        'description': unicode,
        'questions': [ObjectId],
        'author_id': ObjectId,
        'created_at': datetime.datetime,
        'history': [dict]  # editor_id:ObjectId, modify_date:datetime, comment:unicode
    }

    required_fields = ['title', 'questions', 'author_id']

    use_dot_notations = True
