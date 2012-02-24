#coding: utf-8
from wtforms import Form, TextField, SubmitField, SelectField, validators, HiddenField
from application.forms.validators import not_exist_in_db, authorized
from application.models.group import Group
from application.models.organization import Organization


class CreateStudentForm(Form):
    title = 'Регистрация студента'

    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    organization_id  = SelectField('Учебное заведение', choices=Organization.select_field_choises())
    group_id = SelectField('Группа', choices=Group.select_field_choises())
    submit = SubmitField('Добавить студента')

class EditStudentForm(CreateStudentForm):
    title = 'Редактирование профиля студента'

    #group_id = SelectField('Группа', choices=Group.select_field_choises(organization_id))
    submit = SubmitField('Сохранить')
