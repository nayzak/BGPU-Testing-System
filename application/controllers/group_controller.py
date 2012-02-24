#coding: utf-8
from lib.request import BaseRequest
from lib.decorators import role_required
from whirlwind.view.decorators import route
from application.models.group import Group
from application.forms.manage_group import CreateGroupForm, EditGroupForm
from pymongo.objectid import ObjectId
from application.views.helpers.tables import Paginator


@route('/admin/group/create')
class CreateGroupHandler(BaseRequest):
    title = 'Добавление группы'
    template = '/admin/create_admin.html'

    @role_required('tutor')
    def get(self):
        self.render_template(self.template, title=self.title, form=CreateGroupForm())

    @role_required('tutor')
    def post(self):
        form = CreateGroupForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, title=self.title, form=form)
            return
        Group.create_group(
            name=form.data['name'],
            profession=form.data['profession'],
            created_at=form.data['created_at'],
            graduated=form.data['graduated'],
            organization_id=ObjectId(form.data['organization'].decode('hex'))
        )
        self.flash.success = 'Группа успешно добавлена.'
        self.redirect('/admin/group/list')


@route(r'/admin/group/edit/([0-9a-f]{24})')
class EditGroupHandler(BaseRequest):
    title = 'Редактирование группы'
    template = '/admin/create_admin.html'

    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        group = Group.get_by('_id', _id)
        form = EditGroupForm(
            name=group.name,
            profession=group.profession,
            created_at=group.created_at,
            graduated=group.graduated,
            organization=unicode(group.organization.id)
        )
        self.render_template(self.template, title=self.title, form=form)

    @role_required('tutor')
    def post(self, _id):
        _id = ObjectId(_id.decode('hex'))
        form = EditGroupForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, title=self.title, form=form)
            return
        Group.update_group(
            _id=_id,
            name=form.data['name'],
            profession=form.data['profession'],
            created_at=form.data['created_at'],
            graduated=form.data['graduated'],
            organization_id=ObjectId(form.data['organization'].decode('hex'))
        )
        self.flash.success = 'Группа успешно сохранена.'
        self.redirect('/admin/group/list')


@route(r'/admin/group/remove/([a-f0-9]{24})')
class RemoveGroupHandler(BaseRequest):
    @role_required('admin')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        Group.remove(_id)
        self.flash.success = 'Группа успешно удаленa.'
        self.redirect(self.request.headers.get('Referer', '/admin/group/list'))


@route('/admin/group/list')
class ListGroupHandler(BaseRequest):
    title = 'Группы'
    template = '/admin/data_list.html'

    @role_required('tutor')
    def get(self):
        list_args = {
            'fields': [('get_course', 'Курс'),
                       ('name', 'Название'),
                       ('profession', 'Специальность'),
                       ('organization.name', 'Учебное заведение')],
            'actions': {'remove': ('/admin/group/remove/{}', '_id'),
                        'edit': ('/admin/group/edit/{}', '_id'),
                        'view': ('/admin/group/{}', '_id')}
        }
        page = self.get_argument('page', 0)
        sort = self.get_argument('sort', 'organization.name')
        dest = self.get_argument('dest', 1)
        paginator = Paginator(Group.get_all(sort, dest), self.request.full_url(), page, 10)
        self.render_template(
            self.template,
            title=self.title,
            data=paginator.page,
            list_args=list_args,
            paginator=paginator
        )


@route(r'/admin/group/([a-f0-9]{24})')
class ViewGroupHandler(BaseRequest):
    title = 'Группа'
    template = '/admin/view_group.html'

    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        group = Group.get_by('_id', _id)
        if not group:
            self.redirect('/admin/group/list')
        self.render_template(self.template, title=self.title, group=group)
