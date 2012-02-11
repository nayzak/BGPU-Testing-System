# coding: utf-8
from wtforms.form import WebobInputWrapper
from wtforms import TextField, FieldList, Form, FormField, SubmitField, validators


class PhoneForm(Form):
    phone = TextField('Телефон')
    comment = TextField('Комментарий')


class ContactForm(Form):
    country = TextField('Страна')
    region = TextField('Область')
    city = TextField('Город')
    comment = TextField('Комментарий')
    phones = FieldList(FormField(PhoneForm), min_entries=2)


class CreateOrganizationForm(Form):
    title = 'Добавление учебного заведения'

    name = TextField('Название')
    fullname = TextField('Полное название')
    status = TextField('Статус')
    contacts = FieldList(FormField(ContactForm), min_entries=1)
    submit = SubmitField('Добавить')

    def process(self, formdata=None, obj=None, **kwargs):
        if formdata is not None and not hasattr(formdata, 'getlist'):
            if hasattr(formdata, 'getall'):
                formdata = WebobInputWrapper(formdata)
            else:
                raise TypeError("formdata should be a multidict-type wrapper that supports the 'getlist' method")

        for name, field, in self._fields.iteritems():
            if obj is not None and hasattr(obj, name):
                field.process(formdata, getattr(obj, name))
            elif name in kwargs:
                field.process(formdata, kwargs[name])
            else:
                field.process(formdata)

        enclosures = {k: v for k, v in kwargs.items() if '-' in k}
        for key, val in enclosures.items():
            k = key.split('-')
            print self[k[0]]
