#coding: utf-8
from wtforms import Form, SubmitField, FieldList, SelectField, FormField, SelectMultipleField, TextField, TextAreaField
from application.models.question import Question
#from application.forms.widgets import ButtonWidget
from application.forms.widgets import *

class ButtonTemplteForm(Form):
    class_= 'form-inline'

class CreateTemplateForm(Form):
    title = 'Добавление шаблона теста'

    template_title = TextField(label = 'Название шаблона')
    description = TextAreaField(label = 'Описание')
    type = SelectField('Тип вопроса', choices=[("none","Любой"),("asd","asd")])
    subject = SelectField('Предмет', choices=Question.select_subject_choises())
    module = SelectField('Дидактическая единица', choices=Question.select_module_choises())
    complexity = SelectField('Cложность вопроса', choices=Question.select_complexity_choises())
    questions_list = SelectMultipleField('Вопросы', choices=Question.select_questions_choises({'body':1}))
    buttonAdd = FieldList(FormField(ButtonTemplteForm), label = ' ', min_entries=1, widget=ButtonWidget(label = 'добавить', _id = 'buttonAdd'))
    buttonDelete = FieldList(FormField(ButtonTemplteForm), label = ' ', min_entries=1, widget=ButtonWidget(label = 'удалить', _id = 'buttonDelete'))
    made_list = SelectMultipleField('Вопросы для добавления', choices=[])
    submit = SubmitField('Добавить шаблон')
