#coding: utf-8
from wtforms import Form, SubmitField, TextField, FieldList, FormField, validators
from application.forms.fields import TabbedFields
from application.forms.widgets import FieldListWidget


class QuestionSolutionMap(Form):
    class_ = 'form-inline'

    key = TextField()
    value = TextField()


class QuestionSolution(Form):
    one_answer = TextField()
    some_answers = FieldList(TextField(), min_entries=1, widget=FieldListWidget())
    map_answer = FieldList(FormField(QuestionSolutionMap), min_entries=1, widget=FieldListWidget())
    append_answer = TextField()


class CreateQuestionForm(Form):
    title = 'Добавление вопроса'

    solution = TabbedFields(QuestionSolution, label='Ответ', tabs=('С выбором варианта', 'С выбором нескольких вариантов', 'Установление соответствия', 'Дополнение фразой'))
    submit = SubmitField('Добавить вопрос')