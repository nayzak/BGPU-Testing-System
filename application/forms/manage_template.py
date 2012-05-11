#coding: utf-8
from wtforms import Form, SubmitField, FieldList, SelectField, FormField, SelectMultipleField
from application.models.question import Question

class CreateTemplateForm(Form):
    title = 'Добавление шаблона теста'

    type = SelectField('Тип вопроса', choices=[("none","Любой"),("asd","asd")])
    subject = SelectField('Предмет', choices=Question.select_subject_choises())
    module = SelectField('Дидактическая единица', choices=Question.select_module_choises())
    complexity = SelectField('Cложность вопроса', choices=Question.select_complexity_choises())
    questions_list = SelectMultipleField('Вопросы', choices=Question.select_questions_choises({'body':1}))
    submit = SubmitField('Добавить шаблон')
