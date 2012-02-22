#coding: utf-8
from wtforms import Form, TextField, PasswordField, SubmitField, HiddenField, SelectField, validators
from application.forms.validators import not_exist_in_db, authorized
from application.models.group import Group


class CreateStudentForm(Form):
    title = 'Регистрация студента'

    email = TextField('E-mail', [validators.required(), validators.email(), not_exist_in_db('users', 'email', 'Пользователь с таким email уже существует.')], description='E-mail будет использован в качестве логина.')
    password = PasswordField('Пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField('Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    group_id = SelectField('Группа', choices=Group.select_field_choises())
    submit = SubmitField('Добавить студента')
