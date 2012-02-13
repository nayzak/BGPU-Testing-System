from lib.request import BaseRequest
from whirlwind.view.decorators import role_required, route
from application.forms.manage_organization import CreateOrganizationForm


@route('/admin/organization/create')
class CreateOrganizationHandler(BaseRequest):
    @role_required('admin')
    def get(self):
        self.render_template('/admin/create_organization.html', form=CreateOrganizationForm())

    @role_required('admin')
    def post(self):
        form = CreateOrganizationForm(self.request.arguments)
        if not form.validate():
            self.render_template('/admin/create_organization.html', form=form)
            return
