from application.models.user import User
from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING
from application.models.group import Group
import datetime
import hashlib


@Mongo.db.connection.register
class Student(User):
    structure = {
        'group': {
            'id': ObjectId,
            'name': unicode
        },
        'organization': {
            'id': ObjectId,
            'name': unicode
        },
        'course': unicode
    }

    required_fields = ['group']

    default_values = {'roles': ['student']}

    @staticmethod
    def instance(first_name, middle_name, last_name, group_id):
        student = Student()
        student.name.first = first_name
        student.name.middle = middle_name
        student.name.last = last_name
        try:
            group_id = ObjectId(group_id.decode('hex'))
            group = Group.get_by('_id', group_id)
            student.course = group.get_course()
            student.group.id = group_id
            student.group.name = group.name
            student.organization.id = group.organization.id
            student.organization.name = group.organization.name
        except:
            student.group = dict()
            student.organization = dict()
        student.created_at = datetime.datetime.utcnow()
        student.history.num_logins = 0
        return student

    @staticmethod
    def create_student(first_name, middle_name, last_name, group_id):
        student = Student.instance(first_name, middle_name, last_name, group_id)
        Mongo.db.ui.users.insert(student)
        return student

    @staticmethod
    def get_all(sorter='_id', direction=1):
        return Mongo.db.ui.users.find({'_type': 'Student'}).sort(sorter, ASCENDING if int(direction) == 1 else DESCENDING)

    @staticmethod
    def remove(_id):
        Mongo.db.ui.users.remove({'_id': _id})
