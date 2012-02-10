# coding: utf-8
from wtforms import Form, TextField, PasswordField, BooleanField, SubmitField, validators
from application.forms.validators import exists_in_db, authorized


class LoginForm(Form):
    title = 'Вход в панель управления'

    email = TextField('E-mail', [validators.required(), validators.email(), exists_in_db('users', 'email', message='Пользователь с таким email не найден')])
    password = PasswordField('Пароль', [validators.required(), authorized('users', 'email', 'email', message='Неверно введен пароль.')])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
