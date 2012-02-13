# coding: utf-8
from wtforms import TextField, FieldList, Form, FormField, SubmitField, validators
from application.forms.fields import AutocompleteField


class PhoneForm(Form):
    class_ = 'form-inline'

    number = TextField('Номер', [validators.required()])
    comment = TextField('Комментарий')


class ContactForm(Form):
    class_ = 'form-inline well'

    country = AutocompleteField('Страна', [validators.required()], collection='organizations', db_field='contacts.country')
    region = AutocompleteField('Область', [validators.required()], collection='organizations', db_field='contacts.region')
    city = AutocompleteField('Город', [validators.required()], collection='organizations', db_field='contacts.city')
    address = TextField('Адрес')
    comment = TextField('Комментарий')
    phones = FieldList(FormField(PhoneForm), label='Телефон')


class CreateOrganizationForm(Form):
    title = 'Добавление учебного заведения'

    name = TextField('Название', [validators.required()], description='Аббревиатура')
    fullname = TextField('Полное название', [validators.required()])
    status = AutocompleteField('Статус', [validators.required()], collection='organizations', db_field='status', description='Например, вуз, суз')
    contacts = FieldList(FormField(ContactForm), label='Адрес')
    submit = SubmitField('Добавить')
