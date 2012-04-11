#coding: utf-8
from lib.request import BaseRequest
from lib.decorators import role_required
from whirlwind.view.decorators import route
from application.forms.manage_template import CreateTemplateForm

@route('/admin/template/create')
class CreateTemplateHandler(BaseRequest):
    template = '/admin/create_admin.html'
    title = 'Добавление шаблона теста'

    @role_required('tutor')
    def get(self):
        self.render_template(form=CreateTemplateForm())
