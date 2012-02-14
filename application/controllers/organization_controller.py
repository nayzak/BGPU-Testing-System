#coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import role_required, route
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
        renderer_args = {
            'name': 'Название',
            'full_name': 'Полное название',
            'status': 'Статус',
            'contacts.city': 'Город',
            'links': {
                'remove': ('/admin/organization/remove/{}', '_id'),
                'edit': ('/admin/organization/edit/{}', '_id')
            }
        }
        page = self.get_argument('page', 0)
        paginator = Paginator(Organization.get_all(), self.request.full_url(), page, 5)
        self.render_template(self.template, title=self.title, data=paginator.page, fields=renderer_args, paginator=paginator)
