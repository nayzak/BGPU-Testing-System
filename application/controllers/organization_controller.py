#coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import role_required, route
from application.forms.manage_organization import CreateOrganizationForm
from application.models.organization import Organization


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
            fullname=form.data.get('fullname', ''),
            status=form.data.get('status', ''),
            contacts=form.data.get('contacts', list())
        )
        self.redirect('/admin')
