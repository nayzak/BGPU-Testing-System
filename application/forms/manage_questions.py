#coding: utf-8
from wtforms import Form, SubmitField, TextField, FieldList, FormField, validators
from application.forms.fields import TabbedFields
from application.forms.widgets import FieldListWidget


class QuestionSolutionMap(Form):
    class_ = 'form-inline'

    key = TextField(label='Ключ')
    value = TextField(label='Значение')

class QuestionSolution(Form):
    one_answer = TextField(label='Ответ')
    some_answers = FieldList(TextField(label='Вариант ответа'), min_entries=1, widget=FieldListWidget())
    map_answer = FieldList(FormField(QuestionSolutionMap), min_entries=1, widget=FieldListWidget())
    append_answer = TextField()


class CreateQuestionForm(Form):
    title = 'Добавление вопроса'

    solution = TabbedFields(QuestionSolution, label='Ответ', tabs=('Один вариант', 'Несколько вариантов', 'Соответствие', 'Фраза'))
    submit = SubmitField('Добавить вопрос')
