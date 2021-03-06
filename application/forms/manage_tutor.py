#coding: utf-8
from wtforms import Form, TextField, PasswordField, SubmitField, HiddenField, SelectField, validators
from application.forms.validators import not_exist_in_db, authorized
from application.models.organization import Organization


class CreateTutorForm(Form):
    title = 'Регистрация преподавателя'

    email = TextField('E-mail', [validators.required(), validators.email(), not_exist_in_db('users', 'email', 'Пользователь с таким email уже существует.')], description='E-mail будет использован в качестве логина.')
    password = PasswordField('Пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField('Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    position = TextField('Должность', description='Должность, регалии.')
    organization = SelectField('Учебное заведение', choices=Organization.select_field_choises())
    submit = SubmitField('Добавить преподавателя')


class EditTutorForm(Form):
    title = 'Редактирование профиля преподавателя'

    email = TextField('E-mail', [validators.required(), validators.email()])
    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    position = TextField('Должность', description='Должность, регалии.')
    organization = SelectField('Учебное заведение', choices=Organization.select_field_choises())
    password = PasswordField('Пароль', [validators.required(), authorized('users', '_id', 'userid', message='Неверный пароль')])
    userid = HiddenField()
    submit = SubmitField('Сохранить')


class ChpassForm(Form):
    title = 'Смена пароля'

    oldpass = PasswordField('Текущий пароль', [validators.required(), authorized('users', '_id', 'userid', message='Неверный пароль')])
    password = PasswordField('Новый пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField('Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    userid = HiddenField()
    submit = SubmitField('Сменить пароль')


class AdminChpassForm(Form):
    title = 'Смена пароля'

    password = PasswordField('Новый пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField('Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    submit = SubmitField('Сменить пароль')
