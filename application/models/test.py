from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId
from pymongo import *
import datetime
from lib.utils import Solution


@Mongo.db.connection.register
class Test(Document):
    '''
        _id - шестизначный id-ключ-пароль
        executed - закончен ли тест
        questions_count - количество вопросов в тесте
        max_grade - шкала оценки (пятибальная)
        max_execution_time - время, отведенное для решения теста
        questions - список словарей типа {question_id: ObjectId, variants: unicode}. Variants - варианты ответа для пары типов вопросов
        executed_date - дата прохождения теста
        answers - список ответов. Индексы соответствуют списку вопросов.
        execution_time - время, потраченное на решение теста
        score - набранный балл (сложность вопросов)
        grade - рекомендованная оценка
    '''
    structure = {
        '_id': unicode,
        'student_id': ObjectId,
        'test_template_id': ObjectId,
        'executed': bool,
        'questions_count': int,
        'max_grade': int,
        'max_execution_time': int,
        'questions': [dict],
        'executed_date': datetime.datetime,
        'results': {
            'answers': [Solution],
            'execution_time': int,
            'right_count': int,
            'wrong_count': int,
            'ignored_count': int,
            'score': int,
            'grade': int
        }
    }

    required_fields = ['student_id', 'test_template_id', 'executed', 'questions_count', 'max_grade', 'questions', 'executed_date']

    default_values = {'executed': False, 'max_grade': 5}

    use_dot_notation = True
