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
    full_name = TextField('Полное название', [validators.required()])
    status = AutocompleteField('Статус', [validators.required()], collection='organizations', db_field='status', description='Например: вуз, суз')
    contacts = FieldList(FormField(ContactForm), label='Адрес')
    submit = SubmitField('Добавить')

    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        super(CreateOrganizationForm, self).__init__(formdata, obj, prefix, **kwargs)
        #Если форма создавалась в методе get, то добавляем поле адреса и телефона
        import traceback
        if traceback.extract_stack()[-3][2] == 'get':
            if not len(self.contacts):
                self.contacts.append_entry()
            if not len(self.contacts.entries[0].phones):
                self.contacts.entries[0].phones.append_entry()


class EditOrganizationForm(CreateOrganizationForm):
    title = 'Редактирование учебного заведения'

    submit = SubmitField('Сохранить')