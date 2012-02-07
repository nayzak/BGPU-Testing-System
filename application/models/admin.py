from application.models.user import User
from whirlwind.db.mongo import Mongo


@Mongo.db.connection.register
class Admin(User):
    required_fields = ['email', 'password']

    default_values = {'roles': ['admin']}
