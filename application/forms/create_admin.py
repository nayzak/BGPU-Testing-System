# coding: utf-8
from wtforms import Form, TextField, PasswordField, SubmitField, validators


class CreateAdminForm(Form):
    title = 'Регистрация администратора'

    email = TextField('E-mail', [validators.required(), validators.email()], description='E-mail будет использован в качестве логина')
    password = PasswordField('Пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField('Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    submit = SubmitField('Создать администратора')
