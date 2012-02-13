#coding: utf-8
from whirlwind.db.mongo import Mongo
from mongokit import *


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
    def create_organization(name, fullname, status, contacts):
        org = Organization()
        org.name = name
        org.full_name = fullname
        org.status = status
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

        Mongo.db.ui.organizations.insert(org)

        return org
