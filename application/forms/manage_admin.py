# coding: utf-8
from wtforms import Form, TextField, PasswordField, SubmitField, HiddenField, validators
from application.forms.validators import authorized


class CreateAdminForm(Form):
    title = 'Регистрация администратора'

    email = TextField('E-mail', [validators.required(), validators.email()], description='E-mail будет использован в качестве логина')
    password = PasswordField('Пароль', [validators.required(), validators.length(min=6)])
    password_confirmation = PasswordField('Подтвердите пароль', [validators.required(), validators.equal_to('password')])
    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    submit = SubmitField('Создать администратора')


class EditAdminForm(Form):
    title = 'Редактирование профиля администратора'

    email = TextField('E-mail', [validators.required(), validators.email()])
    last_name = TextField('Фамилия', [validators.required()])
    first_name = TextField('Имя', [validators.required()])
    middle_name = TextField('Отчество', [validators.required()])
    password = PasswordField('Пароль', [validators.required(), authorized('users', '_id', 'userid', message='Неверный пароль')])
    userid = HiddenField()
    submit = SubmitField('Сохранить')
