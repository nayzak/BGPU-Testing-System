# coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route, role_required
from application.models.admin import Admin
from application.models.user import User
from application.forms.create_admin import CreateAdminForm


@route('/admin')
class IndexHandler(BaseRequest):
    @role_required('admin')
    def get(self):
        print self.current_user
        self.render_template('/admin/index.html', user=self.current_user)


@route('/admin/init')
class CreateAdminHandler(BaseRequest):
    def get(self):
        if Admin.is_admin_created():
            self.redirect('/admin/login')

        self.render_template('/admin/create_admin.html', form=CreateAdminForm())

    def post(self):
        if Admin.is_admin_created():
            self.redirect('/admin/login')

        form = CreateAdminForm(**self.get_all_arguments())

        if not form.validate():
            self.render_template('/admin/create_admin.html', form=form)

        Admin.create_admin(
            form.first_name.data,
            form.last_name.data,
            form.middle_name.data,
            form.email.data,
            form.password.data
        )

        self.redirect('/admin/login')
