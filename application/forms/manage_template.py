#coding: utf-8
from wtforms import Form, SubmitField

class CreateTemplateForm(Form):
    title = 'Добавление шаблона теста'

    submit = SubmitField('Добавить шаблон')
