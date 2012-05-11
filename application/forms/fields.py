#coding: utf-8
from wtforms.fields import TextField, FormField
from application.forms.widgets import TypeheadInput, TabbedFieldsWidget
from whirlwind.db.mongo import Mongo


class AutocompleteField(TextField):
    def __init__(self, label=None, validators=None, collection=None, db_field=None, **kwargs):
        super(AutocompleteField, self).__init__(label, validators, **kwargs)
        if collection and db_field:
            self.widget = TypeheadInput(Mongo.db.ui[collection].distinct(db_field))


class TabbedFields(FormField):
    def __init__(self, form_class, tabs=tuple(), label=None, validators=None, separator='-', **kwargs):
        self.tabs = tabs
        kwargs['widget'] = TabbedFieldsWidget()
        super(TabbedFields, self).__init__(form_class, label, validators, separator, **kwargs)
