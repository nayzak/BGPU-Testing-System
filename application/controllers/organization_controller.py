#coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route
from lib.decorators import role_required
from application.forms.manage_organization import CreateOrganizationForm, EditOrganizationForm
from application.models.organization import Organization
from pymongo.objectid import ObjectId
from tornado.web import HTTPError
from application.views.helpers.tables import Paginator


@route('/admin/organization/create')
class CreateOrganizationHandler(BaseRequest):
    title = 'Новое учебное заведение'
    template = '/admin/create_organization.html'

    @role_required('admin')
    def get(self):
        form = CreateOrganizationForm()
        self.render_template(self.template, form=form, title=self.title)

    @role_required('admin')
    def post(self):
        form = CreateOrganizationForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, form=form, title=self.title)
            return
        Organization.create_organization(
            name=form.data.get('name', ''),
            full_name=form.data.get('full_name', ''),
            status=form.data.get('status', ''),
            contacts=form.data.get('contacts', list())
        )
        self.flash.success = 'Учебное заведение успешно добавлено.'
        self.redirect('/admin/organization/list')


@route(r'/admin/organization/edit/([0-9a-z]+)')
class EditOrganizationHandler(BaseRequest):
    title = 'Редактирование учебного заведения'
    template = '/admin/create_organization.html'

    @role_required('admin')
    def get(self, _id):
        try:
            _id = ObjectId(_id.decode('hex'))
        except:
            raise HTTPError(404)
        org = Organization.get_by('_id', _id)
        form = EditOrganizationForm(obj=org)
        self.render_template(self.template, form=form, title=self.title)

    @role_required('admin')
    def post(self, _id):
        try:
            _id = ObjectId(_id.decode('hex'))
        except:
            raise HTTPError(404)
        form = CreateOrganizationForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, form=form, title=self.title)
            return
        Organization.update_organization(
            _id=_id,
            name=form.data.get('name', ''),
            full_name=form.data.get('full_name', ''),
            status=form.data.get('status', ''),
            contacts=form.data.get('contacts', list())
        )
        self.flash.success = 'Информация по учебному заведению успешно сохранена.'
        self.redirect('/admin/organization/list')


@route('/admin/organization/list')
class ListOrganizationHandler(BaseRequest):
    title = 'Учебные заведения'
    template = '/admin/data_list.html'

    @role_required('tutor')
    def get(self):
        list_args = {
            'fields': [('name', 'Название'),
                       ('full_name', 'Полное название'),
                       ('status', 'Статус'),
                       ('contacts.city', 'Город')],
            'actions': {'remove': ('/admin/organization/remove/{}', '_id'),
                        'edit': ('/admin/organization/edit/{}', '_id'),
                        'view': ('/admin/organization/{}', '_id')}
        }
        page = self.get_argument('page', 0)
        sort = self.get_argument('sort', 'name')
        dest = self.get_argument('dest', 1)
        paginator = Paginator(Organization.get_all(sort, dest), self.request.full_url(), page, 10)
        self.render_template(
            self.template,
            title=self.title,
            data=paginator.page,
            list_args=list_args,
            paginator=paginator
        )


@route(r'/admin/organization/remove/([0-9a-z]+)')
class RemoveOrganizationHandler(BaseRequest):
    @role_required('admin')
    def get(self, _id):
        try:
            _id = ObjectId(_id.decode('hex'))
        except:
            raise HTTPError(404)
        Organization.remove(_id)
        self.flash.success = 'Учебное заведение успешно удалено'
        self.redirect(self.request.headers.get('Referer', '/admin/organization/list'))


@route(r'/admin/organization/([0-9a-z]+)')
class ViewOrganizationHandler(BaseRequest):
    title = 'Просмотр учебного заведения'
    template = '/admin/view_organization.html'

    @role_required('tutor')
    def get(self, _id):
        try:
            _id = ObjectId(_id.decode('hex'))
        except:
            raise HTTPError(404)
        org = Organization.get_by('_id', _id)
        if not org:
            self.redirect('/admin/organization/list')
        self.render_template(self.template, title=self.title, org=org)
