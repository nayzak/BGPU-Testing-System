#coding: utf-8
from whirlwind.db.mongo import Mongo
from bson.objectid import ObjectId
from mongokit import *
from pymongo import ASCENDING, DESCENDING

@Mongo.db.connection.register
class Organization(Document):
    '''
        name - сокращенное название (БГПУ)
        full_name - полное название
        status - статус учреждения (суз, вуз, пту и т.п.)
        contacts - список словарей {'country': unicode, 'region': unicode, 'city': unicode, phones: [dict], comment: unicode}
        contacts.phones - список словарей типа {'phone': unicode, 'comment': unicode}
    '''
    structure = {
        'name': unicode,
        'full_name': unicode,
        'status': unicode,
        'contacts': [dict]
    }

    required_fields = ['name', 'full_name', 'status']

    use_dot_notation = True

    @staticmethod
    def instance(name, full_name, status, contacts):
        org = Mongo.db.ui.organizations.Organization()
        org.name = unicode(name)
        org.full_name = unicode(full_name)
        org.status = unicode(status)
        org.contacts = list()
        for cn in contacts:
            contact = {
                'country': cn.get('country', ''),
                'region': cn.get('region', ''),
                'city': cn.get('city', ''),
                'address': cn.get('address', ''),
                'comment': cn.get('comment', ''),
                'phones': list()
            }
            for ph in cn.get('phones', list()):
                contact['phones'].append({
                    'number': ph.get('number', ''),
                    'comment': ph.get('comment', '')
                })
            org.contacts.append(contact)
        return org

    @staticmethod
    def create_organization(name, full_name, status, contacts):
        org = Organization.instance(name, full_name, status, contacts)
        Mongo.db.ui.organizations.insert(org)
        return org

    @staticmethod
    def update_organization(_id, name, full_name, status, contacts):
        Mongo.db.ui.organizations.update(
            {'_id': _id},
            {'$set': {'name': name,
                      'full_name': full_name,
                      'status': status,
                      'contacts': contacts}
            }
        )
        Mongo.db.ui.users.update(
            {'organization.id': _id},
            {'$set': {'organization.name': name}}
        )
        Mongo.db.ui.groups.update(
            {'organization.id': _id},
            {'$set': {'organization.name': name}}
        )

    @staticmethod
    def get_by(field, value):
        return Mongo.db.ui.organizations.Organization.find_one({field: value})

    @staticmethod
    def get_all(sorter='_id', direction=1):
        return Mongo.db.ui.organizations.find().sort(sorter, ASCENDING if int(direction) == 1 else DESCENDING)

    @staticmethod
    def remove(_id):
        Mongo.db.ui.organizations.remove({'_id': _id})

    @staticmethod
    def select_field_choises(blank_element=True):
        choises = map(lambda d: (unicode(d['_id']), d['name']), Mongo.db.ui.organizations.find().sort('name', ASCENDING))
        if blank_element:
            choises.insert(0, ('0', 'Выберите учебное заведение'))
        return choises
