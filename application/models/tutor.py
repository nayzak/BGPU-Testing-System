#coding: utf-8
from application.models.user import User
from application.models.organization import Organization
from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING
import hashlib
import datetime


@Mongo.db.connection.register
class Tutor(User):
    '''
        position - должность, регалии
    '''
    structure = {
        'position': unicode,
        'organization': {
            'id': ObjectId,
            'name': unicode
        }
    }
    required_fields = ['email', 'password']

    default_values = {'roles': ['tutor']}

    @staticmethod
    def instance(first_name, middle_name, last_name, email, password, position='', organization_id=u''):
        tutor = Tutor()
        tutor.name.first = first_name
        tutor.name.middle = middle_name
        tutor.name.last = last_name
        tutor.email = email
        tutor.password = hashlib.sha1(password).hexdigest()
        tutor.position = position
        try:
            organization_id = ObjectId(organization_id.decode('hex'))
            tutor.organization.id = organization_id
            tutor.organization.name = Organization.get_by('_id', organization_id).name
        except:
            tutor.organization = dict()
        tutor.created_at = datetime.datetime.utcnow()
        tutor.history.num_logins = 0
        return tutor

    @staticmethod
    def create_tutor(first_name, middle_name, last_name, email, password, position='', organization_id=0):
        tutor = Tutor.instance(first_name, middle_name, last_name, email, password, position, organization_id)
        Mongo.db.ui.users.insert(tutor)
        return tutor

    @staticmethod
    def update_tutor(_id, first_name, middle_name, last_name, email, position='', organization_id=0):
        organization = dict()
        try:
            organization_id = ObjectId(organization_id.decode('hex'))
            organization['id'] = organization_id
            organization['name'] = Organization.get_by('_id', organization_id).name
        except:
            pass
        Mongo.db.ui.users.update(
            {'_id': _id},
            {'$set': {'name.first': first_name,
                      'name.middle': middle_name,
                      'name.last': last_name,
                      'email': email,
                      'position': position,
                      'organization': organization}}
        )

    @staticmethod
    def get_by(field, value):
        return Mongo.db.ui.users.Tutor.find_one({field: value})

    @staticmethod
    def get_all(sorter='_id', direction=1):
        return Mongo.db.ui.users.find({'_type': 'Tutor'}).sort(sorter, ASCENDING if int(direction) == 1 else DESCENDING)

    @staticmethod
    def remove(_id):
        Mongo.db.ui.users.remove({'_id': _id})
