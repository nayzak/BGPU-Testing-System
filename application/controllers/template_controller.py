#coding: utf-8
from application.models.question import Question
from lib.request import BaseRequest
from lib.decorators import role_required
from whirlwind.view.decorators import route
from application.forms.manage_template import CreateTemplateForm
from pymongo.objectid import ObjectId
import json

@route('/admin/template/create')
class CreateTemplateHandler(BaseRequest):
    template = '/admin/create_admin.html'
    title = 'Добавление шаблона теста'

    @role_required('tutor')
    def get(self):
        self.render_template(form=CreateTemplateForm())

@route('/admin/template/complexity')
class CreateComplexityHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        import urlparse
        params = urlparse.parse_qs(self.request.body)
        for param, values in params.items():
            for value in values:
                if (value == 'none'): del params[param]
                elif (param == 'module' or param == 'subject'):
                    params.update({'position.' + param : value})
                    del params[param]
        data = [{'complexity' : question} for question in Question.find_questons(params, {'complexity':1}, 'complexity')]
        self.write(json.dumps(data))

@route('/admin/template/module')
class CreateModuleHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        import urlparse
        params = urlparse.parse_qs(self.request.body)
        for param, values in params.items():
            for value in values:
                if (value == 'none'): del params[param]
                elif (param == 'subject'):
                    params.update({'position.' + param : value})
                    del params[param]
        data = [{'module' : question} for question in Question.find_questons(params, {'position.module':1}, 'position.module')]
        self.write(json.dumps(data))

@route('/admin/template/subject')
class CreateSubjectHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        import urlparse
        params = urlparse.parse_qs(self.request.body)
        for param, values in params.items():
            for value in values:
                if (value == 'none'): del params[param]
                else: params[param] = value
        data = [{'subject' : question} for question in Question.find_questons(params, {'position.subject':1},'position.subject')]
        self.write(json.dumps(data))

@route('/admin/template/updatelist')
class CreateUpdateListHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        import urlparse
        params = urlparse.parse_qs(self.request.body)
        for param, values in params.items():
            for value in values:
                if (value == 'none'): del params[param]
                elif (param == 'subject' or param == 'module'):
                    params.update({'position.' + param : value})
                    del params[param]
                elif (param =='complexity'): params[param] = float(value)
                else: params[param] = value
        data = [Question.dict_value_to_string(question) for question in Question.find_questons(params)]
        self.write(json.dumps(data))
