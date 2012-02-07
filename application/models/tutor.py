from application.models.user import User
from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId


@Mongo.db.connection.register
class Tutor(User):
    '''
        position - должность, регалии
    '''
    structure = {
        'position': unicode,
        'organization_id': ObjectId
    }
    required_fields = ['email', 'password']

    default_values = {'roles': ['tutor']}
