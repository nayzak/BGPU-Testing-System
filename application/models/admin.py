# coding: utf-8
from application.models.user import User
from whirlwind.db.mongo import Mongo
import datetime
import hashlib
from lib import mail


@Mongo.db.connection.register
class Admin(User):
    required_fields = ['email', 'password']

    default_values = {'roles': ['admin']}

    @staticmethod
    def is_admin_created():
        if Mongo.db.ui.users.Admin.find_one() is None:
            return False
        else:
            return True

    @staticmethod
    def create_admin(first_name, last_name, middle_name, email, password):
        admin = Admin()
        admin.name.first = first_name
        admin.name.last = last_name
        admin.name.middle = middle_name
        admin.email = email
        admin.password = hashlib.sha1(password).hexdigest()
        admin.created_at = datetime.datetime.utcnow()
        admin.history.num_logins = 0

        Mongo.db.ui.users.insert(admin)

        mail.sendmail(
            admin.email.encode('utf-8'),
            ' '.join([admin.name.last, admin.name.first, admin.name.middle]).encode('utf-8'),
            'Уведомление о регистрации',
            'Вы успешно зарегистрированы как администратор системы тестирования.'
        )
