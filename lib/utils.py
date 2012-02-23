#coding: utf-8
from mongokit.schema_document import CustomType
import pickle

ST_ONE_ANSWER = 0
ST_SOME_ANSWERS = 1
ST_MAP = 2
ST_APPEND = 3


class Solution(CustomType):
    mongo_type = unicode

    def __init__(self, solution_type=None, solution=None):
        if not self.validate_args(solution_type, solution):
            raise Exception('Solution type is invalid')
        self._type = solution_type
        self.solution = solution

    def __cmp__(self, other):
        if not isinstance(other, Solution):
            return -1
        if self._type == other._type and self.solution == other.solution:
            return 0
        else:
            return 1

    def to_bson(self, value):
        return unicode(pickle.dumps((value._type, value.solution)))

    def to_python(self, value):
        args = pickle.loads(value.encode())
        return Solution(args[0], args[1])

    def validate_args(self, solution_type, solution):
        if solution_type not in (ST_ONE_ANSWER, ST_SOME_ANSWERS, ST_MAP, ST_APPEND):
            return False
        types = {
            ST_ONE_ANSWER: unicode,
            ST_SOME_ANSWERS: [unicode],
            ST_MAP: [(unicode, unicode)],
            ST_APPEND: unicode
        }

        def validate(python_type, value):
            if type(python_type).__name__ == 'type':
                return type(value) is python_type
            elif type(python_type).__name__ in ('list', 'tuple'):
                if type(value).__name__ != type(python_type).__name__:
                    return False
                if len(python_type) > 0 and len(value) > 0:
                    for element in value:
                        if not validate(python_type[0], element):
                            return False
                else:
                    return False
            return True

        return validate(types[solution_type], solution)
