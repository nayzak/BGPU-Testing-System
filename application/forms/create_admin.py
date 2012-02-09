# coding: utf-8
from wtforms import Form, TextField, PasswordField, SubmitField, validators


class CreateAdminForm(Form):
    title = u'Регистрация администратора'

    email = TextField(u'E-mail', [validators.required(), validators.email()], description=u'E-mail будет использован в качестве логина')
    password = PasswordField(u'Пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField(u'Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    last_name = TextField(u'Фамилия', [validators.required()])
    first_name = TextField(u'Имя', [validators.required()])
    middle_name = TextField(u'Отчество', [validators.required()])
    submit = SubmitField(u'Создать администратора')
