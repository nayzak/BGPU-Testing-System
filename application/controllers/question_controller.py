#coding: utf-8
from lib.request import BaseRequest
from lib.decorators import role_required
from whirlwind.view.decorators import route
from application.forms.manage_questions import CreateQuestionForm


@route('/admin/question/create')
class CreateQuestionHandler(BaseRequest):
    template = '/admin/create_admin.html'
    title = 'Добавление вопроса'

    @role_required('tutor')
    def get(self):
        self.render_template(form=CreateQuestionForm())

    @role_required('tutor')
    def post(self):
        print self.request.arguments
        form = CreateQuestionForm(self.request.arguments)
        self.render_template(form=form)
        print form.data
