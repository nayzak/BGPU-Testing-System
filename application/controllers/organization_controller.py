#coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import role_required, route
from application.forms.manage_organization import CreateOrganizationForm, EditOrganizationForm
from application.models.organization import Organization
from pymongo.objectid import ObjectId
from tornado.web import HTTPError


@route('/admin/organization/create')
class CreateOrganizationHandler(BaseRequest):
    @role_required('admin')
    def get(self):
        form = CreateOrganizationForm()
        form.contacts.append_entry()
        form.contacts.entries[0].phones.append_entry()
        self.render_template('/admin/create_organization.html', form=form)

    @role_required('admin')
    def post(self):
        form = CreateOrganizationForm(self.request.arguments)
        if not form.validate():
            self.render_template('/admin/create_organization.html', form=form)
            return
        Organization.create_organization(
            name=form.data.get('name', ''),
            full_name=form.data.get('full_name', ''),
            status=form.data.get('status', ''),
            contacts=form.data.get('contacts', list())
        )
        self.redirect('/admin')


@route(r'/admin/organization/edit/([0-9a-z]+)')
class EditOrganizationHandler(BaseRequest):
    @role_required('admin')
    def get(self, _id):
        try:
            _id = ObjectId(_id.decode('hex'))
        except:
            raise HTTPError(404)
        org = Organization.get_by('_id', _id)
        form = EditOrganizationForm(obj=org)
        if not len(form.contacts):
            form.contacts.append_entry()
        if not len(form.contacts.entries[0].phones):
            form.contacts.entries[0].phones.append_entry()
        self.render_template('/admin/edit_organization.html', form=form)

    @role_required('admin')
    def post(self, _id):
        try:
            _id = ObjectId(_id.decode('hex'))
        except:
            raise HTTPError(404)
        form = CreateOrganizationForm(self.request.arguments)
        if not form.validate():
            self.render_template('/admin/edit_organization.html', form=form)
            return
        Organization.update_organization(
            _id=_id,
            name=form.data.get('name', ''),
            full_name=form.data.get('full_name', ''),
            status=form.data.get('status', ''),
            contacts=form.data.get('contacts', list())
        )
        self.redirect('/admin')
