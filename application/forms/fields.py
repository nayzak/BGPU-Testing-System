from wtforms import TextField
from application.forms.widgets import TypeheadInput
from whirlwind.db.mongo import Mongo


class AutocompleteField(TextField):
    def __init__(self, label=None, validators=None, collection=None, db_field=None, **kwargs):
        super(AutocompleteField, self).__init__(label, validators, **kwargs)
        if collection and db_field:
            self.widget = TypeheadInput(Mongo.db.ui[collection].distinct(db_field))
