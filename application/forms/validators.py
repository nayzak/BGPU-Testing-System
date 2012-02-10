from wtforms.validators import StopValidation
from whirlwind.db.mongo import Mongo
import hashlib


class ExistsInDb(object):
    def __init__(self, collection, doc_field, message=None):
        self.message = message
        self.collection = collection
        self.doc_field = doc_field

    def __call__(self, form, field):
        doc = Mongo.db.ui[self.collection].find_one({self.doc_field: field.data})
        if doc is None:
            if self.message is None:
                    self.message = field.gettext(u'There is no such document in database')
            field.errors[:] = []
            raise StopValidation(self.message)


class NotExistInDb(ExistsInDb):
    def __call__(self, form, field):
        doc = Mongo.db.ui[self.collection].find_one({self.doc_field: field.data})
        if doc is not None:
            if self.message is None:
                    self.message = field.gettext(u'There is already such document in database')
            field.errors[:] = []
            raise StopValidation(self.message)


class Authorized(object):
    def __init__(self, collection, doc_login_field, form_login_field, message=None):
        self.collection = collection
        self.doc_login_field = doc_login_field
        self.form_login_field = form_login_field
        self.message = message

    def __call__(self, form, field):
        doc = Mongo.db.ui[self.collection].find_one({self.doc_login_field: form[self.form_login_field].data})
        if doc is None:
            field.errors[:] = []
            raise StopValidation(field.gettext(u'User not found.'))
        password = hashlib.sha1(field.data).hexdigest()
        if doc['password'] != password:
            if self.message is None:
                    self.message = field.gettext(u'Password is incorrect.')
            field.errors[:] = []
            raise StopValidation(self.message)


exists_in_db = ExistsInDb
not_exist_in_db = NotExistInDb
authorized = Authorized
