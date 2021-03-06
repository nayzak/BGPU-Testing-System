#coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route
from lib.decorators import role_required
from application.forms.manage_tutor import CreateTutorForm, EditTutorForm
from application.models.tutor import Tutor
from application.views.helpers.tables import Paginator
from tornado.web import HTTPError
from bson.objectid import ObjectId


@route('/admin/tutor/create')
class CreateTutorHandler(BaseRequest):
    title = 'Добавление преподавателя'
    template = '/admin/create_admin.html'

    @role_required('admin')
    def get(self):
        self.render_template(form=CreateTutorForm())

    @role_required('admin')
    def post(self):
        form = CreateTutorForm(self.request.arguments)
        if not form.validate():
            self.render_template(form=form)
            return
        Tutor.create_tutor(
            first_name=form.data['first_name'],
            middle_name=form.data['middle_name'],
            last_name=form.data['last_name'],
            email=form.data['email'],
            password=form.data['password'],
            position=form.data['position'],
            organization_id=form.data['organization']
        )
        self.flash.success = 'Преподаватель успешно добавлен'
        self.redirect('/admin/tutor/list')


@route(r'/admin/tutor/edit/([0-9a-f]{24})')
class EditTutorHandler(BaseRequest):
    title = 'Редактирование профиля преподавателя'
    template = '/admin/create_admin.html'

    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        if self.current_user['_type'] != 'Admin' and self.current_user['_id'] != _id:
            raise HTTPError(403)
        tutor = Tutor.get_by('_id', _id)
        form = EditTutorForm(
            first_name=tutor.name.first,
            middle_name=tutor.name.middle,
            last_name=tutor.name.last,
            email=tutor.email,
            position=tutor.position,
            organization=unicode(tutor.organization.id) if 'id' in tutor.organization else '0',
            userid=self.current_user['_id']
        )
        self.render_template(form=form)

    @role_required('tutor')
    def post(self, _id):
        _id = ObjectId(_id.decode('hex'))
        if self.current_user['_type'] != 'Admin' and self.current_user['_id'] != _id:
            raise HTTPError(403)
        form = EditTutorForm(self.request.arguments)
        if not form.validate():
            self.render_template(form=form)
            return
        Tutor.update_tutor(
            _id=_id,
            first_name=form.data['first_name'],
            middle_name=form.data['middle_name'],
            last_name=form.data['last_name'],
            email=form.data['email'],
            position=form.data['position'],
            organization_id=form.data['organization']
        )
        self.flash.success = 'Профиль преподавателя успешно изменен.'
        self.redirect('/admin/tutor/list')


@route(r'/admin/tutor/remove/([a-f0-9]{24})')
class RemoveTutorHandler(BaseRequest):
    @role_required('admin')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        Tutor.remove(_id)
        self.flash.success = 'Преподаватель успешно удален.'
        self.redirect(self.request.headers.get('Referer', '/admin/tutor/list'))


@route('/admin/tutor/list')
class ListTutorHandler(BaseRequest):
    title = 'Преподаватели'
    template = '/admin/data_list.html'

    @role_required('tutor')
    def get(self):
        list_args = {
            'fields': [('name.last', 'Фамилия'),
                       ('name.first', 'Имя'),
                       ('name.middle', 'Отчество'),
                       ('position', 'Должность'),
                       ('organization.name', 'Учебное заведение')],
            'actions': {'remove': ('/admin/tutor/remove/{}', '_id'),
                        'edit': ('/admin/tutor/edit/{}', '_id'),
                        'chpass': ('/admin/profile/chpass/{}', '_id'),
                        'view': ('/admin/tutor/{}', '_id')}
        }
        page = self.get_argument('page', 0)
        sort = self.get_argument('sort', 'name.last')
        dest = self.get_argument('dest', 1)
        paginator = Paginator(Tutor.get_all(sort, dest), self.request.full_url(), page, 10)
        self.render_template(
            data=paginator.page,
            list_args=list_args,
            paginator=paginator
        )


@route(r'/admin/tutor/([a-f0-9]{24})')
class ViewTutorHandler(BaseRequest):
    title = 'Профиль преподавателя'
    template = '/admin/view_tutor.html'

    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        tutor = Tutor.get_by('_id', _id)
        if not tutor:
            self.redirect('/admin/tutor/list')
        self.render_template(tutor=tutor)
