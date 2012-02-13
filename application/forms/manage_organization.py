# coding: utf-8
from wtforms import TextField, FieldList, Form, FormField, SubmitField, validators


class PhoneForm(Form):
    class_ = 'form-inline'

    number = TextField('Номер', [validators.required()])
    comment = TextField('Комментарий')


class ContactForm(Form):
    class_ = 'form-inline well'

    country = TextField('Страна', [validators.required()])
    region = TextField('Область', [validators.required()])
    city = TextField('Город', [validators.required()])
    address = TextField('Адрес')
    comment = TextField('Комментарий')
    phones = FieldList(FormField(PhoneForm), label='Телефон')


class CreateOrganizationForm(Form):
    title = 'Добавление учебного заведения'

    name = TextField('Название', [validators.required()])
    fullname = TextField('Полное название', [validators.required()])
    status = TextField('Статус', [validators.required()])
    contacts = FieldList(FormField(ContactForm), label='Адрес')
    submit = SubmitField('Добавить')
