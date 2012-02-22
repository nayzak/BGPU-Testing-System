# coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route
from lib.decorators import role_required
from application.models.student import Student
from application.forms.manage_student import CreateStudentForm
from application.views.helpers.tables import Paginator
from pymongo.objectid import ObjectId
#from tornado.web import HTTPError

@route('/admin/student/create')
class CreateStudentHandler(BaseRequest):
    title = 'Добавление студента'
    template = '/admin/create_admin.html'

    @role_required('admin')
    def get(self):
        self.render_template(self.template, title=self.title, form=CreateStudentForm())

    @role_required('admin')
    def post(self):
        form = CreateStudentForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, title=self.title, form=form)
            return
        Student.create_student(
            first_name=form.data['first_name'],
            middle_name=form.data['middle_name'],
            last_name=form.data['last_name'],
            group_id=form.data['group_id']
        )
        self.flash.success = 'Студент успешно добавлен'
        self.redirect('/admin/student/list')

@route('/admin/student/list')
class ListStudentHandler(BaseRequest):
    title = 'Студенты'
    template = '/admin/data_list.html'

    @role_required('tutor')
    def get(self):
        list_args = {
            'fields': [('name.last', 'Фамилия'),
                       ('name.first', 'Имя'),
                       ('name.middle', 'Отчество'),
                       ('organization.name', 'Учебное заведение'),
                       ('course', 'Курс'),
                       ('group.name', 'Группа')],
            'actions': {'remove': ('/admin/student/remove/{}', '_id'),
                        'edit': ('/admin/student/edit/{}', '_id'),
                        'chpass': ('/admin/profile/chpass/{}', '_id'),
                        'view': ('/admin/student/{}', '_id')}
        }
        page = self.get_argument('page', 0)
        sort = self.get_argument('sort', 'name.last')
        dest = self.get_argument('dest', 1)
        paginator = Paginator(Student.get_all(sort, dest), self.request.full_url(), page, 10)
        self.render_template(
            self.template,
            title=self.title,
            data=paginator.page,
            list_args=list_args,
            paginator=paginator
        )

@route(r'/admin/student/remove/([a-f0-9]{24})')
class RemoveStudentHandler(BaseRequest):
    @role_required('admin')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        Student.remove(_id)
        self.flash.success = 'Студент успешно удален.'
        self.redirect(self.request.headers.get('Referer', '/admin/student/list'))
