#coding: utf-8
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
            'name': unicode,
            'created_at': datetime.datetime,
        },
        'organization': {
            'id': ObjectId,
            'name': unicode
        }
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

    @staticmethod
    def create_student(first_name, middle_name, last_name, group_id):
        student = Student.instance(first_name, middle_name, last_name, group_id)
        Mongo.db.ui.users.insert(student)
        return student

    @staticmethod
    def get_all(sorter='_id', direction=1):
        return Mongo.db.ui.users.Student.find({'_type': 'Student'}).sort(sorter, ASCENDING if int(direction) == 1 else DESCENDING)

    @staticmethod
    def remove(_id):
        Mongo.db.ui.users.remove({'_id': _id})

    @staticmethod
    def update_student(_id, first_name, middle_name, last_name, group_id):
        group = Group.get_by('_id', ObjectId(group_id))
        print(group)
        Mongo.db.ui.users.Student.update(
            {'_id': _id},
            {'$set': {'name.first': first_name,
                      'name.middle': middle_name,
                      'name.last': last_name,
                      'group.id': group_id,
                      'group.name': group.name,
                      'group.created_at': group.created_at,
                      'organization.id': group.organization.id,
                      'organization.name': group.organization.name }}
        )

    @staticmethod
    def get_by(field, value):
        return Mongo.db.ui.users.Student.find_one({field: value})

    def get_course(self):
        return (datetime.datetime.utcnow() - self.created_at).days / 365 + 1
