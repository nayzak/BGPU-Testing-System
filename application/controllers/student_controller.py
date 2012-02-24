# coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route
from lib.decorators import role_required
from application.models.student import Student
from application.models.student import Group
from application.forms.manage_student import CreateStudentForm, EditStudentForm
from application.views.helpers.tables import Paginator
from pymongo.objectid import ObjectId
from tornado.web import HTTPError
import json


@route('/admin/student/create')
class CreateStudentHandler(BaseRequest):
    title = 'Добавление студента'
    template = '/admin/create_admin.html'

    @role_required('tutor')
    def get(self):
        self.render_template(self.template, title=self.title, form=CreateStudentForm())

    @role_required('tutor')
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
    title = 'Список студентов'
    template = '/admin/data_list.html'

    @role_required('tutor')
    def get(self):
        list_args = {
            'fields': [('name.last', 'Фамилия'),
                       ('name.first', 'Имя'),
                       ('name.middle', 'Отчество'),
                       ('organization.name', 'Учебное заведение'),
                       ('get_course', 'Курс'),
                       ('group.name', 'Группа')],
            'actions': {'remove': ('/admin/student/remove/{}', '_id'),
                        'edit': ('/admin/student/edit/{}', '_id')}
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
    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        Student.remove(_id)
        self.flash.success = 'Студент успешно удален.'
        self.redirect(self.request.headers.get('Referer', '/admin/student/list'))


@route(r'/admin/student/edit/([0-9a-f]{24})')
class EditStudentHandler(BaseRequest):
    title = 'Редактирование профиля студента'
    template = '/admin/create_admin.html'

    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        student = Student.get_by('_id', _id)
        form = EditStudentForm(
            first_name = student.name.first,
            middle_name = student.name.middle,
            last_name = student.name.last,
            group_id= student.group.id,
            organization_id = student.organization.id,
            userid = self.current_user['_id']
        )
        self.render_template(self.template, title=self.title, form=form)

    @role_required('tutor')
    def post(self, _id):
        _id = ObjectId(_id.decode('hex'))
        form = EditStudentForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, title=self.title, form=form)
            return
        Student.update_student(
            _id=_id,
            first_name=form.data['first_name'],
            middle_name=form.data['middle_name'],
            last_name=form.data['last_name'],
            group_id=form.data['group_id']
        )
        self.flash.success = 'Профиль студента успешно изменен.'
        self.redirect('/admin/student/list')


@route('/admin/student/updatelist')
class CreateUpdateListHandler(BaseRequest):

    def post(self):
        try:
            items = Group.select_field_choises(ObjectId(self.request.body))
        except:
            items = list()
        data = [{'group_id': gid, 'name': name} for gid, name in items]
        self.write(json.dumps(data))
