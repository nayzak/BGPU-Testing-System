#coding: utf-8
from application.models.question import Question
from lib.request import BaseRequest
from lib.decorators import role_required
from lib.tools import Tools
from whirlwind.view.decorators import route
from application.forms.manage_template import CreateTemplateForm
from application.models.test_template import TestTemplate
from bson.objectid import ObjectId
import json
import urlparse
import datetime

@route('/admin/template/create')
class CreateTemplateHandler(BaseRequest):
    template = '/admin/create_admin.html'
    title = 'Добавление шаблона теста'

    @role_required('tutor')
    def get(self):
        self.render_template(form=CreateTemplateForm())

    @role_required('tutor')
    def post(self):
        form = CreateTemplateForm(self.request.arguments)
        TestTemplate.create_template(
            title = form.data['template_title'],
            description = form.data['description'],
            questions = form.data['made_list'],
            author_id = self.current_user,
            created_at = datetime.datetime.now(),
            history = [
                {'editor_id': self.current_user},
                {'modify_date': datetime.datetime.now()},
                {'comment': form.data['comments']}
            ],
        )
        self.flash.success = 'Шаблон успешно добавлен'
        self.redirect('/admin/template/create')

@route('/admin/template/updateComplexityFields')
class CreateUpdateComplexityFieldsHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        params = Tools.quary_from_params(urlparse.parse_qs(self.request.body))
        data = [{'complexity' : question} for question in Question.find_questions(params, {'complexity':1}, 'complexity')]
        self.write(json.dumps(data))

@route('/admin/template/updateModuleFields')
class CreateUpdateModuleFieldsHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        params = Tools.quary_from_params(urlparse.parse_qs(self.request.body))
        data = [{'module' : question} for question in Question.find_questions(params, {'position.module':1}, 'position.module')]
        self.write(json.dumps(data))

@route('/admin/template/updateSubjectFields')
class CreateUpdateSubjectFieldsHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        params = Tools.quary_from_params(urlparse.parse_qs(self.request.body))
        data = [{'subject' : question} for question in Question.find_questions(params, {'position.subject':1},'position.subject')]
        self.write(json.dumps(data))

@route('/admin/template/updateQuestionList')
class CreateUpdateQuestionListHandler(BaseRequest):

    @role_required('tutor')
    def post(self):
        params = Tools.quary_from_params(urlparse.parse_qs(self.request.body))
        data = [Question.dict_value_to_string(question) for question in Question.find_questions(params)]
        self.write(json.dumps(data))
