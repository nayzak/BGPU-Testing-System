#coding: utf-8
from wtforms import Form, TextField, SubmitField, SelectField, validators, HiddenField
from application.forms.validators import not_exist_in_db, authorized
from application.models.group import Group


class CreateStudentForm(Form):
    title = 'Регистрация студента'

    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    group_id = SelectField('Группа', choices=Group.select_field_choises())
    submit = SubmitField('Добавить студента')

class EditStudentForm(Form):
    title = 'Редактирование профиля студента'

    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    group_id = SelectField('Группа', choices=Group.select_field_choises())
    userid = HiddenField()
    submit = SubmitField('Сохранить')

