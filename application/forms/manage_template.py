#coding: utf-8
from wtforms import Form, SubmitField, SelectField
from application.models.question import Question

class CreateTemplateForm(Form):
    title = 'Добавление шаблона теста'

    type_question = SelectField('Тип вопроса', choices=list())
    subject = SelectField('Предмет', choices=Question.select_subject_choises())
    module = SelectField('Дидактическая единица', choices=Question.select_module_choises())
    complexity = SelectField('Cложность вопроса', choices=Question.select_complexity_choises())
    submit = SubmitField('Добавить шаблон')
