#coding: utf-8
from wtforms import Form, SelectField, SubmitField, BooleanField, DateTimeField
from wtforms import validators
from application.forms.fields import AutocompleteField
from application.models.organization import Organization


class CreateGroupForm(Form):
    title = 'Добавление группы'

    organization = SelectField('Учебное заведение', [validators.required()], choices=Organization.select_field_choises(False))
    created_at = DateTimeField('Дата организации', [validators.required()], format='%Y-%m-%d', description='Пример: 2007-09-01')
    name = AutocompleteField('Название', [validators.required()], 'groups', 'name', description='Название группы без обозначения курса. Например: A, но не 3A.')
    profession = AutocompleteField('Специальность', [validators.required()], 'groups', 'profession')
    graduated = BooleanField('Выпуск', description='Отметить, если группа выпустилась.')
    submit = SubmitField('Добавить группу')


class EditGroupForm(CreateGroupForm):
    title = 'Редактирование группы'
    submit = SubmitField('Сохранить')
