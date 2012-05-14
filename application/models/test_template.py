#coding: utf-8
from whirlwind.db.mongo import Mongo
from bson.objectid import ObjectId
from pymongo import *
from mongokit import *
import datetime

@Mongo.db.connection.register
class TestTemplate(Document):
    '''
        title = название шаблона
        description = описание
        questions = набор вопросов
        author_id = автор шаблона
        created_at = дата создания
        history = история
    '''

    structure = {
        'title': unicode,
        'description': unicode,
        'questions': [ObjectId],
        'author_id': ObjectId,
        'created_at': datetime.datetime,
        'history': [dict]  # editor_id:ObjectId, modify_date:datetime, comment:unicode
    }

    required_fields = ['title', 'questions', 'author_id']

    use_dot_notations = True

    @staticmethod
    def instance(title, description, questions, author_id, created_at, history):
        template = Mongo.db.ui.templates.TestTemplate()
        template['title'] = unicode(title)
        template['description'] = description
        template['questions'] = questions
        template['author_id'] = author_id
        template['created_at'] = created_at
        template['history'] = history
        return template

    @staticmethod
    def create_template(title, description, questions, author_id, created_at, history):
        template = TestTemplate.instance(title, description, questions, author_id, created_at, history)
        print template
        Mongo.db.ui.templates.insert(template)
        return template
