from application.models.user import User
from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId


@Mongo.db.connection.register
class Student(User):
    structure = {
        'group_id': ObjectId
    }

    required_fields = ['group_id']

    default_values = {'roles': ['student']}
