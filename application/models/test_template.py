from whirlwind.db.mongo import Mongo
from bson.objectid import ObjectId
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

    @staticmethod
    def instance(title, description, questions, author_id, created_at, history):
        student = Student()
        student.name.first = first_name
        student.name.middle = middle_name
        student.name.last = last_name
        try:
            group_id = ObjectId(group_id.decode('hex'))
            group = Group.get_by('_id', group_id)
            student.group.id = group_id
            student.group.name = group.name
            student.group.created_at = group.created_at
            student.organization.id = group.organization.id
            student.organization.name = group.organization.name
        except:
            student.group = dict()
            student.organization = dict()
        student.created_at = datetime.datetime.utcnow()
        student.history.num_logins = 0
        return student
