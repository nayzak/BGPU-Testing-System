from whirlwind.db.mongo import Mongo
from pymongo import *


@Mongo.db.connection.register
class Organization(Document):
    '''
        name - сокращенное название (БГПУ)
        full_name - полное название
        status - статус учреждения (суз, вуз, пту и т.п.)
        contacts.phones - список словарей типа {'phone': unicode, 'comment': unicode}
    '''
    structure = {
        'name': unicode,
        'full_name': unicode,
        'status': unicode,
        'contacts': {
            'country': unicode,
            'region': unicode,
            'city': unicode,
            'address': unicode,
            'phones': [dict]
        }
    }

    required_fields = ['name', 'full_name', 'status']

    use_dot_notation = True